from vector2 import *
from basis2 import *
from screen import *

class Renderer:
    
    def __init__(self, basis: Basis2, screen: Screen) -> None:
        self.basis: Basis2 = basis        
        self.screen: Screen = screen
        
    def draw_grid(self, canvas, numH: int, numV: int) -> None:
        h_begin = int(-numH * 0.5 - 0.5)
        for i in range(numH+1):
            v0 = Vector2(h_begin, 0) + Vector2(0, -numV * 0.5)
            v1 = Vector2(h_begin, 0) + Vector2(0, numV * 0.5)
            
            v0 = self.basis * v0
            v1 = self.basis * v1
            
            v0 = self.screen * v0
            v1 = self.screen * v1
            
            canvas.create_line(v0.x, v0.y, v1.x, v1.y, fill="gray", width=1, dash=(4,2))
            
            h_begin += 1
            
        v_begin = int(-numV * 0.5 - 0.5)
        for i in range(numV+1):
            v0 = Vector2(0, v_begin) + Vector2(-numH / 2, 0)
            v1 = Vector2(0, v_begin) + Vector2(numH / 2, 0)
            
            v0 = (self.basis * v0)
            v1 = (self.basis * v1)
            
            v0 = self.screen * v0
            v1 = self.screen * v1
            
            canvas.create_line(v0.x, v0.y, v1.x, v1.y, fill="gray", width=1, dash=(4,2))
            
            v_begin += 1
            
    def draw_line(self, canvas, v0: Vector2, v1: Vector2) -> None:
        v0 = (self.basis * v0)
        v1 = (self.basis * v1)
        
        v0 = self.screen * v0
        v1 = self.screen * v1
        
        canvas.create_line(v0.x, v0.y, v1.x, v1.y, fill="gray", width=2)