from .vector2 import Vector2
from .matrix3 import Matrix3

class Screen:
    
    def __init__(self, canvas, realWidth, realHeight, screenWidth, screenHeight) -> None:
        self.canvas = canvas
        self.realWidth = realWidth
        self.realHeight = realHeight
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        
        #self.
        
        self.transform = Matrix3( 
                                1, 0, realWidth * 0.5,
                                0, 1, realHeight * 0.5,
                                0, 0, 1 
                            )
        
        gap = 10
        w = int(self.width / gap)
        h = int(self.height /gap)
        for i in range(w):
            self.canvas.create_line(i * gap, 0, i * gap, self.height, fill="gray", width=1, dash=(2,2))
            
        for i in range(h):
            self.canvas.create_line(0, i * gap, self.width, i * gap, fill="gray", width=1, dash=(2,2))
            
        self.canvas.create_line(0, self.height / 2, self.width, self.height / 2, fill="blue", width=1)
        self.canvas.create_line(self.width / 2, 0, self.width / 2, self.height, fill="red", width=1)
        
        
        pos = Vector2(2, 3)
        pos = self.transform * pos
        self.canvas.create_rectangle(pos.x, pos.y, pos.x + gap, pos.y + 10, fill="black")

    def update():
        pass
    
    def draw():
        pass
        
    def Transform(self, input: Vector2) -> Vector2:
        return self.transform * input
        
    def __mul__(self, input: Vector2) -> Vector2:
        return self.Transform(input)
        