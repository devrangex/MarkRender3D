from mathmatic.vector2 import Vector2

class ScreenCoordinator:
    def __init__(self, axis1: Vector2, axis2: Vector2, origin: Vector2) -> None:        
        self.axis1 = axis1
        self.axis2 = axis2
        self.origin = origin
        
    def trasnform(self, input) -> Vector2:
        t0 = self.axis1 * input.x
        t1 = self.axis2 * input.y
        return Vector2(t0.x + t1.x + self.origin.x * 0.5, t0.y + t1.y + self.origin.y * 0.5)
        