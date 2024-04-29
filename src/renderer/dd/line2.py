from tkinter import Canvas
from ..gameobject import GameObject
from .vector2 import Vector2

class Line2(GameObject):
    
    def __init__(self, canvas: Canvas, p0: Vector2, p1: Vector2, fill="gray", width=1, dash=()) -> None:
        self.start = p0
        self.end = p1
        
        item = canvas.create_line(self.start.x, self.start.y, self.end.x, self.end.y, fill=fill, width=width, dash=dash)        
        super(Line2, self).__init__(canvas, item)