from .treehelper import TreeHelper
from .shaderops import *
from .shadervariables import * 

class GeometryTreeBuilder:
    def __init__(self, program):
        self.program = program
        self.treehelper = TreeHelper()
    
    def typeToSocket(self,variable_type):
        if variable_type=="geometry":
            return "NodeSocketGeometry"
        if variable_type=="vector":
            return "NodeSocketVector"
        if variable_type=="float":
            return "NodeSocketFloat"
        if variable_type=="int":
            return "NodeSocketInt"
        raise TypeError('Invalid type')

    def CreateInput(self, inst):
        sock = self.treehelper.addInputSocket(self.typeToSocket(inst.input_type),inst.name)
        if not inst.default_value is None:
            print("not setting default, totally broken")

    def CreateOutput(self, inst):
        self.treehelper.addOutputSocket(inst.output_var.name,inst.name)

    def CreateFloat(self, inst):
        node = self.treehelper.addNode("ShaderNodeValue", {})
        node.outputs[0].default_value = inst.value
        self.treehelper.register_variable(node.outputs[0], inst.output_var)
        node.label = inst.output_var

    def CreateVector(self, inst):
        node = self.treehelper.addNode("ShaderNodeCombineXYZ", {})
        key = ( inst.x , inst.y, inst.z )
        self.SetOrLink(node.inputs[0], inst.x)
        self.SetOrLink(node.inputs[1], inst.y)
        self.SetOrLink(node.inputs[2], inst.z)
        self.treehelper.register_variable(node.outputs[0], inst.output_var)
        node.label = inst.output_var

    def ScaleGeometryConst(self, inst):
        node = self.treehelper.addNode("GeometryNodeTransform", {})
        SI = node.inputs[0]
        self.treehelper.Link(SI, inst.input_var)
        self.treehelper.register_variable(node.outputs[0], inst.output_var)
        node.inputs[3].default_value = [ inst.scale, inst.scale, inst.scale ]

    def TranslateGeometry(self, inst):
        node = self.treehelper.addNode("GeometryNodeTransform", {})
        self.treehelper.Link(node.inputs[0], inst.input_var)
        self.treehelper.Link(node.inputs[1], inst.offset.name)
        self.treehelper.register_variable(node.outputs[0], inst.output_var)

    def JoinGeometry(self, inst):
        node = self.treehelper.addNode("GeometryNodeJoinGeometry", {})
        for geo in inst.geometries:
            self.treehelper.Link(node.inputs[0], geo.name)
        self.treehelper.register_variable(node.outputs[0], inst.output_var)

    def SetOrLink(self, socket, value):
        if(isinstance(value, ShaderVariable)):
            self.treehelper.Link(socket, value.name)
        else:
            #print("setting %s to %s" % (socket, value) )
            socket.default_value = value

    def PrimitiveGrid(self, inst):
        node = self.treehelper.addNode("GeometryNodeMeshGrid", {})
        self.SetOrLink(node.inputs[0], inst.width)
        self.SetOrLink(node.inputs[1], inst.height)
        self.SetOrLink(node.inputs[2], inst.vertX)
        self.SetOrLink(node.inputs[3], inst.vertY)
        self.treehelper.register_variable(node.outputs[0], inst.output_var)

    def RawCall(self, inst):
        node = self.treehelper.addNode(inst.nodename, {})
        for k in inst.input_vars:
            val = inst.input_vars[k]
            if not val is None:
                #print("Setting %s to %s (%s)" % (k, val,type(val) ))
                self.SetOrLink(node.inputs[k], val)
        for k in inst.input_props:
            val = inst.input_props[k]
            #print("Setting %s to %s (%s)" % (k, val,type(val) ))
            if not val is None:
                setattr(node, k, val)
        for k in inst.output_vars._mapping_:
            outvar = inst.output_vars[inst.output_vars._mapping_[k]]
            self.treehelper.register_variable(node.outputs[k], outvar.name)
        node.label = outvar.name

    def AttributeRemove(self,inst):
        node = self.treehelper.addNode("GeometryNodeAttributeRemove", {})
        self.treehelper.Link(node.inputs[0], inst.geometry.name)
        for attr in inst.attributes:
            sval = self.treehelper.addNode("FunctionNodeInputString", {})
            sval.string = attr
            self.treehelper.Link(node.inputs[1], sval.outputs[0])
        self.treehelper.register_variable(node.outputs[0], inst.output_var)
        pass

    def generate(self):
        print("Starting tree build for %s" % (self.treehelper.getNodetree().name))
        for inst in self.program:
            if isinstance(inst, ShaderOpCreateInput):
                self.CreateInput(inst)
            elif isinstance(inst, ShaderOpCreateOutput):
                self.CreateOutput(inst)
            elif isinstance(inst, ShaderOpScaleGeometryConst):
                self.ScaleGeometryConst(inst)
            elif isinstance(inst, ShaderOpCreateVector):
                self.CreateVector(inst)
            elif isinstance(inst, ShaderOpTranslateGeometry):
                self.TranslateGeometry(inst)
            elif isinstance(inst, ShaderOpJoin):
                self.JoinGeometry(inst)
            elif isinstance(inst, ShaderOpPrimitiveGrid):
                self.PrimitiveGrid(inst)
            elif isinstance(inst, ShaderOpRawNodeCall):
                self.RawCall(inst)
            elif isinstance(inst, ShaderOpCreateFloat):
                self.CreateFloat(inst)
            elif isinstance(inst, ShaderOpAttributeRemove):
                self.AttributeRemove(inst)
            else:
                print("^^ UNHANDLED!!!!")
            
        return self.treehelper.getNodetree()
