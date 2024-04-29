from tkinter import Canvas

from .vector2 import Vector2
from ..gameobject import GameObject
from .line2 import Line2
from .matrix2 import Matrix2

class Grid2:
    
    def __init__(self, canvas: Canvas, h, v) -> None:
        self.canvas = canvas
        self.lines = {}
        
        self.basis = Matrix2(20, 0, 
                             0, -20)
        
        self.horizontal = h
        self.vertical = v
        
        begin = int(self.horizontal * 0.5)
        for i in range(self.horizontal):
            p0 = Vector2(begin, 0) + Vector2(0, -self.vertical * 0.5)
            p1 = Vector2(begin, 0) + Vector2(0, self.vertical * 0.5)
            
            #p0 = self.basis * p0
            #p1 = self.basis * p1
            
            line = Line2(canvas, p0, p1)
            self.lines[line.item] = line
            
            begin += 1
            
        begin = int(-self.vertical * 0.5)
        for i in range(self.vertical):
            p0 = Vector2(0, begin) + Vector2(-self.horizontal * 0.5, 0)
            p1 = Vector2(0, begin) + Vector2(self.horizontal * 0.5, 0)
            
            #p0 = self.basis * p0 + Vector2(200, 200)
            #p1 = self.basis * p1 + Vector2(200, 200)            
            
            line = Line2(canvas, p0, p1)
            self.lines[line.item] = line
            
            begin += 1
            
    def update(self):
        
        # 3d -> screen
        basis = Matrix2(20, 0, 
                        0, -20)        
        # move origin
        origin = Vector2(200, 200)
        
        for line in self.lines:
            
            # 누적되면 안대고 첨에 저장된 값을 지속적으로 수정해줘야 한답니다.
            coords = self.canvas.coords(line)
            p0 = Vector2(coords[0], coords[1])
            p1 = Vector2(coords[2], coords[3])
            
            p0 = self.basis * p0 + Vector2(200, 200)
            p1 = self.basis * p1 + Vector2(200, 200)
            
            self.canvas.coords(line, p0.x, p0.y, p1.x, p1.y)
            