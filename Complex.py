import math

class Complex:
    
    def __init__(self, real, imaginary = 0):
        if type(real) is complex:
            if imaginary == 0:
                self.real = real.real
                self.imaginary = real.imag
            else:
                raise ValueError(f"unexpected initialization value(s). If the initialization variable 'real' is of type 'complex', the initialization variable 'imaginary' should be omitted.\ntype of 'real': {type(real).__name__}\n'imaginary': {imaginary}")
        elif (not isinstance(real, (int, float))) or (not isinstance(imaginary, (int, float))):
            raise TypeError(f"invalid initialization type(s). Only 'int', 'float', and 'complex' is supported for Complex() initialization.\nreal: '{type(real).__name__}'\nimaginary: '{type(imaginary).__name__}'")
        else:
            self.real = real
            self.imaginary = imaginary
        self.argument = math.atan2(self.imaginary, self.real)
    
    def __abs__(self):
        return math.sqrt((self.real ** 2) + (self.imaginary ** 2))
    
    def __str__(self):
        if self.imaginary == 0:
            return str(self.real)
        elif self.imaginary < 0:
            if self.real != 0:
                if self.imaginary == -1:
                    return f"{self.real} - i"
                else:
                    return f"{self.real} - {abs(self.imaginary)}i"
            else:
                if self.imaginary == -1:
                    return "-i"
                else:
                    return f"-{abs(self.imaginary)}i"
        else:
            if self.real != 0:
                if self.imaginary == 1:
                    return f"{self.real} + i"
                else:
                    return f"{self.real} + {self.imaginary}i"
            else:
                if self.imaginary == 1:
                    return "i"
                else:
                    return f"{self.imaginary}i"
    
    def __repr__(self):
        return f"Complex({self.real}, {self.imaginary})"
    
    def __neg__(self):
        return Complex(-self.real, -self.imaginary)
    
    def __add__(self, other):
        if isinstance(other, (int, float, complex)):
            other = Complex(other)
        if type(other) is Complex:
            return Complex(self.real + other.real, self.imaginary + other.imaginary)
        else:
            raise TypeError(f"unsupported operand type(s) for +: 'Complex' and '{type(other).__name__}'")
    
    def __radd__(self, other):
        return self + other
    
    def __sub__(self, other):
        if isinstance(other, (int, float, complex)):
            other = Complex(other)
        if type(other) is Complex:
            return Complex(self.real - other.real, self.imaginary - other.imaginary)
        else:
            raise TypeError(f"unsupported operand type(s) for -: 'Complex' and '{type(other).__name__}'")
    
    def __rsub__(self, other):
        return other + (-self)
    
    def __mul__(self, other):
        if isinstance(other, (int, float, complex)):
            other = Complex(other)
        if type(other) is Complex:
            return Complex((self.real * other.real) - (self.imaginary * other.imaginary), (self.real * other.imaginary) + (self.imaginary * other.real))
        else:
            raise TypeError(f"unsupported operand type(s) for *: 'Complex' and '{type(other).__name__}'")
    
    def __rmul__(self, other):
        return self * other
    
    def __truediv__(self, other):
        if isinstance(other, (int, float, complex)):
            other = Complex(other)
        if type(other) is Complex:
            return Complex(((self.real * other.real) + (self.imaginary * other.imaginary)) / (other.real ** 2 + other.imaginary ** 2), ((self.imaginary * other.real) - (self.real * other.imaginary)) / (other.real ** 2 + other.imaginary ** 2))
        else:
            raise TypeError(f"unsupported operand type(s) for /: 'Complex' and '{type(other).__name__}'")

    def __rtruediv__(self, other):
        if isinstance(other, (int, float, complex)):
            other_number = Complex(other)
        else:
            raise TypeError(f"unsupported operand type(s) for /: 'Complex' and '{type(other).__name__}'")
        return other_number / self
    
    def __floordiv__(self, other):
        if isinstance(other, (int, float, complex)):
            other = Complex(other)
        if type(other) is Complex:
            return math.floor(Complex(((self.real * other.real) + (self.imaginary * other.imaginary)) / (other.real ** 2 + other.imaginary ** 2), ((self.imaginary * other.real) - (self.real * other.imaginary)) / (other.real ** 2 + other.imaginary ** 2)))
        else:
            raise TypeError(f"unsupported operand type(s) for //: 'Complex' and '{type(other).__name__}'")
    
    def __rfloordiv__(self, other):
        if isinstance(other, (int, float, complex)):
            other_number = Complex(other)
        else:
            raise TypeError(f"unsupported operand type(s) for /: 'Complex' and '{type(other).__name__}'")
        return other_number // self
    
    def __mod__(self, other):
        if isinstance(other, (int, float, complex)):
            other = Complex(other)
        if type(other) is Complex:
            quotiant = (self // other) * other
            return self - quotiant
        else:
            raise TypeError(f"unsupported operand type(s) for %: 'Complex' and '{type(other).__name__}'")

    def __rmod__(self, other):
        if isinstance(other, (int, float, complex)):
            other = Complex(other)
        else:
            raise TypeError(f"unsupported operand type(s) for /: 'Complex' and '{type(other).__name__}'")
        return other % self
    
    def __divmod__(self, other):
        if isinstance(other, (int, float, complex)):
            other = Complex(other)
        if type(other) is Complex:
            return (self // other, self % other)
        else:
            raise TypeError(f"unsupported operand type(s) for divmod(): 'Complex' and '{type(other).__name__}'")

    def __rdivmod__(self, other):
        if isinstance(other, (int, float, complex)):
            other = Complex(other)
        else:
            raise TypeError(f"unsupported operand type(s) for divmod(): 'Complex' and '{type(other).__name__}'")
        return divmod(other, self)

    def __pow__(self, other):
        if isinstance(other, (int, float, complex)):
            other = Complex(other)
        elif type(other) is Complex:
            return (abs(self) ** other.real) * (Complex(math.cos(math.log(abs(self)) * other.imaginary), math.sin(math.log(abs(self)) * other.imaginary))) * Complex(math.cos(self.argument * other.real), math.sin(self.argument * other.real)) / math.exp(self.argument * other.imaginary)
        else:
            raise TypeError(f"unsupported operand type(s) for ** or pow(): 'Complex' and '{type(other).__name__}'")
    
    def __rpow__(self, other):
        if isinstance(other, (int, float, complex)):
            other = Complex(other)
        else:
            raise TypeError(f"unsupported operand type(s) for ** or pow(): 'Complex' and '{type(other).__name__}'")
        return other ** self
    
    def log(self, base=math.e):
        if type(base) is not Complex:
            return Complex(math.log(abs(self)), self.argument) / math.log(base)
        else:
            return Complex(math.log(abs(self)), self.argument) / Complex(math.log(abs(base)), base.argument)
    
    def __eq__(self, other):
        if type(other) is Complex:  
            if (abs(self.real - other.real) < 0.00000001) and (abs(self.imaginary - other.imaginary) < 0.00000001):
                return True
            else:
                return False
        elif type(other) is complex:
            if (abs(self.real - other.real) < 0.00000001) and (abs(self.imaginary - other.imag) < 0.00000001):
                return True
            else:
                return False
        elif isinstance(other, (int, float)):
            if abs(self.imaginary) < 0.00000001:
                if abs(self.real - other) < 0.00000001:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def exp(self):
        return math.e ** self
    
    def sin(self):
        return Complex(math.sin(self.real) * math.cosh(self.imaginary), math.cos(self.real) * math.sinh(self.imaginary))
    
    def cos(self):
        return Complex(math.cos(self.real) * math.cosh(self.imaginary), -1 * math.sin(self.real) * math.sinh(self.imaginary))
    
    def tan(self):
        return self.sin() / self.cos()
    
    def sinh(self):
        return Complex(math.sinh(self.real) * math.cos(self.imaginary), math.cosh(self.real) * math.sin(self.imaginary))
    
    def cosh(self):
        return Complex(math.cosh(self.real) * math.cos(self.imaginary), math.sinh(self.real) * math.sin(self.imaginary))
    
    def tanh(self):
        return self.sinh() / self.cosh()
    
    def sqrt(self):
        return self ** 0.5
    
    def __floor__(self):
        return Complex(math.floor(self.real), math.floor(self.imaginary))
    
    def __ceil__(self):
        return Complex(math.ceil(self.real), math.ceil(self.imaginary))
    
    def __round__(self, ndigits = None):
        return Complex(round(self.real, ndigits), round(self.imaginary, ndigits))
    
    def __trunc__(self):
        return Complex(math.trunc(self.real), math.trunc(self.imaginary))
    
    def __int__(self):
        if (abs(self.imaginary) < 0.00000001):
            return int(self.real)
        else:
            raise ValueError(f"value of 'imaginary' attribute is non-zero. Unable to cast to 'int'\n'imaginary' = {self.imaginary}")
    
    def __float__(self):
        if (abs(self.imaginary) < 0.00000001):
            return float(self.real)
        else:
            raise ValueError(f"value of 'imaginary' attribute is non-zero. Unable to cast to 'float'\n'imaginary' = {self.imaginary}")

    def __complex__(self):
        return complex(self.real, self.imaginary)
