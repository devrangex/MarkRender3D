from vector2 import *

class Basis2:
    
    def __init__(self, axis1: Vector2 = Vector2(1, 0), axis2: Vector2 = Vector2(0, 1)) -> None:
        self.axis1: Vector2 = axis1
        self.axis2: Vector2 = axis2
        
    def SetInfo(self, axis1: Vector2 = Vector2(1, 0), axis2: Vector2 = Vector2(0, 1)) -> None:
        self.axis1: Vector2 = axis1
        self.axis2: Vector2 = axis2
        
    def Transform(self, input: Vector2) -> Vector2:
        return Vector2(
            input.x * self.axis1.x + input.y * self.axis2.x,
            input.x * self.axis1.y + input.y * self.axis2.y
        )
        
    def __mul__(self, input: Vector2) -> Vector2:
        return self.Transform(input)