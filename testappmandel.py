import math

class Complex:
    def __init__(self, real,imag):
        self.real = real
        self.imag = imag
    
    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)
    
    def __mul__(self, other):
        return Complex(self.real * other.real - self.imag * other.imag, self.imag * other.real + self.real * other.imag)

    def __abs__(self):
        new = (self.real*self.real) + (self.imag*self.imag)
        return math.sqrt(new)

def select(cond, val_true, val_false):
    vt = cond * val_true
    vf = (1.0-cond) * val_false
    return vt+vf



z = Complex(0.0, 0.0)
c = Complex(-2.5, -2.5)
itr = 3
escape_iter = 0
for x in range(itr):
    nz = z*z + c
    print("%s: %s,%s -> %s" % (x,z.real,z.imag, abs(nz)))
    escaped = abs(nz) > 2.0
    z = Complex(
            select(escaped, z.real, nz.real),
            select(escaped, z.imag, nz.imag)
        )
    escape_iter = select(escaped, escape_iter , x)

