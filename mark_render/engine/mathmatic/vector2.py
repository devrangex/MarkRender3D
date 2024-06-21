import math
import numpy as np

class Vector2:
    
    def __init__(self, x: float = 0, y: float = 0, w: float = 1) -> None:        
        self.__pos = np.array([x, y, w])        
        
    @property
    def x(self):
        return self.__pos[0]
    
    @x.setter
    def x(self, v):
        self.__pos[0] = v
    
    @property
    def y(self):
        return self.__pos[1]
    
    @y.setter
    def y(self, v):
        self.__pos[1] = v
    
    @property
    def w(self):        
        return self.__pos[2]        
    
    @w.setter
    def w(self, v):
        self.__pos[2] = v    
    
    # addition two vectors.
    def __add__(self, rhs):        
        return Vector2(self.x + rhs.x, self.y + rhs.y)
    
    # subtraction two vectors.
    def __sub__(self, rhs):
        return Vector2(self.x - rhs.x, self.y - rhs.y)
    
    # scalar multiplication.
    def __mul__(self, rhs):
        if isinstance(rhs, Vector2):
            return self.dot(rhs)
        elif isinstance(rhs, float) or isinstance(rhs, int):
            return Vector2(self.x * rhs, self.y * rhs)
        else:
            raise TypeError("Unsupported multiplication type")
        
    def __rmul__(self, lhs):
        # 내적
        if isinstance(lhs, Vector2):
            return self.dot(lhs)
        #상수배
        elif isinstance(lhs, float) or isinstance(lhs, int):
            return Vector2(self.x*lhs, self.y*lhs)
        else:
            raise TypeError("Unsupported multiplication type")
    
    # dot product
    def dot(self, rhs):
        return self.x * rhs.x + self.y * rhs.y
    
    # magnitude
    def magnitude(self):
        return (self.x*self.x + self.y*self.y)**0.5
    
    # magnitude squared
    def magnitude_squared(self):
        return (self.x*self.x + self.y*self.y)
    
    # normalize
    def normalize(self):
        magnitude = self.magnitude()
        return Vector2(self.x/magnitude, self.y/magnitude)
    
    # normalized
    def normalized(self):
        magnitude = self.magnitude()
        self.x /= magnitude
        self.y /= magnitude
        self.z /= magnitude
    
    @staticmethod
    def distance(a, b):        
        return ((a.x - b.x)**2 + (a.y - b.y)**2)**0.5
    
    @staticmethod
    def distance_squared(a, b):        
        return (a.x - b.x)**2 + (a.y - b.y)**2
    
    @staticmethod
    def lerp(begin, end, ratio):
        ratio = min(1, max(0, ratio))
        return Vector2(begin.x + ((end.x - begin.x)*ratio), begin.y + ((end.y - begin.y)*ratio))
    
Vector2.zero = Vector2(0, 0)
Vector2.one = Vector2(1, 1)
Vector2.right = Vector2(1, 0)
Vector2.up = Vector2(0, 1)
