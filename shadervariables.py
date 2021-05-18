from .shaderops import *
from .attrdict import AttrDict

class Attributes(AttrDict):
    def __init__(self,parent,geometry):
        self.parent = parent
        self.geometry = geometry
        self.position = self.Vector("position")
        self.__dict__['_init_complete_'] = True
        
    def add_item_callback(self,item,value):
        if not '_init_complete_' in self.__dict__:
            return
        if isinstance(value, Attribute):
            resgeo = self.parent.raw.GeometryNodeAttributeConvert(Geometry = self.geometry.clone(), Attribute = value.name, Result=item)
            self.geometry.name = resgeo.name

    def Float(self,name):
        return FloatAttribute(self.parent, self.geometry, name)

    def Vector(self,name):
        return VectorAttribute(self.parent, self.geometry, name)

class Attribute(object):
    def __init__(self,parent,geometry,name):
        self.parent = parent
        self.name = name
        self.geometry = geometry

    def attr_math_vector(self, other, operation):
        B0 = None
        B1 = None
        if isinstance(other, VectorAttribute):
            btype = "ATTRIBUTE"
            B0 = other.name
        elif isinstance(other, ShaderVariableVector):
            btype = "VECTOR"
            B1 = other
        else:
            print("unhandled operation : %s %s %s" % (type(self), operation, type(other)))
            raise TypeError('Invalid type')
        tmpName = self.parent.makeTempAttribute(self.geometry,"ATR")
        resGeo = self.parent.raw.GeometryNodeAttributeVectorMath(Geometry = self.geometry.clone(),A0 = self.name, B0 = B0, B1=B1, operation=operation, input_type_a = 'ATTRIBUTE', input_type_b = btype, Result=tmpName  )
        self.geometry.name = resGeo.name
        res = VectorAttribute(self.parent, self.geometry,tmpName)
        return res

    def attr_math_float(self, other, operation):
        B0 = None
        B1 = None 
        if isinstance(other, FloatAttribute):
            btype = "ATTRIBUTE"
            B0 = other.name
        elif isinstance(other, ShaderVariableFloat):
            btype = "FLOAT"
            B1 = other
        else:
            print("unhandled operation : %s %s %s" % (type(self), operation, type(other)))
            raise TypeError('Invalid type')
        tmpName = self.parent.makeTempAttribute(self.geometry, "ATR")
        resGeo = self.parent.raw.GeometryNodeAttributeMath(Geometry = self.geometry.clone(),A0 = self.name, B0 = B0, B1 = B1, operation=operation, input_type_a = 'ATTRIBUTE', input_type_b = btype, Result=tmpName  )
        self.geometry.name = resGeo.name
        res = FloatAttribute(self.parent, self.geometry,tmpName)
        return res        

    def attr_math(self,other,operation):
        if isinstance(other, (int, float)):
             if(isinstance(self, FloatAttribute)):
                 other = self.parent.Float(other)
             if(isinstance(self, VectorAttribute)):
                 other = self.parent.Vector(other,other,other)
        if isinstance(self, FloatAttribute) and isinstance(other, ShaderVariableVector):
            v1 = self.toVector()
            res = v1.attr_math(other, operation)
        if isinstance(self, ShaderVariableVector) and isinstance(other, FloatAttribute):
            other = other.toVector()
            res = self.attr_math(other, operation)
        if isinstance(self, VectorAttribute) and isinstance(other, FloatAttribute):
            other = other.toVector()
            res = self.attr_math(other, operation)            
        if isinstance(self, FloatAttribute) and isinstance(other, VectorAttribute):
            v1 = self.toVector()
            res = v1.attr_math(other, operation)            
        elif isinstance(self, VectorAttribute):
             res = self.attr_math_vector(other, operation)
        elif isinstance(self, FloatAttribute):
             res = self.attr_math_float(other, operation)
        else:
            raise TypeError('Unhandled Math operation')
        return res
    
    def attr_math_1(self,operation):
        if isinstance(self, FloatAttribute):
            tmpName = self.parent.makeTempAttribute(self.geometry, "ATR")
            resGeo = self.parent.raw.GeometryNodeAttributeMath(Geometry = self.geometry.clone(),A0 = self.name, operation=operation, input_type_a = 'ATTRIBUTE', Result=tmpName)
            self.geometry.name = resGeo.name
            res = FloatAttribute(self.parent, self.geometry,tmpName)
            return res        
        else:
            raise TypeError('Lazy didnt do this yet')

    def log(self,other):
        return self.attr_math(other,'LOGARITHM')

    def log2(self,other):
        return self.attr_math(2.0,'LOGARITHM')

    def sqrt(self):
        return self.attr_math_1('SQRT')

    def fract(self):
        return self.attr_math_1('FRACT')

    def __abs__(self):
        return self.attr_math_1('ABSOLUTE')

    def __gt__(self, other):
        return self.attr_math(other,'GREATER_THAN')

    def __add__(self, other):
        return self.attr_math(other,'ADD')

    def __radd__(self, other):
        return self.attr_math(other,'ADD')

    def __sub__(self, other):
        return self.attr_math(other,'SUBTRACT')

    def __rsub__(self, other):
        print("RSUB self = %s other = %s"% (self,other))
        #if then input is a pure float, make a shader var first
        if isinstance(other, (int,float)):
            other = self.parent.Float(other)
        #then fill it in as attribute
        if isinstance(other, ShaderVariableFloat):
            tmpName = self.parent.makeTempAttribute(self.geometry, "ATR")
            resGeo = self.parent.raw.GeometryNodeAttributeFill(Geometry=self.geometry.clone(), Attribute=tmpName, data_type='FLOAT', Value1=other)
            self.geometry.name = resGeo.name
            other = FloatAttribute(self.parent, self.geometry,tmpName)
        print("RSUB self = %s other = %s"% (self,other))
        return other.attr_math(self,'SUBTRACT')

    def __truediv__(self, other):
        return self.attr_math(other,'DIVIDE')

    def __mul__(self, other):
        return self.attr_math(other,'MULTIPLY')

    #def __rmul__(self, other):
    #    return self.attr_math(other,'MULTIPLY')


class FloatAttribute(Attribute):
    def __init__(self,parent,geometry,name):
        self.parent = parent
        self.name = name
        self.geometry = geometry

    def toVector(self):
        tmpName = self.parent.makeTempAttribute(self.geometry,"ATR")
        resGeo = self.parent.raw.GeometryNodeAttributeCombineXYZ(
            Geometry = self.geometry.clone(), 
            X0 = self.name,
            Y0 = self.name, 
            Z0 = self.name, 
            Result=tmpName, 
            input_type_x="ATTRIBUTE",
            input_type_y="ATTRIBUTE",
            input_type_z="ATTRIBUTE",
        )
        self.geometry.name = resGeo.name
        return VectorAttribute(self.parent, self.geometry,tmpName)


class VectorAttribute(Attribute):
    def __init__(self,parent,geometry,name=None):
        self.parent = parent
        self.geometry = geometry
        self.split = None
        if name == None:
            self.name = parent.makeTempAttribute(self.geometry, "avec")
        else:
            self.name = name

    def split_to_floats(self):
        if self.split is None:
            tmpNameX = self.parent.makeTempAttribute(self.geometry,"ATR_X")
            tmpNameY = self.parent.makeTempAttribute(self.geometry,"ATR_Y")
            tmpNameZ = self.parent.makeTempAttribute(self.geometry,"ATR_Z")
            resGeo = self.parent.raw.GeometryNodeAttributeSeparateXYZ(Geometry = self.geometry.clone(), Vector0 = self.name, input_type='ATTRIBUTE' , ResultX = tmpNameX, ResultY = tmpNameY, ResultZ = tmpNameZ )
            resX = FloatAttribute(self.parent, self.geometry,tmpNameX)
            resY = FloatAttribute(self.parent, self.geometry,tmpNameY)
            resZ = FloatAttribute(self.parent, self.geometry,tmpNameZ)
            self.split = [ resX, resY, resZ ]
            self.geometry.name = resGeo.name
    
    def get_x(self):
        self.split_to_floats()
        return self.split[0]
    def get_y(self):
        self.split_to_floats()
        return self.split[1]
    def get_z(self):
        self.split_to_floats()
        return self.split[2]

    def set_x(self, x):
        self.split_to_floats()
        X0 = None
        X1 = None
        if isinstance(x, (int, float)):
            X1 = x
            xtype = 'FLOAT'
        elif isinstance(x, FloatAttribute):
            X0 = x.name
            xtype = 'ATTRIBUTE'
        else:
            raise TypeError("Invalid Type")
        resGeo = self.parent.raw.GeometryNodeAttributeCombineXYZ(
            Geometry = self.geometry.clone(), 
            X0 = X0,
            X1 = X1,
            Y0 = self.split[1].name, 
            Z0 = self.split[2].name, 
            Result=self.name, 
            input_type_x=xtype,
            input_type_y="ATTRIBUTE",
            input_type_z="ATTRIBUTE",
        )
        self.split = None
        self.geometry.name = resGeo.name

    def set_y(self, y):
        self.split_to_floats()
        Y0 = None
        Y1 = None
        if isinstance(y, (int, float)):
            Y1 = y
            ytype = 'FLOAT'
        elif isinstance(y, FloatAttribute):
            Y0 = y.name
            ytype = 'ATTRIBUTE'
        else:
            raise TypeError("Invalid Type")
        resGeo = self.parent.raw.GeometryNodeAttributeCombineXYZ(
            Geometry = self.geometry.clone(), 
            X0 = self.split[0].name, 
            Y0 = Y0, 
            Y1 = Y1, 
            Z0 = self.split[2].name, 
            Result=self.name, 
            input_type_x="ATTRIBUTE",
            input_type_y=ytype,
            input_type_z="ATTRIBUTE",
        )
        self.split = None
        self.geometry.name = resGeo.name
    
    def set_z(self, z):
        self.split_to_floats()
        Z0 = None
        Z1 = None
        if isinstance(z, (int, float)):
            Z1 = z
            ztype = 'FLOAT'
        elif isinstance(z, FloatAttribute):
            Z0 = z.name
            ztype = 'ATTRIBUTE'
        else:
            raise TypeError("Invalid Type")
        resGeo = self.parent.raw.GeometryNodeAttributeCombineXYZ(
            Geometry = self.geometry.clone(), 
            X0 = self.split[0].name, 
            Y0 = self.split[1].name, 
            Z0 = Z0, 
            Z1 = Z1, 
            Result=self.name, 
            input_type_x="ATTRIBUTE",
            input_type_y="ATTRIBUTE",
            input_type_z=ztype,
        )
        self.split = None
        self.geometry.name = resGeo.name


    x = property(get_x, set_x)
    y = property(get_y, set_y)
    z = property(get_z, set_z)

class ShaderVariable:
    def __init__(self):
        pass

    def __repr__(self):
        newDict = dict()
        for (key, value) in self.__dict__.items():
            if key != '__parent__':
                newDict[key] = value
        return "{}({!r})".format(self.__class__.__name__, newDict)

class ShaderVariableUnk(ShaderVariable):
    def __init__(self,parent, name=None):
        self.__parent__ = parent
        if name == None:
            self.name = "unk_" + str(parent.var_id)
            parent.var_id +=1
        else:
            self.name = name


class ShaderVariableVector(ShaderVariable):
    def __init__(self,parent, name=None):
        self.__parent__ = parent
        if name == None:
            self.name = self.__parent__.makeTempName("vec")
        else:
            self.name = name

    def math2(self,other,operation):
        print("VECTOR MATH %s %s %s" % (self, operation, other))
        if isinstance(other, (int,float)):
            other = self.__parent__.Vector(other,other,other)
        if isinstance(other, (ShaderVariableFloat)):
            other = self.__parent__.Vector(other,other,other)
        if isinstance(other, ShaderVariableVector):
            res = self.__parent__.raw.ShaderNodeVectorMath(Vector0 = self, Vector1 = other, operation=operation)
            return res.Vector
        raise TypeError('Invalid type')

    def __add__(self, other):
        return self.math2(other,'ADD')

    def __radd__(self, other):
        if isinstance(other, (int,float)):
            other = self.__parent__.Vector(other,other,other)
            return other.math2(self,'ADD')
        raise TypeError('Invalid type')

    def __rsub__(self, other):
        if isinstance(other, (int,float)):
            other = self.__parent__.Vector(other,other,other)
            return other.math2(self,'SUBTRACT')
        raise TypeError('Invalid type')

    def __sub__(self, other):
        return self.math2(other,'SUBTRACT')

    def __mul__(self, other):
        print("Vector Mult: %s x %s" % (self, other))
        return self.math2(other,'MULTIPLY')

    def __rmul__(self, other):
        if isinstance(other, (int,float)):
            other = self.__parent__.Vector(other,other,other)
            return other * self
        raise TypeError('Invalid type')

    def __truediv__(self, other):
        return self.math2(other,'DIVIDE')

    def __rtruediv__(self, other):
        if isinstance(other, (int,float, ShaderVariableFloat)):
            other = self.__parent__.Vector(other,other,other)
            return other / self
        raise TypeError('Invalid type')

class ShaderVariableInt(ShaderVariable):
    def __init__(self,parent, name=None):
        self.__parent__ = parent
        if name == None:
            self.name = "int_" + str(parent.var_id)
            parent.var_id +=1
        else:
            self.name = name

class ShaderVariableFloat(ShaderVariable):
    def __init__(self,parent, name=None):
        self.__parent__ = parent
        if name == None:
            self.name = "flt_" + str(parent.var_id)
            parent.var_id +=1
        else:
            self.name = name
    
    def math2(self,other,operation):
        if isinstance(other, (int,float)):
            other = self.__parent__.Float(other)
        if isinstance(other, ShaderVariableVector):
            vself = self.__parent__.Vector(self, self, self)
            return vself.math2(other, operation)
        if isinstance(other, ShaderVariableFloat):
            res = ShaderVariableFloat(self.__parent__)
            self.__parent__.raw.ShaderNodeMath(Value0 = self, Value1 = other, operation=operation)
            return res
        raise TypeError('Invalid type')
    
    def __add__(self, other):
        return self.math2(other,'ADD')

    def __sub__(self, other):
        return self.math2(other,'SUBTRACT')

    def __mul__(self, other):
        return self.math2(other,'MULTIPLY')

    def __truediv__(self, other):
        return self.math2(other,'DIVIDE')

    def __radd__(self, other):
        if isinstance(other, (int,float)):
            other = self.__parent__.Float(other)
            return other.math2(self,'ADD')
        raise TypeError('Invalid type')

    def __rsub__(self, other):
        if isinstance(other, (int,float)):
            other = self.__parent__.Float(other)
            return other.math2(self,'SUBTRACT')
        raise TypeError('Invalid type')

    def __rmul__(self, other):
        if isinstance(other, (int,float)):
            other = self.__parent__.Float(other)
            return other.math2(self,'MULTIPLY')
        raise TypeError('Invalid type')

    def __rtruediv__(self, other):
        if isinstance(other, (int,float)):
            other = self.__parent__.Float(other)
            return other.math2(self,'DIVIDE')
        raise TypeError('Invalid type')


class ShaderVariableGeometry(ShaderVariable):
    def __init__(self,parent, name=None):
        self.__parent__ = parent
        self.attributes = Attributes(parent, self)
        if name == None:
            self.name = "geo_" + str(parent.var_id)
            parent.var_id +=1
        else:
            self.name = name

    def cleanattributes(self, geooverride = None):
        print("Cleaning outputs for %s" % (self))
        attr_list = [ ]
        search = geooverride
        if search is None:
            search = self 
        for (geo,name) in self.__parent__.temp_attr:
            if geo == search:
                print("marking %s for removal" % (name))
                attr_list.append(name)
        if len(attr_list) > 0:
            res = ShaderVariableGeometry(self.__parent__)
            self.__parent__.shader_program.append(ShaderOpAttributeRemove(res.name, self.clone(), attr_list))
            self.name = res.name
        return self

    def clone(self):
        return ShaderVariableGeometry(self.__parent__, self.name)

    def join(self, other):
        res = ShaderVariableGeometry(self.__parent__)
        self.__parent__.shader_program.append(ShaderOpJoin(res.name, [self, other]))
        return res

    def __mul__(self, other):
         if isinstance(other, (int, float)):
             res = ShaderVariableGeometry(self.__parent__)
             self.__parent__.shader_program.append(ShaderOpScaleGeometryConst(res.name, self.name, other))
             return res
         raise TypeError('Invalid type')    
    
    def __add__(self, other):
         if isinstance(other, ShaderVariableVector):
             res = ShaderVariableGeometry(self.__parent__)
             self.__parent__.shader_program.append(ShaderOpTranslateGeometry(res.name, self.name, other))
             return res
         raise TypeError('Invalid type')             