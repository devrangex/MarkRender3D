import tkinter as tk
import math
from vector2 import *
from basis2 import *
from screen import *
from renderer import *

canvas: tk.Canvas = None
root: tk.Tk = None
width: int = 800
height: int = 600

def init():    
    global root, canvas, width, height
    
    root = tk.Tk() # GUI 생성 
    root.title("GameEngine Example")
    root.geometry("1100x800")

    canvas = tk.Canvas(root, width=width, height=height)
    canvas.pack()
    
def draw():
    
    global root, canvas, width, height
    
    basis = Basis2()
    screen = Screen()
    screen.SetInfo(Vector2(50, 0), Vector2(0, -50), Vector2(width * 0.5, height * 0.5))
    
    grid = Renderer(basis, screen)    
    grid.draw_grid(canvas, 10, 10)
    
    grid2 = Renderer(Basis2(Vector2(math.cos(math.pi / 4),math.sin(math.pi / 4)), Vector2(-math.sin(math.pi / 4), math.cos(math.pi / 4))), screen)
    grid2.draw_grid(canvas, 10, 10)
    
    v0 = Vector2(0, 0)
    v1 = Vector2(1, 0)
    grid.draw_line(canvas, v0, v1)   
    grid2.draw_line(canvas, v0, v1)   
    
    
def draw_edge():
    
    global root, canvas, width, height
    
    #canvas.create_line(0, 0, width, height, fill="black", width=1)
    #canvas.create_line(0, height, width, 0, fill="black", width=1)
    
    canvas.create_line(2, 0, 2, height, fill="black", width=1)
    canvas.create_line(0, 2, width, 2, fill="black", width=1)
    canvas.create_line(width - 2, 0, width - 2, height, fill="black", width=1)
    canvas.create_line(0, height - 2, width, height - 2, fill="black", width=1)

    #canvas.create_line(0, 0, 400, 0, fill="black", width=3)


def main():
    
    init()
    
    draw_edge()
    
    draw()

    root.mainloop() # GUI가 보이고 종료될때까지 실행함
    
if __name__ == "__main__":
    main()
