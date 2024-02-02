import tkinter as tk
import math
import time
from vector2 import *
from basis2 import *
from screen import *
from renderer import *
from matrix2 import *
from matrix3 import *

canvas: tk.Canvas = None
root: tk.Tk = None
width: int = 800
height: int = 600
deg: int = 0

def init():    
    global root, canvas, width, height
    
    root = tk.Tk() # GUI 생성 
    root.title("GameEngine Example")
    root.geometry("1100x800")

    canvas = tk.Canvas(root, width=width, height=height)
    canvas.pack()
    
def draw():
    
    global root, canvas, width, height, deg
    
    canvas.delete('all')
    
    basis = Basis2()
    screen = Screen()
    screen.SetInfo(Vector2(50, 0), Vector2(0, -50), Vector2(width * 0.5, height * 0.5))
    
    grid = Renderer(basis, screen)    
    grid.draw_grid(canvas, 10, 10)
    
    v0 = Vector2(0, 0)
    v1 = Vector2(math.cos(math.pi/4), math.sin(math.pi/4))
    #grid.draw_line(canvas, v0, v1)   
    
    
    basis2 = Basis2()
    grid2 = Renderer(basis2, screen)
    
    # basis 축 회전
    rad = deg / 180 * math.pi
    matRot = Matrix2(
                    math.cos(rad), -math.sin(rad), 
                    math.sin(rad), math.cos(rad)
                )    
    matScale = Matrix2(
                    1, 0, 
                    0, 1
                )
    matFinal = matRot * matScale
    basis2.axis1 = matFinal * basis2.axis1
    basis2.axis2 = matFinal * basis2.axis2
    
    
    # 벡터 자체 회전
    matTrans = Matrix3()
    matTrans.set_translation(0, 0)
    
    matRot2 = Matrix3()
    matRot2.set_rotaition(90)
    
    v0 = matTrans * matRot2 * v0
    v1 = matTrans * matRot2 * v1
        
    
    #basis2.SetInfo(Vector2(math.cos(rad),math.sin(rad)), Vector2(-math.sin(rad), math.cos(rad)))
    grid2.draw_grid(canvas, 10, 10)
    grid2.draw_line(canvas, v0, v1)
    
    deg += 5    
    root.after(100, draw)
    
    
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
