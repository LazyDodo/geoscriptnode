class ShaderOp:
    def Generate(self, treebuilder):
        print("ShaderOp::Generate")

    def __repr__(self):
        return "{}({!r})".format(self.__class__.__name__, self.__dict__)

class ShaderOpCreateInput(ShaderOp):
    def __init__(self, name, input_type, default_value):
        self.name = name
        self.input_type = input_type
        self.default_value = default_value 
        
class ShaderOpCreateOutput(ShaderOp):
    def __init__(self, name, output_var):
        self.name = name
        self.output_var = output_var

class ShaderOpScaleGeometryConst(ShaderOp):
    def __init__(self, output_var, input_var, scale):
        self.output_var = output_var
        self.input_var = input_var
        self.scale = scale

class ShaderOpTranslateGeometry(ShaderOp):
    def __init__(self, output_var, input_var, offset):
        self.output_var = output_var
        self.input_var = input_var
        self.offset = offset

class ShaderOpCreateVector(ShaderOp):
    def __init__(self, output_var, x, y, z):
        self.output_var = output_var
        self.x = x
        self.y = y
        self.z = z

class ShaderOpCreateFloat(ShaderOp):
    def __init__(self, output_var, value):
        self.output_var = output_var
        self.value = value

class ShaderOpJoin(ShaderOp):
    def __init__(self, output_var, geometries):
        self.output_var = output_var
        self.geometries = geometries 

class ShaderOpPrimitiveGrid(ShaderOp):
    def __init__(self, output_var, width , height, vertX, vertY):
        self.output_var = output_var
        self.width = width
        self.height = height
        self.vertX = vertX
        self.vertY = vertY

class ShaderOpRawNodeCall(ShaderOp):
    def __init__(self, nodename, output_vars, input_vars, input_props):
        self.nodename = nodename
        self.output_vars = output_vars
        self.input_vars = input_vars
        self.input_props = input_props

class ShaderOpAttributeRemove(ShaderOp):
    def __init__(self, output_var, geometry, attributes):
        self.output_var = output_var
        self.geometry = geometry
        self.attributes = attributes
