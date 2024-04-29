from vector2 import Vector2

class Screen:
    
    def __init__(self, axis1: Vector2 = Vector2(20, 0), axis2: Vector2 = Vector2(0, 20), origin: Vector2 = Vector2(0, 0)) -> None:
        self.axis1 = axis1
        self.axis2 = axis2
        self.origin = origin
        
    def SetInfo(self, axis1: Vector2, axis2: Vector2, origin: Vector2) -> None:
        self.axis1 = axis1
        self.axis2 = axis2
        self.origin = origin
        
    def Transform(self, input: Vector2) -> Vector2:
        return Vector2(
            input.x * self.axis1.x + input.y * self.axis2.x + self.origin.x,
            input.x * self.axis1.y + input.y * self.axis2.y + self.origin.y
        )
        
    def __mul__(self, input: Vector2) -> Vector2:
        return self.Transform(input)
        