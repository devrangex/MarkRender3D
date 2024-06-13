import math
import numpy as np

class Vector3:
    def __init__(self, x: float = 0, y: float = 0, z:float = 0, w: float = 1) -> None:
        self.pos = np.array([x, y, z, w])
        
    @property
    def x(self):
        return self.pos[0]
    
    @property
    def y(self):
        return self.pos[1]
    
    @property
    def z(self):
        return self.pos[2]
    
    @property
    def w(self):
        return self.pos[3]
        
    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)    
    
    def __mul__(self, rhs):
        if isinstance(rhs, Vector3):
            #내적
            return self.dot(rhs)
        else:
            #상수배
            return Vector3(self.x * rhs, self.y * rhs, self.z * rhs)
    
    def __rmul__(self, rhs):
        return self.dot(rhs)
    
    def dot(self, rhs):
        return self.x * rhs.x + self.y * rhs.y + self.z * rhs.z
    
    def cross(self, rhs):
        return Vector3(
            self.y * rhs.z - self.z * rhs.y,
            self.z * rhs.x - self.x * rhs.z,
            self.x * rhs.y - self.y * rhs.x
        )
        
    def magnitude(self):
        return (self.x * self.x + self.y * self.y + self.z * self.z) ** 0.5
    
    def normalized(self):
        magnitude = self.magnitude()
        self.pos[0] /= magnitude
        self.pos[1] /= magnitude
        self.pos[2] /= magnitude
    
    @staticmethod
    def distance(lhs, rhs):        
        # is this sqrt?
        return ((lhs.x - rhs.x) ** 2 + (lhs.y - rhs.y) ** 2 + (lhs.z - rhs.z) ** 2) ** 0.5
    
    @staticmethod
    def lerp(begin, end, ratio):
        ratio = min(1, max(0, ratio))
        return Vector3(begin.x + ((end.x - begin.x) * ratio), begin.y + ((end.y - begin.y) * ratio), begin.z + ((end.z - begin.z) * ratio))
    
Vector3.zero = Vector3(0, 0, 0)
Vector3.one = Vector3(1, 1, 1)
Vector3.right = Vector3(1, 0, 0)
Vector3.up = Vector3(0, 1, 0)
Vector3.forward = Vector3(0, 0, 1)

        