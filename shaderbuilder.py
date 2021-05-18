
from .shaderops import * 
from .shadervariables import * 
from .rawcalls import RawCalls
from .attrdict import AttrDict
from pprint import pprint
import math as pymath

class Primitives:
    def __init__(self,parent):
        self.parent = parent
    
    def grid(self, SizeX = None, SizeY = None, VerticesX = None, VerticesY = None):
        res = self.parent.raw.GeometryNodeMeshGrid(SizeX = SizeX, SizeY = SizeY, VerticesX = VerticesX, VerticesY = VerticesY)
        return res.clone()

class math:
    def __init__(self,parent):
        self.parent = parent

    def sqrt(self, value):
        if isinstance(value, FloatAttribute):
            return value.sqrt()
        else:
            print("unhandled %s" % (type(value)))

    def shadermath_float_1(self, a, operation):
        res = self.parent.raw.ShaderNodeMath(Value0 = a, operation=operation)
        return res

    def shadermath_vector_1(self, a, operation):
        res = self.parent.raw.ShaderNodeVectorMath(Vector0 = a, operation=operation)
        return res.Vector

    def attributemath_float_1(self, a, operation):
        tmpName = self.parent.makeTempAttribute(a.geometry, "ATR")
        res = self.parent.raw.GeometryNodeAttributeMath(Geometry=a.geometry.clone(), A0 = a.name, input_type_a='ATTRIBUTE', operation=operation, Result=tmpName)
        a.geometry.name = res.name
        return FloatAttribute(self.parent, a.geometry, tmpName)
        
    def attributemath_vector_1(self, a, operation):
        tmpName = self.parent.makeTempAttribute(a.geometry, "ATR")
        res = self.parent.raw.GeometryNodeAttributeVectorMath(Geometry=a.geometry.clone(), A0 = a.name, input_type_a='ATTRIBUTE', operation=operation, Result=tmpName)
        a.geometry.name = res.name
        return FloatAttribute(self.parent, a.geometry, tmpName)

    def math_1(self, a, operation):
        if (isinstance(a, ShaderVariableFloat)):
            return self.shadermath_float_1(a, operation)
        if (isinstance(a, ShaderVariableVector)):
            return self.shadermath_vector_1(a, operation)
        if (isinstance(a, FloatAttribute)):
            return self.attributemath_float_1(a, operation)
        if (isinstance(a, VectorAttribute)):
            return self.attributemath_vector_1(a, operation)
        raise NotImplementedError()


    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

    def sin(self,a):
        if (isinstance(a, (int,float))):
            return pymath.sin(a)
        return self.math_1(a, 'SINE')

    def cos(self, a):
        if (isinstance(a, (int,float))):
            return pymath.cos(a)
        return self.math_1(a, 'COSINE')

    def tan(self, a):
        if (isinstance(a, (int,float))):
            return pymath.tan(a)
        return self.math_1(a, 'TANGENT')


class ShaderBuilder:
    def __init__(self):
        self.shader_program = []
        self.temp_attr = [ ]
        self.inputs = {} 
        self.outputs = {} 
        self.var_id = 1
        self.primitives = Primitives(self)
        self.raw = RawCalls(self)
        self.math = math(self)
        self.vector_cache = { }

    def RegisterTempAttribute(self, geometry, name):
        self.temp_attr.append((geometry,name))

    def makeTempAttribute(self,geometry, prefix = 'tmp'):
        name = self.makeTempName(prefix)
        self.RegisterTempAttribute(geometry, name)
        return name

    def makeTempName(self,prefix = 'tmp'):
        res = prefix + '_' + str(self.var_id)
        self.var_id +=1
        return res 

    def join(self, geometries):
        res = ShaderVariableGeometry(self)
        self.shader_program.append(ShaderOpJoin(res.name, geometries))
        return res

    def Input(self, name, sockettype, default_value=None):
         res = None
         if sockettype == "geometry":
             res=ShaderVariableGeometry(self,name)
         elif sockettype == "vector":
             res=ShaderVariableVector(self,name)
         elif sockettype == "float":
             res=ShaderVariableFloat(self,name)             
         elif sockettype == "int":
             res=ShaderVariableInt(self,name)             
         else: 
             raise TypeError("Unknown type")
         self.shader_program.append(ShaderOpCreateInput(name,sockettype,default_value))
         return res

    def Output(self, name, value):
        if isinstance(value, (float,int)):
            value = self.Float(value)
        if isinstance(value, ShaderVariableGeometry):
            self.shader_program.append(ShaderOpCreateOutput(name, value.clone().cleanattributes(value)))
        elif isinstance(value, ShaderVariable):
            self.shader_program.append(ShaderOpCreateOutput(name, value))
        else:
            raise TypeError("Cannot put this type for output")

    def Vector(self, x, y, z):
        key = (x, y, z)
        if key in self.vector_cache:
            return self.vector_cache[key]
        name = self.makeTempName("vec")
        self.shader_program.append(ShaderOpCreateVector(name, x,y,z))
        res = ShaderVariableVector(self, name)
        self.vector_cache[key] = res
        return res

    def Float(self, value):
        name = self.makeTempName("flt")
        self.shader_program.append(ShaderOpCreateFloat(name, value))
        return ShaderVariableFloat(self, name)

    def Switch(self, select, a, b):
        # todo type check and handle the 'other' cases
        name = self.makeTempAttribute(select.geometry,"ATR")
        resgeo = self.raw.GeometryNodeAttributeMix(
            Geometry = select.geometry.clone(), 
            Factor = select.name, 
            A0 = a.name, 
            B0 = b.name, 
            input_type_a = 'ATTRIBUTE', 
            input_type_b = 'ATTRIBUTE',
            input_type_c = 'ATTRIBUTE', 
            Result=name
        )
        select.Geometry=resgeo
        if(isinstance(a, FloatAttribute)):
            return FloatAttribute(self, select.geometry, name )
        else:
            return VectorAttribute(self, select.geometry, name )
   
    def PrintProgram(self):
        print("----[Program Start]-----")
        for inst in self.shader_program: 
            pprint(inst)
        print("----[Program End]-----")
