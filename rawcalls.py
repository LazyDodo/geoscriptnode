from .attrdict import AttrDict
from .shadervariables import * 

class RawCalls:
    def __init__(self, parent):
        self.parent = parent

    def FunctionNodeBooleanMath(self, *, Boolean0 = None, Boolean1 = None, operation = None):
        inputs = AttrDict()
        inputs[0] = Boolean0 # NodeSocketBool
        inputs[1] = Boolean1 # NodeSocketBool
        input_props = AttrDict()
        input_props['operation'] = operation
        outputs = AttrDict()
        outputs['Boolean'] = ShaderVariableUnk(self.parent)
        outputs['_mapping_'] = {
            0: 'Boolean',
        }
        self.parent.shader_program.append(ShaderOpRawNodeCall('FunctionNodeBooleanMath', outputs, inputs, input_props))
        return outputs['Boolean']

    def FunctionNodeFloatCompare(self, *, A = None, B = None, Epsilon = None, operation = None):
        inputs = AttrDict()
        inputs[0] = A # NodeSocketFloat
        inputs[1] = B # NodeSocketFloat
        inputs[2] = Epsilon # NodeSocketFloat
        input_props = AttrDict()
        input_props['operation'] = operation
        outputs = AttrDict()
        outputs['Result'] = ShaderVariableUnk(self.parent)
        outputs['_mapping_'] = {
            0: 'Result',
        }
        self.parent.shader_program.append(ShaderOpRawNodeCall('FunctionNodeFloatCompare', outputs, inputs, input_props))
        return outputs['Result']

    def FunctionNodeInputString(self, *, string = None):
        inputs = AttrDict()
        input_props = AttrDict()
        input_props['string'] = string
        outputs = AttrDict()
        outputs['String'] = ShaderVariableUnk(self.parent)
        outputs['_mapping_'] = {
            0: 'String',
        }
        self.parent.shader_program.append(ShaderOpRawNodeCall('FunctionNodeInputString', outputs, inputs, input_props))
        return outputs['String']

    def FunctionNodeInputVector(self, *, vector = None):
        inputs = AttrDict()
        input_props = AttrDict()
        input_props['vector'] = vector
        outputs = AttrDict()
        outputs['Vector'] = ShaderVariableVector(self.parent)
        outputs['_mapping_'] = {
            0: 'Vector',
        }
        self.parent.shader_program.append(ShaderOpRawNodeCall('FunctionNodeInputVector', outputs, inputs, input_props))
        return outputs['Vector']

    def FunctionNodeRandomFloat(self, *, Min = None, Max = None, Seed = None):
        inputs = AttrDict()
        inputs[0] = Min # NodeSocketFloat
        inputs[1] = Max # NodeSocketFloat
        inputs[2] = Seed # NodeSocketInt
        input_props = AttrDict()
        outputs = AttrDict()
        outputs['Value'] = ShaderVariableFloat(self.parent)
        outputs['_mapping_'] = {
            0: 'Value',
        }
        self.parent.shader_program.append(ShaderOpRawNodeCall('FunctionNodeRandomFloat', outputs, inputs, input_props))
        return outputs['Value']

    def GeometryNodeAlignRotationToVector(self, *, Geometry = None, Factor0 = None, Factor1 = None, Vector0 = None, Vector1 = None, axis = None, input_type_factor = None, input_type_vector = None, pivot_axis = None):
        inputs = AttrDict()
        inputs[0] = Geometry # NodeSocketGeometry
        inputs[1] = Factor0 # NodeSocketString
        inputs[2] = Factor1 # NodeSocketFloatFactor
        inputs[3] = Vector0 # NodeSocketString
        inputs[4] = Vector1 # NodeSocketVector
        input_props = AttrDict()
        input_props['axis'] = axis
        input_props['input_type_factor'] = input_type_factor
        input_props['input_type_vector'] = input_type_vector
        input_props['pivot_axis'] = pivot_axis
        outputs = AttrDict()
        outputs['Geometry'] = ShaderVariableGeometry(self.parent)
        outputs['_mapping_'] = {
            0: 'Geometry',
        }
        self.parent.shader_program.append(ShaderOpRawNodeCall('GeometryNodeAlignRotationToVector', outputs, inputs, input_props))
        return outputs['Geometry']

    def GeometryNodeAttributeClamp(self, *, Geometry = None, Attribute = None, Result = None, Min0 = None, Max0 = None, Min1 = None, Max1 = None, Min2 = None, Max2 = None, Min3 = None, Max3 = None, data_type = None, operation = None):
        inputs = AttrDict()
        inputs[0] = Geometry # NodeSocketGeometry
        inputs[1] = Attribute # NodeSocketString
        inputs[2] = Result # NodeSocketString
        inputs[3] = Min0 # NodeSocketVector
        inputs[4] = Max0 # NodeSocketVector
        inputs[5] = Min1 # NodeSocketFloat
        inputs[6] = Max1 # NodeSocketFloat
        inputs[7] = Min2 # NodeSocketInt
        inputs[8] = Max2 # NodeSocketInt
        inputs[9] = Min3 # NodeSocketColor
        inputs[10] = Max3 # NodeSocketColor
        input_props = AttrDict()
        input_props['data_type'] = data_type
        input_props['operation'] = operation
        outputs = AttrDict()
        outputs['Geometry'] = ShaderVariableGeometry(self.parent)
        outputs['_mapping_'] = {
            0: 'Geometry',
        }
        self.parent.shader_program.append(ShaderOpRawNodeCall('GeometryNodeAttributeClamp', outputs, inputs, input_props))
        return outputs['Geometry']

    def GeometryNodeAttributeColorRamp(self, *, Geometry = None, Attribute = None, Result = None, color_ramp = None):
        inputs = AttrDict()
        inputs[0] = Geometry # NodeSocketGeometry
        inputs[1] = Attribute # NodeSocketString
        inputs[2] = Result # NodeSocketString
        input_props = AttrDict()
        input_props['color_ramp'] = color_ramp
        outputs = AttrDict()
        outputs['Geometry'] = ShaderVariableGeometry(self.parent)
        outputs['_mapping_'] = {
            0: 'Geometry',
        }
        self.parent.shader_program.append(ShaderOpRawNodeCall('GeometryNodeAttributeColorRamp', outputs, inputs, input_props))
        return outputs['Geometry']

    def GeometryNodeAttributeCombineXYZ(self, *, Geometry = None, X0 = None, X1 = None, Y0 = None, Y1 = None, Z0 = None, Z1 = None, Result = None, input_type_x = None, input_type_y = None, input_type_z = None):
        inputs = AttrDict()
        inputs[0] = Geometry # NodeSocketGeometry
        inputs[1] = X0 # NodeSocketString
        inputs[2] = X1 # NodeSocketFloat
        inputs[3] = Y0 # NodeSocketString
        inputs[4] = Y1 # NodeSocketFloat
        inputs[5] = Z0 # NodeSocketString
        inputs[6] = Z1 # NodeSocketFloat
        inputs[7] = Result # NodeSocketString
        input_props = AttrDict()
        input_props['input_type_x'] = input_type_x
        input_props['input_type_y'] = input_type_y
        input_props['input_type_z'] = input_type_z
        outputs = AttrDict()
        outputs['Geometry'] = ShaderVariableGeometry(self.parent)
        outputs['_mapping_'] = {
            0: 'Geometry',
        }
        self.parent.shader_program.append(ShaderOpRawNodeCall('GeometryNodeAttributeCombineXYZ', outputs, inputs, input_props))
        return outputs['Geometry']

    def GeometryNodeAttributeCompare(self, *, Geometry = None, A0 = None, A1 = None, A2 = None, A3 = None, B0 = None, B1 = None, B2 = None, B3 = None, Threshold = None, Result = None, input_type_a = None, input_type_b = None, operation = None):
        inputs = AttrDict()
        inputs[0] = Geometry # NodeSocketGeometry
        inputs[1] = A0 # NodeSocketString
        inputs[2] = A1 # NodeSocketFloat
        inputs[3] = A2 # NodeSocketVector
        inputs[4] = A3 # NodeSocketColor
        inputs[5] = B0 # NodeSocketString
        inputs[6] = B1 # NodeSocketFloat
        inputs[7] = B2 # NodeSocketVector
        inputs[8] = B3 # NodeSocketColor
        inputs[9] = Threshold # NodeSocketFloat
        inputs[10] = Result # NodeSocketString
        input_props = AttrDict()
        input_props['input_type_a'] = input_type_a
        input_props['input_type_b'] = input_type_b
        input_props['operation'] = operation
        outputs = AttrDict()
        outputs['Geometry'] = ShaderVariableGeometry(self.parent)
        outputs['_mapping_'] = {
            0: 'Geometry',
        }
        self.parent.shader_program.append(ShaderOpRawNodeCall('GeometryNodeAttributeCompare', outputs, inputs, input_props))
        return outputs['Geometry']

    def GeometryNodeAttributeConvert(self, *, Geometry = None, Attribute = None, Result = None, data_type = None, domain = None):
        inputs = AttrDict()
        inputs[0] = Geometry # NodeSocketGeometry
        inputs[1] = Attribute # NodeSocketString
        inputs[2] = Result # NodeSocketString
        input_props = AttrDict()
        input_props['data_type'] = data_type
        input_props['domain'] = domain
        outputs = AttrDict()
        outputs['Geometry'] = ShaderVariableGeometry(self.parent)
        outputs['_mapping_'] = {
            0: 'Geometry',
        }
        self.parent.shader_program.append(ShaderOpRawNodeCall('GeometryNodeAttributeConvert', outputs, inputs, input_props))
        return outputs['Geometry']

    def GeometryNodeAttributeFill(self, *, Geometry = None, Attribute = None, Value0 = None, Value1 = None, Value2 = None, Value3 = None, Value4 = None, data_type = None, domain = None):
        inputs = AttrDict()
        inputs[0] = Geometry # NodeSocketGeometry
        inputs[1] = Attribute # NodeSocketString
        inputs[2] = Value0 # NodeSocketVector
        inputs[3] = Value1 # NodeSocketFloat
        inputs[4] = Value2 # NodeSocketColor
        inputs[5] = Value3 # NodeSocketBool
        inputs[6] = Value4 # NodeSocketInt
        input_props = AttrDict()
        input_props['data_type'] = data_type
        input_props['domain'] = domain
        outputs = AttrDict()
        outputs['Geometry'] = ShaderVariableGeometry(self.parent)
        outputs['_mapping_'] = {
            0: 'Geometry',
        }
        self.parent.shader_program.append(ShaderOpRawNodeCall('GeometryNodeAttributeFill', outputs, inputs, input_props))
        return outputs['Geometry']

    def GeometryNodeAttributeMapRange(self, *, Geometry = None, Attribute = None, Result = None, FromMin0 = None, FromMax0 = None, ToMin0 = None, ToMax0 = None, Steps0 = None, FromMin1 = None, FromMax1 = None, ToMin1 = None, ToMax1 = None, Steps1 = None, Clamp = None, data_type = None, interpolation_type = None):
        inputs = AttrDict()
        inputs[0] = Geometry # NodeSocketGeometry
        inputs[1] = Attribute # NodeSocketString
        inputs[2] = Result # NodeSocketString
        inputs[3] = FromMin0 # NodeSocketFloat
        inputs[4] = FromMax0 # NodeSocketFloat
        inputs[5] = ToMin0 # NodeSocketFloat
        inputs[6] = ToMax0 # NodeSocketFloat
        inputs[7] = Steps0 # NodeSocketFloat
        inputs[8] = FromMin1 # NodeSocketVector
        inputs[9] = FromMax1 # NodeSocketVector
        inputs[10] = ToMin1 # NodeSocketVector
        inputs[11] = ToMax1 # NodeSocketVector
        inputs[12] = Steps1 # NodeSocketVector
        inputs[13] = Clamp # NodeSocketBool
        input_props = AttrDict()
        input_props['data_type'] = data_type
        input_props['interpolation_type'] = interpolation_type
        outputs = AttrDict()
        outputs['Geometry'] = ShaderVariableGeometry(self.parent)
        outputs['_mapping_'] = {
            0: 'Geometry',
        }
        self.parent.shader_program.append(ShaderOpRawNodeCall('GeometryNodeAttributeMapRange', outputs, inputs, input_props))
        return outputs['Geometry']

    def GeometryNodeAttributeMath(self, *, Geometry = None, A0 = None, A1 = None, B0 = None, B1 = None, C0 = None, C1 = None, Result = None, input_type_a = None, input_type_b = None, input_type_c = None, operation = None):
        inputs = AttrDict()
        inputs[0] = Geometry # NodeSocketGeometry
        inputs[1] = A0 # NodeSocketString
        inputs[2] = A1 # NodeSocketFloat
        inputs[3] = B0 # NodeSocketString
        inputs[4] = B1 # NodeSocketFloat
        inputs[5] = C0 # NodeSocketString
        inputs[6] = C1 # NodeSocketFloat
        inputs[7] = Result # NodeSocketString
        input_props = AttrDict()
        input_props['input_type_a'] = input_type_a
        input_props['input_type_b'] = input_type_b
        input_props['input_type_c'] = input_type_c
        input_props['operation'] = operation
        outputs = AttrDict()
        outputs['Geometry'] = ShaderVariableGeometry(self.parent)
        outputs['_mapping_'] = {
            0: 'Geometry',
        }
        self.parent.shader_program.append(ShaderOpRawNodeCall('GeometryNodeAttributeMath', outputs, inputs, input_props))
        return outputs['Geometry']

    def GeometryNodeAttributeMix(self, *, Geometry = None, Factor0 = None, Factor1 = None, A0 = None, A1 = None, A2 = None, A3 = None, B0 = None, B1 = None, B2 = None, B3 = None, Result = None, blend_type = None, input_type_a = None, input_type_b = None, input_type_factor = None):
        inputs = AttrDict()
        inputs[0] = Geometry # NodeSocketGeometry
        inputs[1] = Factor0 # NodeSocketString
        inputs[2] = Factor1 # NodeSocketFloatFactor
        inputs[3] = A0 # NodeSocketString
        inputs[4] = A1 # NodeSocketFloat
        inputs[5] = A2 # NodeSocketVector
        inputs[6] = A3 # NodeSocketColor
        inputs[7] = B0 # NodeSocketString
        inputs[8] = B1 # NodeSocketFloat
        inputs[9] = B2 # NodeSocketVector
        inputs[10] = B3 # NodeSocketColor
        inputs[11] = Result # NodeSocketString
        input_props = AttrDict()
        input_props['blend_type'] = blend_type
        input_props['input_type_a'] = input_type_a
        input_props['input_type_b'] = input_type_b
        input_props['input_type_factor'] = input_type_factor
        outputs = AttrDict()
        outputs['Geometry'] = ShaderVariableGeometry(self.parent)
        outputs['_mapping_'] = {
            0: 'Geometry',
        }
        self.parent.shader_program.append(ShaderOpRawNodeCall('GeometryNodeAttributeMix', outputs, inputs, input_props))
        return outputs['Geometry']

    def GeometryNodeAttributeProximity(self, *, Geometry = None, Target = None, Distance = None, Position = None, target_geometry_element = None):
        inputs = AttrDict()
        inputs[0] = Geometry # NodeSocketGeometry
        inputs[1] = Target # NodeSocketGeometry
        inputs[2] = Distance # NodeSocketString
        inputs[3] = Position # NodeSocketString
        input_props = AttrDict()
        input_props['target_geometry_element'] = target_geometry_element
        outputs = AttrDict()
        outputs['Geometry'] = ShaderVariableGeometry(self.parent)
        outputs['_mapping_'] = {
            0: 'Geometry',
        }
        self.parent.shader_program.append(ShaderOpRawNodeCall('GeometryNodeAttributeProximity', outputs, inputs, input_props))
        return outputs['Geometry']

    def GeometryNodeAttributeRandomize(self, *, Geometry = None, Attribute = None, Min0 = None, Max0 = None, Min1 = None, Max1 = None, Min2 = None, Max2 = None, Seed = None, data_type = None, operation = None):
        inputs = AttrDict()
        inputs[0] = Geometry # NodeSocketGeometry
        inputs[1] = Attribute # NodeSocketString
        inputs[2] = Min0 # NodeSocketVector
        inputs[3] = Max0 # NodeSocketVector
        inputs[4] = Min1 # NodeSocketFloat
        inputs[5] = Max1 # NodeSocketFloat
        inputs[6] = Min2 # NodeSocketInt
        inputs[7] = Max2 # NodeSocketInt
        inputs[8] = Seed # NodeSocketInt
        input_props = AttrDict()
        input_props['data_type'] = data_type
        input_props['operation'] = operation
        outputs = AttrDict()
        outputs['Geometry'] = ShaderVariableGeometry(self.parent)
        outputs['_mapping_'] = {
            0: 'Geometry',
        }
        self.parent.shader_program.append(ShaderOpRawNodeCall('GeometryNodeAttributeRandomize', outputs, inputs, input_props))
        return outputs['Geometry']

    def GeometryNodeAttributeRemove(self, *, Geometry = None, Attribute = None):
        inputs = AttrDict()
        inputs[0] = Geometry # NodeSocketGeometry
        inputs[1] = Attribute # NodeSocketString
        input_props = AttrDict()
        outputs = AttrDict()
        outputs['Geometry'] = ShaderVariableGeometry(self.parent)
        outputs['_mapping_'] = {
            0: 'Geometry',
        }
        self.parent.shader_program.append(ShaderOpRawNodeCall('GeometryNodeAttributeRemove', outputs, inputs, input_props))
        return outputs['Geometry']

    def GeometryNodeAttributeSampleTexture(self, *, Geometry = None, Mapping = None, Result = None, texture = None):
        inputs = AttrDict()
        inputs[0] = Geometry # NodeSocketGeometry
        inputs[1] = Mapping # NodeSocketString
        inputs[2] = Result # NodeSocketString
        input_props = AttrDict()
        input_props['texture'] = texture
        outputs = AttrDict()
        outputs['Geometry'] = ShaderVariableGeometry(self.parent)
        outputs['_mapping_'] = {
            0: 'Geometry',
        }
        self.parent.shader_program.append(ShaderOpRawNodeCall('GeometryNodeAttributeSampleTexture', outputs, inputs, input_props))
        return outputs['Geometry']

    def GeometryNodeAttributeSeparateXYZ(self, *, Geometry = None, Vector0 = None, Vector1 = None, ResultX = None, ResultY = None, ResultZ = None, input_type = None):
        inputs = AttrDict()
        inputs[0] = Geometry # NodeSocketGeometry
        inputs[1] = Vector0 # NodeSocketString
        inputs[2] = Vector1 # NodeSocketVector
        inputs[3] = ResultX # NodeSocketString
        inputs[4] = ResultY # NodeSocketString
        inputs[5] = ResultZ # NodeSocketString
        input_props = AttrDict()
        input_props['input_type'] = input_type
        outputs = AttrDict()
        outputs['Geometry'] = ShaderVariableGeometry(self.parent)
        outputs['_mapping_'] = {
            0: 'Geometry',
        }
        self.parent.shader_program.append(ShaderOpRawNodeCall('GeometryNodeAttributeSeparateXYZ', outputs, inputs, input_props))
        return outputs['Geometry']

    def GeometryNodeAttributeTransfer(self, *, Geometry = None, SourceGeometry = None, Source = None, Destination = None, domain = None, mapping = None):
        inputs = AttrDict()
        inputs[0] = Geometry # NodeSocketGeometry
        inputs[1] = SourceGeometry # NodeSocketGeometry
        inputs[2] = Source # NodeSocketString
        inputs[3] = Destination # NodeSocketString
        input_props = AttrDict()
        input_props['domain'] = domain
        input_props['mapping'] = mapping
        outputs = AttrDict()
        outputs['Geometry'] = ShaderVariableGeometry(self.parent)
        outputs['_mapping_'] = {
            0: 'Geometry',
        }
        self.parent.shader_program.append(ShaderOpRawNodeCall('GeometryNodeAttributeTransfer', outputs, inputs, input_props))
        return outputs['Geometry']

    def GeometryNodeAttributeVectorMath(self, *, Geometry = None, A0 = None, A1 = None, B0 = None, B1 = None, B2 = None, C0 = None, C1 = None, C2 = None, Result = None, input_type_a = None, input_type_b = None, input_type_c = None, operation = None):
        inputs = AttrDict()
        inputs[0] = Geometry # NodeSocketGeometry
        inputs[1] = A0 # NodeSocketString
        inputs[2] = A1 # NodeSocketVector
        inputs[3] = B0 # NodeSocketString
        inputs[4] = B1 # NodeSocketVector
        inputs[5] = B2 # NodeSocketFloat
        inputs[6] = C0 # NodeSocketString
        inputs[7] = C1 # NodeSocketVector
        inputs[8] = C2 # NodeSocketFloat
        inputs[9] = Result # NodeSocketString
        input_props = AttrDict()
        input_props['input_type_a'] = input_type_a
        input_props['input_type_b'] = input_type_b
        input_props['input_type_c'] = input_type_c
        input_props['operation'] = operation
        outputs = AttrDict()
        outputs['Geometry'] = ShaderVariableGeometry(self.parent)
        outputs['_mapping_'] = {
            0: 'Geometry',
        }
        self.parent.shader_program.append(ShaderOpRawNodeCall('GeometryNodeAttributeVectorMath', outputs, inputs, input_props))
        return outputs['Geometry']

    def GeometryNodeBoolean(self, *, Geometry1 = None, Geometry2 = None, SelfIntersection = None, HoleTolerant = None, operation = None):
        inputs = AttrDict()
        inputs[0] = Geometry1 # NodeSocketGeometry
        inputs[1] = Geometry2 # NodeSocketGeometry
        inputs[2] = SelfIntersection # NodeSocketBool
        inputs[3] = HoleTolerant # NodeSocketBool
        input_props = AttrDict()
        input_props['operation'] = operation
        outputs = AttrDict()
        outputs['Geometry'] = ShaderVariableGeometry(self.parent)
        outputs['_mapping_'] = {
            0: 'Geometry',
        }
        self.parent.shader_program.append(ShaderOpRawNodeCall('GeometryNodeBoolean', outputs, inputs, input_props))
        return outputs['Geometry']

    def GeometryNodeBoundBox(self, *, Geometry = None):
        inputs = AttrDict()
        inputs[0] = Geometry # NodeSocketGeometry
        input_props = AttrDict()
        outputs = AttrDict()
        outputs['Mesh'] = ShaderVariableGeometry(self.parent)
        outputs['Min'] = ShaderVariableVector(self.parent)
        outputs['Max'] = ShaderVariableVector(self.parent)
        outputs['_mapping_'] = {
            0: 'Mesh',
            1: 'Min',
            2: 'Max',
        }
        self.parent.shader_program.append(ShaderOpRawNodeCall('GeometryNodeBoundBox', outputs, inputs, input_props))
        return outputs

    def GeometryNodeCollectionInfo(self, *, Collection = None, transform_space = None):
        inputs = AttrDict()
        inputs[0] = Collection # NodeSocketCollection
        input_props = AttrDict()
        input_props['transform_space'] = transform_space
        outputs = AttrDict()
        outputs['Geometry'] = ShaderVariableGeometry(self.parent)
        outputs['_mapping_'] = {
            0: 'Geometry',
        }
        self.parent.shader_program.append(ShaderOpRawNodeCall('GeometryNodeCollectionInfo', outputs, inputs, input_props))
        return outputs['Geometry']

    def GeometryNodeCurveToMesh(self, *, Curve = None, ProfileCurve = None):
        inputs = AttrDict()
        inputs[0] = Curve # NodeSocketGeometry
        inputs[1] = ProfileCurve # NodeSocketGeometry
        input_props = AttrDict()
        outputs = AttrDict()
        outputs['Mesh'] = ShaderVariableGeometry(self.parent)
        outputs['_mapping_'] = {
            0: 'Mesh',
        }
        self.parent.shader_program.append(ShaderOpRawNodeCall('GeometryNodeCurveToMesh', outputs, inputs, input_props))
        return outputs['Mesh']

    def GeometryNodeEdgeSplit(self, *, Geometry = None, EdgeAngle = None, Angle = None, SharpEdges = None):
        inputs = AttrDict()
        inputs[0] = Geometry # NodeSocketGeometry
        inputs[1] = EdgeAngle # NodeSocketBool
        inputs[2] = Angle # NodeSocketFloatAngle
        inputs[3] = SharpEdges # NodeSocketBool
        input_props = AttrDict()
        outputs = AttrDict()
        outputs['Geometry'] = ShaderVariableGeometry(self.parent)
        outputs['_mapping_'] = {
            0: 'Geometry',
        }
        self.parent.shader_program.append(ShaderOpRawNodeCall('GeometryNodeEdgeSplit', outputs, inputs, input_props))
        return outputs['Geometry']

    def GeometryNodeGroup(self, *, interface = None, node_tree = None):
        inputs = AttrDict()
        input_props = AttrDict()
        input_props['interface'] = interface
        input_props['node_tree'] = node_tree
        outputs = AttrDict()
        outputs['_mapping_'] = {
        }
        self.parent.shader_program.append(ShaderOpRawNodeCall('GeometryNodeGroup', outputs, inputs, input_props))
        return outputs

    def GeometryNodeIsViewport():
        inputs = AttrDict()
        input_props = AttrDict()
        outputs = AttrDict()
        outputs['IsViewport'] = ShaderVariableUnk(self.parent)
        outputs['_mapping_'] = {
            0: 'IsViewport',
        }
        self.parent.shader_program.append(ShaderOpRawNodeCall('GeometryNodeIsViewport', outputs, inputs, input_props))
        return outputs['IsViewport']

    def GeometryNodeJoinGeometry(self, *, Geometry = None):
        inputs = AttrDict()
        inputs[0] = Geometry # NodeSocketGeometry
        input_props = AttrDict()
        outputs = AttrDict()
        outputs['Geometry'] = ShaderVariableGeometry(self.parent)
        outputs['_mapping_'] = {
            0: 'Geometry',
        }
        self.parent.shader_program.append(ShaderOpRawNodeCall('GeometryNodeJoinGeometry', outputs, inputs, input_props))
        return outputs['Geometry']

    def GeometryNodeMeshCircle(self, *, Vertices = None, Radius = None, fill_type = None):
        inputs = AttrDict()
        inputs[0] = Vertices # NodeSocketInt
        inputs[1] = Radius # NodeSocketFloatDistance
        input_props = AttrDict()
        input_props['fill_type'] = fill_type
        outputs = AttrDict()
        outputs['Geometry'] = ShaderVariableGeometry(self.parent)
        outputs['_mapping_'] = {
            0: 'Geometry',
        }
        self.parent.shader_program.append(ShaderOpRawNodeCall('GeometryNodeMeshCircle', outputs, inputs, input_props))
        return outputs['Geometry']

    def GeometryNodeMeshCone(self, *, Vertices = None, RadiusTop = None, RadiusBottom = None, Depth = None, fill_type = None):
        inputs = AttrDict()
        inputs[0] = Vertices # NodeSocketInt
        inputs[1] = RadiusTop # NodeSocketFloatDistance
        inputs[2] = RadiusBottom # NodeSocketFloatDistance
        inputs[3] = Depth # NodeSocketFloatDistance
        input_props = AttrDict()
        input_props['fill_type'] = fill_type
        outputs = AttrDict()
        outputs['Geometry'] = ShaderVariableGeometry(self.parent)
        outputs['_mapping_'] = {
            0: 'Geometry',
        }
        self.parent.shader_program.append(ShaderOpRawNodeCall('GeometryNodeMeshCone', outputs, inputs, input_props))
        return outputs['Geometry']

    def GeometryNodeMeshCube(self, *, Size = None):
        inputs = AttrDict()
        inputs[0] = Size # NodeSocketFloatDistance
        input_props = AttrDict()
        outputs = AttrDict()
        outputs['Geometry'] = ShaderVariableGeometry(self.parent)
        outputs['_mapping_'] = {
            0: 'Geometry',
        }
        self.parent.shader_program.append(ShaderOpRawNodeCall('GeometryNodeMeshCube', outputs, inputs, input_props))
        return outputs['Geometry']

    def GeometryNodeMeshCylinder(self, *, Vertices = None, Radius = None, Depth = None, fill_type = None):
        inputs = AttrDict()
        inputs[0] = Vertices # NodeSocketInt
        inputs[1] = Radius # NodeSocketFloatDistance
        inputs[2] = Depth # NodeSocketFloatDistance
        input_props = AttrDict()
        input_props['fill_type'] = fill_type
        outputs = AttrDict()
        outputs['Geometry'] = ShaderVariableGeometry(self.parent)
        outputs['_mapping_'] = {
            0: 'Geometry',
        }
        self.parent.shader_program.append(ShaderOpRawNodeCall('GeometryNodeMeshCylinder', outputs, inputs, input_props))
        return outputs['Geometry']

    def GeometryNodeMeshGrid(self, *, SizeX = None, SizeY = None, VerticesX = None, VerticesY = None):
        inputs = AttrDict()
        inputs[0] = SizeX # NodeSocketFloatDistance
        inputs[1] = SizeY # NodeSocketFloatDistance
        inputs[2] = VerticesX # NodeSocketInt
        inputs[3] = VerticesY # NodeSocketInt
        input_props = AttrDict()
        outputs = AttrDict()
        outputs['Geometry'] = ShaderVariableGeometry(self.parent)
        outputs['_mapping_'] = {
            0: 'Geometry',
        }
        self.parent.shader_program.append(ShaderOpRawNodeCall('GeometryNodeMeshGrid', outputs, inputs, input_props))
        return outputs['Geometry']

    def GeometryNodeMeshIcoSphere(self, *, Radius = None, Subdivisions = None):
        inputs = AttrDict()
        inputs[0] = Radius # NodeSocketFloatDistance
        inputs[1] = Subdivisions # NodeSocketInt
        input_props = AttrDict()
        outputs = AttrDict()
        outputs['Geometry'] = ShaderVariableGeometry(self.parent)
        outputs['_mapping_'] = {
            0: 'Geometry',
        }
        self.parent.shader_program.append(ShaderOpRawNodeCall('GeometryNodeMeshIcoSphere', outputs, inputs, input_props))
        return outputs['Geometry']

    def GeometryNodeMeshLine(self, *, Count = None, Resolution = None, StartLocation = None, Offset = None, count_mode = None, mode = None):
        inputs = AttrDict()
        inputs[0] = Count # NodeSocketInt
        inputs[1] = Resolution # NodeSocketFloatDistance
        inputs[2] = StartLocation # NodeSocketVectorTranslation
        inputs[3] = Offset # NodeSocketVectorTranslation
        input_props = AttrDict()
        input_props['count_mode'] = count_mode
        input_props['mode'] = mode
        outputs = AttrDict()
        outputs['Geometry'] = ShaderVariableGeometry(self.parent)
        outputs['_mapping_'] = {
            0: 'Geometry',
        }
        self.parent.shader_program.append(ShaderOpRawNodeCall('GeometryNodeMeshLine', outputs, inputs, input_props))
        return outputs['Geometry']

    def GeometryNodeMeshUVSphere(self, *, Segments = None, Rings = None, Radius = None):
        inputs = AttrDict()
        inputs[0] = Segments # NodeSocketInt
        inputs[1] = Rings # NodeSocketInt
        inputs[2] = Radius # NodeSocketFloatDistance
        input_props = AttrDict()
        outputs = AttrDict()
        outputs['Geometry'] = ShaderVariableGeometry(self.parent)
        outputs['_mapping_'] = {
            0: 'Geometry',
        }
        self.parent.shader_program.append(ShaderOpRawNodeCall('GeometryNodeMeshUVSphere', outputs, inputs, input_props))
        return outputs['Geometry']

    def GeometryNodeObjectInfo(self, *, Object = None, transform_space = None):
        inputs = AttrDict()
        inputs[0] = Object # NodeSocketObject
        input_props = AttrDict()
        input_props['transform_space'] = transform_space
        outputs = AttrDict()
        outputs['Location'] = ShaderVariableVector(self.parent)
        outputs['Rotation'] = ShaderVariableVector(self.parent)
        outputs['Scale'] = ShaderVariableVector(self.parent)
        outputs['Geometry'] = ShaderVariableGeometry(self.parent)
        outputs['_mapping_'] = {
            0: 'Location',
            1: 'Rotation',
            2: 'Scale',
            3: 'Geometry',
        }
        self.parent.shader_program.append(ShaderOpRawNodeCall('GeometryNodeObjectInfo', outputs, inputs, input_props))
        return outputs

    def GeometryNodePointDistribute(self, *, Geometry = None, DistanceMin = None, DensityMax = None, DensityAttribute = None, Seed = None, distribute_method = None):
        inputs = AttrDict()
        inputs[0] = Geometry # NodeSocketGeometry
        inputs[1] = DistanceMin # NodeSocketFloatDistance
        inputs[2] = DensityMax # NodeSocketFloat
        inputs[3] = DensityAttribute # NodeSocketString
        inputs[4] = Seed # NodeSocketInt
        input_props = AttrDict()
        input_props['distribute_method'] = distribute_method
        outputs = AttrDict()
        outputs['Geometry'] = ShaderVariableGeometry(self.parent)
        outputs['_mapping_'] = {
            0: 'Geometry',
        }
        self.parent.shader_program.append(ShaderOpRawNodeCall('GeometryNodePointDistribute', outputs, inputs, input_props))
        return outputs['Geometry']

    def GeometryNodePointInstance(self, *, Geometry = None, Object = None, Collection = None, Seed = None, instance_type = None, use_whole_collection = None):
        inputs = AttrDict()
        inputs[0] = Geometry # NodeSocketGeometry
        inputs[1] = Object # NodeSocketObject
        inputs[2] = Collection # NodeSocketCollection
        inputs[3] = Seed # NodeSocketInt
        input_props = AttrDict()
        input_props['instance_type'] = instance_type
        input_props['use_whole_collection'] = use_whole_collection
        outputs = AttrDict()
        outputs['Geometry'] = ShaderVariableGeometry(self.parent)
        outputs['_mapping_'] = {
            0: 'Geometry',
        }
        self.parent.shader_program.append(ShaderOpRawNodeCall('GeometryNodePointInstance', outputs, inputs, input_props))
        return outputs['Geometry']

    def GeometryNodePointScale(self, *, Geometry = None, Factor0 = None, Factor1 = None, Factor2 = None, input_type = None):
        inputs = AttrDict()
        inputs[0] = Geometry # NodeSocketGeometry
        inputs[1] = Factor0 # NodeSocketString
        inputs[2] = Factor1 # NodeSocketVectorXYZ
        inputs[3] = Factor2 # NodeSocketFloat
        input_props = AttrDict()
        input_props['input_type'] = input_type
        outputs = AttrDict()
        outputs['Geometry'] = ShaderVariableGeometry(self.parent)
        outputs['_mapping_'] = {
            0: 'Geometry',
        }
        self.parent.shader_program.append(ShaderOpRawNodeCall('GeometryNodePointScale', outputs, inputs, input_props))
        return outputs['Geometry']

    def GeometryNodePointSeparate(self, *, Geometry = None, Mask = None):
        inputs = AttrDict()
        inputs[0] = Geometry # NodeSocketGeometry
        inputs[1] = Mask # NodeSocketString
        input_props = AttrDict()
        outputs = AttrDict()
        outputs['Geometry1'] = ShaderVariableGeometry(self.parent)
        outputs['Geometry2'] = ShaderVariableGeometry(self.parent)
        outputs['_mapping_'] = {
            0: 'Geometry1',
            1: 'Geometry2',
        }
        self.parent.shader_program.append(ShaderOpRawNodeCall('GeometryNodePointSeparate', outputs, inputs, input_props))
        return outputs

    def GeometryNodePointTranslate(self, *, Geometry = None, Translation0 = None, Translation1 = None, input_type = None):
        inputs = AttrDict()
        inputs[0] = Geometry # NodeSocketGeometry
        inputs[1] = Translation0 # NodeSocketString
        inputs[2] = Translation1 # NodeSocketVectorTranslation
        input_props = AttrDict()
        input_props['input_type'] = input_type
        outputs = AttrDict()
        outputs['Geometry'] = ShaderVariableGeometry(self.parent)
        outputs['_mapping_'] = {
            0: 'Geometry',
        }
        self.parent.shader_program.append(ShaderOpRawNodeCall('GeometryNodePointTranslate', outputs, inputs, input_props))
        return outputs['Geometry']

    def GeometryNodePointsToVolume(self, *, Geometry = None, Density = None, VoxelSize = None, VoxelAmount = None, Radius0 = None, Radius1 = None, input_type_radius = None, resolution_mode = None):
        inputs = AttrDict()
        inputs[0] = Geometry # NodeSocketGeometry
        inputs[1] = Density # NodeSocketFloat
        inputs[2] = VoxelSize # NodeSocketFloatDistance
        inputs[3] = VoxelAmount # NodeSocketFloat
        inputs[4] = Radius0 # NodeSocketString
        inputs[5] = Radius1 # NodeSocketFloat
        input_props = AttrDict()
        input_props['input_type_radius'] = input_type_radius
        input_props['resolution_mode'] = resolution_mode
        outputs = AttrDict()
        outputs['Geometry'] = ShaderVariableGeometry(self.parent)
        outputs['_mapping_'] = {
            0: 'Geometry',
        }
        self.parent.shader_program.append(ShaderOpRawNodeCall('GeometryNodePointsToVolume', outputs, inputs, input_props))
        return outputs['Geometry']

    def GeometryNodeRotatePoints(self, *, Geometry = None, Axis0 = None, Axis1 = None, Angle0 = None, Angle1 = None, Rotation0 = None, Rotation1 = None, input_type_angle = None, input_type_axis = None, input_type_rotation = None, space = None):
        inputs = AttrDict()
        inputs[0] = Geometry # NodeSocketGeometry
        inputs[1] = Axis0 # NodeSocketString
        inputs[2] = Axis1 # NodeSocketVectorXYZ
        inputs[3] = Angle0 # NodeSocketString
        inputs[4] = Angle1 # NodeSocketFloatAngle
        inputs[5] = Rotation0 # NodeSocketString
        inputs[6] = Rotation1 # NodeSocketVectorEuler
        input_props = AttrDict()
        input_props['input_type_angle'] = input_type_angle
        input_props['input_type_axis'] = input_type_axis
        input_props['input_type_rotation'] = input_type_rotation
        input_props['space'] = space
        outputs = AttrDict()
        outputs['Geometry'] = ShaderVariableGeometry(self.parent)
        outputs['_mapping_'] = {
            0: 'Geometry',
        }
        self.parent.shader_program.append(ShaderOpRawNodeCall('GeometryNodeRotatePoints', outputs, inputs, input_props))
        return outputs['Geometry']

    def GeometryNodeSubdivide(self, *, Geometry = None, Level = None):
        inputs = AttrDict()
        inputs[0] = Geometry # NodeSocketGeometry
        inputs[1] = Level # NodeSocketInt
        input_props = AttrDict()
        outputs = AttrDict()
        outputs['Geometry'] = ShaderVariableGeometry(self.parent)
        outputs['_mapping_'] = {
            0: 'Geometry',
        }
        self.parent.shader_program.append(ShaderOpRawNodeCall('GeometryNodeSubdivide', outputs, inputs, input_props))
        return outputs['Geometry']

    def GeometryNodeSubdivisionSurface(self, *, Geometry = None, Level = None, UseCreases = None, BoundarySmooth = None, SmoothUVs = None):
        inputs = AttrDict()
        inputs[0] = Geometry # NodeSocketGeometry
        inputs[1] = Level # NodeSocketInt
        inputs[2] = UseCreases # NodeSocketBool
        inputs[3] = BoundarySmooth # NodeSocketBool
        inputs[4] = SmoothUVs # NodeSocketBool
        input_props = AttrDict()
        outputs = AttrDict()
        outputs['Geometry'] = ShaderVariableGeometry(self.parent)
        outputs['_mapping_'] = {
            0: 'Geometry',
        }
        self.parent.shader_program.append(ShaderOpRawNodeCall('GeometryNodeSubdivisionSurface', outputs, inputs, input_props))
        return outputs['Geometry']

    def GeometryNodeSwitch(self, *, Switch = None, A0 = None, B0 = None, A1 = None, B1 = None, A2 = None, B2 = None, A3 = None, B3 = None, A4 = None, B4 = None, A5 = None, B5 = None, A6 = None, B6 = None, A7 = None, B7 = None, A8 = None, B8 = None, input_type = None):
        inputs = AttrDict()
        inputs[0] = Switch # NodeSocketBool
        inputs[1] = A0 # NodeSocketFloat
        inputs[2] = B0 # NodeSocketFloat
        inputs[3] = A1 # NodeSocketInt
        inputs[4] = B1 # NodeSocketInt
        inputs[5] = A2 # NodeSocketBool
        inputs[6] = B2 # NodeSocketBool
        inputs[7] = A3 # NodeSocketVector
        inputs[8] = B3 # NodeSocketVector
        inputs[9] = A4 # NodeSocketColor
        inputs[10] = B4 # NodeSocketColor
        inputs[11] = A5 # NodeSocketString
        inputs[12] = B5 # NodeSocketString
        inputs[13] = A6 # NodeSocketGeometry
        inputs[14] = B6 # NodeSocketGeometry
        inputs[15] = A7 # NodeSocketObject
        inputs[16] = B7 # NodeSocketObject
        inputs[17] = A8 # NodeSocketCollection
        inputs[18] = B8 # NodeSocketCollection
        input_props = AttrDict()
        input_props['input_type'] = input_type
        outputs = AttrDict()
        outputs['Output0'] = ShaderVariableFloat(self.parent)
        outputs['Output1'] = ShaderVariableUnk(self.parent)
        outputs['Output2'] = ShaderVariableUnk(self.parent)
        outputs['Output3'] = ShaderVariableVector(self.parent)
        outputs['Output4'] = ShaderVariableVector(self.parent)
        outputs['Output5'] = ShaderVariableUnk(self.parent)
        outputs['Output6'] = ShaderVariableGeometry(self.parent)
        outputs['Output7'] = ShaderVariableUnk(self.parent)
        outputs['Output8'] = ShaderVariableUnk(self.parent)
        outputs['_mapping_'] = {
            0: 'Output0',
            1: 'Output1',
            2: 'Output2',
            3: 'Output3',
            4: 'Output4',
            5: 'Output5',
            6: 'Output6',
            7: 'Output7',
            8: 'Output8',
        }
        self.parent.shader_program.append(ShaderOpRawNodeCall('GeometryNodeSwitch', outputs, inputs, input_props))
        return outputs

    def GeometryNodeTransform(self, *, Geometry = None, Translation = None, Rotation = None, Scale = None):
        inputs = AttrDict()
        inputs[0] = Geometry # NodeSocketGeometry
        inputs[1] = Translation # NodeSocketVectorTranslation
        inputs[2] = Rotation # NodeSocketVectorEuler
        inputs[3] = Scale # NodeSocketVectorXYZ
        input_props = AttrDict()
        outputs = AttrDict()
        outputs['Geometry'] = ShaderVariableGeometry(self.parent)
        outputs['_mapping_'] = {
            0: 'Geometry',
        }
        self.parent.shader_program.append(ShaderOpRawNodeCall('GeometryNodeTransform', outputs, inputs, input_props))
        return outputs['Geometry']

    def GeometryNodeTriangulate(self, *, Geometry = None, MinimumVertices = None, ngon_method = None, quad_method = None):
        inputs = AttrDict()
        inputs[0] = Geometry # NodeSocketGeometry
        inputs[1] = MinimumVertices # NodeSocketInt
        input_props = AttrDict()
        input_props['ngon_method'] = ngon_method
        input_props['quad_method'] = quad_method
        outputs = AttrDict()
        outputs['Geometry'] = ShaderVariableGeometry(self.parent)
        outputs['_mapping_'] = {
            0: 'Geometry',
        }
        self.parent.shader_program.append(ShaderOpRawNodeCall('GeometryNodeTriangulate', outputs, inputs, input_props))
        return outputs['Geometry']

    def GeometryNodeVolumeToMesh(self, *, Geometry = None, Density = None, VoxelSize = None, VoxelAmount = None, Threshold = None, Adaptivity = None, resolution_mode = None):
        inputs = AttrDict()
        inputs[0] = Geometry # NodeSocketGeometry
        inputs[1] = Density # NodeSocketString
        inputs[2] = VoxelSize # NodeSocketFloatDistance
        inputs[3] = VoxelAmount # NodeSocketFloat
        inputs[4] = Threshold # NodeSocketFloat
        inputs[5] = Adaptivity # NodeSocketFloatFactor
        input_props = AttrDict()
        input_props['resolution_mode'] = resolution_mode
        outputs = AttrDict()
        outputs['Geometry'] = ShaderVariableGeometry(self.parent)
        outputs['_mapping_'] = {
            0: 'Geometry',
        }
        self.parent.shader_program.append(ShaderOpRawNodeCall('GeometryNodeVolumeToMesh', outputs, inputs, input_props))
        return outputs['Geometry']

    def NodeFrame(self, *, label_size = None, shrink = None, text = None):
        inputs = AttrDict()
        input_props = AttrDict()
        input_props['label_size'] = label_size
        input_props['shrink'] = shrink
        input_props['text'] = text
        outputs = AttrDict()
        outputs['_mapping_'] = {
        }
        self.parent.shader_program.append(ShaderOpRawNodeCall('NodeFrame', outputs, inputs, input_props))
        return outputs

    def NodeGroupInput(self, *, interface = None):
        inputs = AttrDict()
        input_props = AttrDict()
        input_props['interface'] = interface
        outputs = AttrDict()
        outputs['Geometry'] = ShaderVariableGeometry(self.parent)
        outputs['unk'] = ShaderVariableUnk(self.parent)
        outputs['_mapping_'] = {
            0: 'Geometry',
            1: 'unk',
        }
        self.parent.shader_program.append(ShaderOpRawNodeCall('NodeGroupInput', outputs, inputs, input_props))
        return outputs

    def NodeGroupOutput(self, *, Geometry = None, unk = None, interface = None, is_active_output = None):
        inputs = AttrDict()
        inputs[0] = Geometry # NodeSocketGeometry
        inputs[1] = unk # NodeSocketVirtual
        input_props = AttrDict()
        input_props['interface'] = interface
        input_props['is_active_output'] = is_active_output
        outputs = AttrDict()
        outputs['_mapping_'] = {
        }
        self.parent.shader_program.append(ShaderOpRawNodeCall('NodeGroupOutput', outputs, inputs, input_props))
        return outputs

    def NodeReroute(self, *, Input = None):
        inputs = AttrDict()
        inputs[0] = Input # NodeSocketFloat
        input_props = AttrDict()
        outputs = AttrDict()
        outputs['Output'] = ShaderVariableFloat(self.parent)
        outputs['_mapping_'] = {
            0: 'Output',
        }
        self.parent.shader_program.append(ShaderOpRawNodeCall('NodeReroute', outputs, inputs, input_props))
        return outputs['Output']

    def ShaderNodeClamp(self, *, Value = None, Min = None, Max = None, clamp_type = None):
        inputs = AttrDict()
        inputs[0] = Value # NodeSocketFloat
        inputs[1] = Min # NodeSocketFloat
        inputs[2] = Max # NodeSocketFloat
        input_props = AttrDict()
        input_props['clamp_type'] = clamp_type
        outputs = AttrDict()
        outputs['Result'] = ShaderVariableFloat(self.parent)
        outputs['_mapping_'] = {
            0: 'Result',
        }
        self.parent.shader_program.append(ShaderOpRawNodeCall('ShaderNodeClamp', outputs, inputs, input_props))
        return outputs['Result']

    def ShaderNodeCombineRGB(self, *, R = None, G = None, B = None):
        inputs = AttrDict()
        inputs[0] = R # NodeSocketFloatUnsigned
        inputs[1] = G # NodeSocketFloatUnsigned
        inputs[2] = B # NodeSocketFloatUnsigned
        input_props = AttrDict()
        outputs = AttrDict()
        outputs['Image'] = ShaderVariableVector(self.parent)
        outputs['_mapping_'] = {
            0: 'Image',
        }
        self.parent.shader_program.append(ShaderOpRawNodeCall('ShaderNodeCombineRGB', outputs, inputs, input_props))
        return outputs['Image']

    def ShaderNodeCombineXYZ(self, *, X = None, Y = None, Z = None):
        inputs = AttrDict()
        inputs[0] = X # NodeSocketFloat
        inputs[1] = Y # NodeSocketFloat
        inputs[2] = Z # NodeSocketFloat
        input_props = AttrDict()
        outputs = AttrDict()
        outputs['Vector'] = ShaderVariableVector(self.parent)
        outputs['_mapping_'] = {
            0: 'Vector',
        }
        self.parent.shader_program.append(ShaderOpRawNodeCall('ShaderNodeCombineXYZ', outputs, inputs, input_props))
        return outputs['Vector']

    def ShaderNodeMapRange(self, *, Value = None, FromMin = None, FromMax = None, ToMin = None, ToMax = None, Steps = None, clamp = None, interpolation_type = None):
        inputs = AttrDict()
        inputs[0] = Value # NodeSocketFloat
        inputs[1] = FromMin # NodeSocketFloat
        inputs[2] = FromMax # NodeSocketFloat
        inputs[3] = ToMin # NodeSocketFloat
        inputs[4] = ToMax # NodeSocketFloat
        inputs[5] = Steps # NodeSocketFloat
        input_props = AttrDict()
        input_props['clamp'] = clamp
        input_props['interpolation_type'] = interpolation_type
        outputs = AttrDict()
        outputs['Result'] = ShaderVariableFloat(self.parent)
        outputs['_mapping_'] = {
            0: 'Result',
        }
        self.parent.shader_program.append(ShaderOpRawNodeCall('ShaderNodeMapRange', outputs, inputs, input_props))
        return outputs['Result']

    def ShaderNodeMath(self, *, Value0 = None, Value1 = None, Value2 = None, operation = None, use_clamp = None):
        inputs = AttrDict()
        inputs[0] = Value0 # NodeSocketFloat
        inputs[1] = Value1 # NodeSocketFloat
        inputs[2] = Value2 # NodeSocketFloat
        input_props = AttrDict()
        input_props['operation'] = operation
        input_props['use_clamp'] = use_clamp
        outputs = AttrDict()
        outputs['Value'] = ShaderVariableFloat(self.parent)
        outputs['_mapping_'] = {
            0: 'Value',
        }
        self.parent.shader_program.append(ShaderOpRawNodeCall('ShaderNodeMath', outputs, inputs, input_props))
        return outputs['Value']

    def ShaderNodeSeparateRGB(self, *, Image = None):
        inputs = AttrDict()
        inputs[0] = Image # NodeSocketColor
        input_props = AttrDict()
        outputs = AttrDict()
        outputs['R'] = ShaderVariableFloat(self.parent)
        outputs['G'] = ShaderVariableFloat(self.parent)
        outputs['B'] = ShaderVariableFloat(self.parent)
        outputs['_mapping_'] = {
            0: 'R',
            1: 'G',
            2: 'B',
        }
        self.parent.shader_program.append(ShaderOpRawNodeCall('ShaderNodeSeparateRGB', outputs, inputs, input_props))
        return outputs

    def ShaderNodeSeparateXYZ(self, *, Vector = None):
        inputs = AttrDict()
        inputs[0] = Vector # NodeSocketVector
        input_props = AttrDict()
        outputs = AttrDict()
        outputs['X'] = ShaderVariableFloat(self.parent)
        outputs['Y'] = ShaderVariableFloat(self.parent)
        outputs['Z'] = ShaderVariableFloat(self.parent)
        outputs['_mapping_'] = {
            0: 'X',
            1: 'Y',
            2: 'Z',
        }
        self.parent.shader_program.append(ShaderOpRawNodeCall('ShaderNodeSeparateXYZ', outputs, inputs, input_props))
        return outputs

    def ShaderNodeValToRGB(self, *, Fac = None, color_ramp = None):
        inputs = AttrDict()
        inputs[0] = Fac # NodeSocketFloatFactor
        input_props = AttrDict()
        input_props['color_ramp'] = color_ramp
        outputs = AttrDict()
        outputs['Color'] = ShaderVariableVector(self.parent)
        outputs['Alpha'] = ShaderVariableFloat(self.parent)
        outputs['_mapping_'] = {
            0: 'Color',
            1: 'Alpha',
        }
        self.parent.shader_program.append(ShaderOpRawNodeCall('ShaderNodeValToRGB', outputs, inputs, input_props))
        return outputs

    def ShaderNodeValue():
        inputs = AttrDict()
        input_props = AttrDict()
        outputs = AttrDict()
        outputs['Value'] = ShaderVariableFloat(self.parent)
        outputs['_mapping_'] = {
            0: 'Value',
        }
        self.parent.shader_program.append(ShaderOpRawNodeCall('ShaderNodeValue', outputs, inputs, input_props))
        return outputs['Value']

    def ShaderNodeVectorMath(self, *, Vector0 = None, Vector1 = None, Vector2 = None, Scale = None, operation = None):
        inputs = AttrDict()
        inputs[0] = Vector0 # NodeSocketVector
        inputs[1] = Vector1 # NodeSocketVector
        inputs[2] = Vector2 # NodeSocketVector
        inputs[3] = Scale # NodeSocketFloat
        input_props = AttrDict()
        input_props['operation'] = operation
        outputs = AttrDict()
        outputs['Vector'] = ShaderVariableVector(self.parent)
        outputs['Value'] = ShaderVariableFloat(self.parent)
        outputs['_mapping_'] = {
            0: 'Vector',
            1: 'Value',
        }
        self.parent.shader_program.append(ShaderOpRawNodeCall('ShaderNodeVectorMath', outputs, inputs, input_props))
        return outputs

    def ShaderNodeVectorRotate(self, *, Vector = None, Center = None, Axis = None, Angle = None, Rotation = None, invert = None, rotation_type = None):
        inputs = AttrDict()
        inputs[0] = Vector # NodeSocketVector
        inputs[1] = Center # NodeSocketVector
        inputs[2] = Axis # NodeSocketVector
        inputs[3] = Angle # NodeSocketFloatAngle
        inputs[4] = Rotation # NodeSocketVectorEuler
        input_props = AttrDict()
        input_props['invert'] = invert
        input_props['rotation_type'] = rotation_type
        outputs = AttrDict()
        outputs['Vector'] = ShaderVariableVector(self.parent)
        outputs['_mapping_'] = {
            0: 'Vector',
        }
        self.parent.shader_program.append(ShaderOpRawNodeCall('ShaderNodeVectorRotate', outputs, inputs, input_props))
        return outputs['Vector']

