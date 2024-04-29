import tkinter as tk

class GameObject:
    
    def __init__(self, canvas: tk.Canvas, item: int) -> None:
        self.canvas = canvas
        self.item = item
        
    def get_position(self):
        return self.canvas.coords(self.item)

    def move(self, x, y):
        self.canvas.move(self.item, x, y)

    def delete(self):
        self.canvas.delete(self.item)