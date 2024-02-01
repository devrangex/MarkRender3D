import math

class Vector2:
    def __init__(self, tx: float, ty: float) -> None:
        self.x: float = tx
        self.y: float = ty
        
    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar: int):
        return Vector2(self.x * scalar, self.y * scalar)
    
    @staticmethod
    def distance(a, b):
        # is this sqrt?
        return ((a.x - b.x) ** 2 + (a.y - b.y) ** 2) ** 0.5
    
    @staticmethod
    def lerp(begin, end, ratio):
        ratio = min(1, max(0, ratio))
        return begin.x + ((end.x - begin.x) * ratio)
    
Vector2.zero = Vector2(0, 0)
Vector2.one = Vector2(1, 1)
Vector2.right = Vector2(1, 0)
Vector2.up = Vector2(0, 1)

        