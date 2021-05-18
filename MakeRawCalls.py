import bpy
import inspect
from pprint import pprint
 
group = bpy.data.node_groups['Geometry Nodes.001']
 
def SanatizeName(name):
    res = name.replace(' ','')
    if len(res) == 0:
        res = "unk"
    return res

def make_unique(vals):
    res = []
    counter = { }
    for val in vals:
        if vals.count(val) > 1:
            counter[val] = 0
    for val in vals:
        if val in counter:
            res.append(val+str(counter[val]))
            counter[val] = counter[val]+1
        else:
            res.append(val)
    return res

def map_output_type(socket_type):
    mapping = {
        "NodeSocketFloat": "ShaderVariableFloat",
        "NodeSocketFloatUnsigned": "ShaderVariableFloat",
        "NodeSocketFloatFactor": "ShaderVariableFloat",
        "NodeSocketFloatAngle": "ShaderVariableFloat",
        "NodeSocketFloatDistance": "ShaderVariableFloat",
        "NodeSocketVector": "ShaderVariableVector",
        "NodeSocketVectorTranslation": "ShaderVariableVector",
        "NodeSocketVectorXYZ": "ShaderVariableVector",
        "NodeSocketVectorEuler": "ShaderVariableVector",
        "NodeSocketColor": "ShaderVariableVector",
        "NodeSocketGeometry": "ShaderVariableGeometry",
        "NodeSocketBool": "ShaderVariableUnk",
        "NodeSocketString": "ShaderVariableUnk",
        "NodeSocketInt": "ShaderVariableUnk",
        "NodeSocketObject": "ShaderVariableUnk",
        "NodeSocketCollection": "ShaderVariableUnk",
        "NodeSocketVirtual": "ShaderVariableUnk"
    }
    return mapping[socket_type]
        
 
for type in dir(bpy.types):
    real_type = getattr(bpy.types, type)
    if inspect.isclass(real_type) and issubclass(real_type, bpy.types.Node):
        node = None
        try:
            #if type == "GeometryNodeAttributeVectorMath":
            node = group.nodes.new(type)
        except:
            pass
        if not node is None:
            function_name = node.bl_idname
            input_variables = [ ]
            input_types = [ ]
            input_props = [ ] 
            output_variables = [ ] 
            output_types = [ ]
            #filter out the stuff we do not want/need
            for f in dir(node):
                if f.startswith('__'):
                    continue 
                if f.startswith('bl_'):
                    continue 
                if f in ['inputs','internal_links','outputs','rna_type','type', 'active_preview', 'color', 'dimensions', 'height', 'hide',  'label', 'location', 'mute',  'name',  'select',  'show_options',  'show_preview',  'show_texture',  'use_custom_color', 'width',  'width_hidden', 'draw_buttons', 'draw_buttons_ext', 'input_template', 'is_registered_node_type' ,'output_template', 'parent', 'poll', 'poll_instance', 'socket_value_update', 'update' ]:
                    continue 
                input_props.append(f)
            for i in range(node.inputs.__len__()):
                n = node.inputs[i]
                input_types.append(n.bl_idname)
                input_variables.append(SanatizeName(n.name))
            for i in range(node.outputs.__len__()):
                sock = node.outputs[i]
                output_variables.append(SanatizeName(sock.name))
                output_types.append(map_output_type(sock.bl_idname))
            group.nodes.remove( node )
            sane_input_variables = make_unique(input_variables)
            sane_input_variables_none = [s + ' = None' for s in sane_input_variables + input_props]
            inputs = ", ".join(sane_input_variables_none)
            if len(inputs) > 0:
                inputs = "self, *, "+ inputs 
            print("def %s(%s):" % ( function_name , inputs ))
            print("    inputs = AttrDict()")
            for i in range(len(input_variables)):
                print("    inputs[%s] = %s # %s" % ( i , sane_input_variables[i] , input_types[i] ))
            print("    input_props = AttrDict()")
            for i in range(len(input_props)):
                print("    input_props['%s'] = %s" % ( input_props[i] , input_props[i] ))
            print("    outputs = AttrDict()")
            sane_output_variables = make_unique(output_variables)
            for i in range(len(sane_output_variables)):
                print("    outputs['%s'] = %s(self.parent)" % ( sane_output_variables[i], output_types[i]))
            print("    outputs['_mapping_'] = {")
            for i in range(len(sane_output_variables)):
                print("        %s: '%s'," % ( i, sane_output_variables[i]))
            print("    }")
            print("    self.parent.shader_program.append(ShaderOpRawNodeCall('%s', outputs, inputs, input_props))" % ( function_name ))
            if len(sane_output_variables) == 1:
                print("    return outputs['%s']" % (sane_output_variables[0]))
            else:
                print("    return outputs")
            print("")
