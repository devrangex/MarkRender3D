class Vector2:
    
    def __init__(self, tx: float, ty: float) -> None:
        self.x: float = tx
        self.y: float = ty
        
    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)
        