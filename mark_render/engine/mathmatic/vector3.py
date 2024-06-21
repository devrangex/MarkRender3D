import numpy as np

class Vector3:
    def __init__(self, x: float = 0, y: float = 0, z:float = 0, w: float = 1) -> None:
        self.__pos = np.array([x, y, z, w])
        
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
    def z(self):
        return self.__pos[2]
    
    @z.setter
    def z(self, v):
        self.__pos[2] = v
    
    @property
    def w(self):        
        return self.__pos[3]
    
    @w.setter
    def w(self, v):
        self.__pos[3] = v
        
    # addition
    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)    
    
    def __mul__(self, rhs):
        # 내적
        if isinstance(rhs, Vector3):            
            return self.dot(rhs)
        #상수배
        elif isinstance(rhs, float) or isinstance(rhs, int):
            return Vector3(self.x * rhs, self.y * rhs, self.z * rhs)
        else:
            raise TypeError("Unsupported multiplication type")
    
    def __rmul__(self, lhs):
        # 내적
        if isinstance(lhs, Vector3):            
            return self.dot(lhs)
        #상수배
        elif isinstance(lhs, float) or isinstance(lhs, int):
            return Vector3(self.x * lhs, self.y * lhs, self.z * lhs)
        else:
            raise TypeError("Unsupported multiplication type")
    
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

        