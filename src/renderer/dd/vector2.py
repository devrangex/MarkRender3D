import math
import numpy as np

class Vector2:
    
    def __init__(self, x: float = 0, y: float = 0, w: float = 1) -> None:        
        self.pos = np.array([x, y, w])        
        
    @property
    def x(self):
        return self.pos[0]
    
    @property
    def y(self):
        return self.pos[1]
    
    @property
    def w(self):
        return self.pos[2]        
    
    def __add__(self, other):        
        return Vector2(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)    
    
    def __mul__(self, scalar):
        return Vector2(self.x * scalar, self.y * scalar)
    
    @staticmethod
    def distance(a, b):        
        return ((a.x - b.x) ** 2 + (a.y - b.y) ** 2) ** 0.5
    
    @staticmethod
    def lerp(begin, end, ratio):
        ratio = min(1, max(0, ratio))
        return Vector2(begin.x + ((end.x - begin.x) * ratio), begin.y + ((end.y - begin.y) * ratio))
    
Vector2.zero = Vector2(0, 0)
Vector2.one = Vector2(1, 1)
Vector2.right = Vector2(1, 0)
Vector2.up = Vector2(0, 1)
