import math

class Vector3:
    def __init__(self, tx: float, ty: float, tz:float, tw: float = 1) -> None:
        self.x: float = tx
        self.y: float = ty
        self.z: float = tz
        self.w: float = tw
        
    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, scalar: int):
        return Vector3(self.x * scalar, self.y * scalar, self.z * scalar)
    
    def dot(self, right):
        return self.x * right.x + self.y * right.y + self.z * right.z
    
    def cross(self, right):
        return Vector3(
            self.y * right.z - self.z * right.y,
            self.z * right.x - self.x * right.z,
            self.x * right.y - self.y * right.x
        )
        
    def magnitude(self):
        return (self.x * self.x + self.y * self.y * self.z * self.z) ** 0.5
    
    @staticmethod
    def distance(a, b):
        # is this sqrt?
        return ((a.x - b.x) ** 2 + (a.y - b.y) ** 2 + (a.z - b.z) ** 2) ** 0.5
    
    @staticmethod
    def lerp(begin, end, ratio):
        ratio = min(1, max(0, ratio))
        return Vector3(begin.x + ((end.x - begin.x) * ratio), begin.y + ((end.y - begin.y) * ratio), begin.z + ((end.z - begin.z) * ratio))
    
Vector3.zero = Vector3(0, 0, 0)
Vector3.one = Vector3(1, 1, 1)
Vector3.right = Vector3(1, 0, 0)
Vector3.up = Vector3(0, 1, 0)
Vector3.forward = Vector3(0, 0, 1)

        