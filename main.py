import tkinter as tk
import math
import time
from vector2 import *
from basis2 import *
from screen import *
from renderer import *
from matrix2 import *
from matrix3 import *
from polygon import *
from cube import *
from plane import *
from camera import *
from sphere import *

canvas: tk.Canvas = None
root: tk.Tk = None
mainFrame: tk.Frame = None
width: int = 800
height: int = 600
deg: int = 0

def init():    
    global root, canvas, width, height
    
    root = tk.Tk() # GUI 생성 
    root.title("GameEngine Example")
    root.geometry("1100x800")
    mainFrame = tk.Frame(root)    

    canvas = tk.Canvas(root, width=width, height=height)
    canvas.pack()   
    
    
def draw():
    
    global root, canvas, width, height, deg
    
    canvas.delete('all')
    
    basis = Basis2()
    screen = Screen()
    screen.SetInfo(Vector2(50, 0), Vector2(0, -50), Vector2(width * 0.5, height * 0.5))
    
    grid = Renderer(basis, screen, canvas)    
    grid.draw_grid(10, 10)
    
    v0 = Vector2(0, 0)
    v1 = Vector2(math.cos(math.pi/4), math.sin(math.pi/4))
    #grid.draw_line(canvas, v0, v1)   
    
    
    basis2 = Basis2()
    grid2 = Renderer(basis2, screen, canvas)
    
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
    grid2.draw_grid(10, 10)
    grid2.draw_line(v0, v1)
    
    deg += 5    
    root.after(100, draw)
    
def draw_polygon():
    
    draw_edge()
    
    global root, canvas, width, height, deg
    
    canvas.delete('all')
    
    basis = Basis2()
    screen = Screen()
    screen.SetInfo(Vector2(20, 0), Vector2(0, -20), Vector2(width * 0.5, height * 0.5))    
    renderer = Renderer(basis, screen, canvas)    
    renderer.draw_grid(40, 40)
    
    matRotY = Matrix4()
    matRotY.set_rotaitionY(deg)
    
    matRotX = Matrix4()
    matRotX.set_rotaitionZ(deg)
    
    matTrans = Matrix4()
    matTrans.set_translation(5, 5, 0)
    
    polygon = Polygon()
    polygon.set_index_buffer()
    polygon.set_vertex_buffer()
    
    #polygon.transform(matRotY * matRotX)
    polygon.transform(matTrans * matRotX)
    polygon.render(renderer)
    
    deg += 5
    root.after(100, draw_polygon)
    
def draw_cube():
    
    global root, canvas, width, height, deg
    
    canvas.delete('all')
    
    draw_edge()
    
    basis = Basis2()
    screen = Screen()
    screen.SetInfo(Vector2(1, 0), Vector2(0, -1), Vector2(width * 0.5, height * 0.5))    
    
    camera = Camera()
    camera.set_projection(5.5, 5000, 60, width, height)
    camera.set_position(Vector3(0, 50, 50))
    camera.look_at(Vector3(0, 0, 0))
    
    renderer = Renderer(basis, screen, canvas, camera, width, height)    

    #renderer.draw_grid(40, 40)
    
    matRotY = Matrix4()
    matRotY.set_rotaitionY(deg)
    
    matRotX = Matrix4()
    matRotX.set_rotaitionZ(deg)
    
    matTrans = Matrix4()
    matTrans.set_translation((deg+1)*0.5, (deg+1)*0.5, (deg+1)*0.5)
    matTrans.set_identity()
    
    #matProj = Matrix4()
    #matProj.set_projection(5.5, 5000, 60, width, height)
    #matViewProj = camera.get_projection_matrix()
    
    cube = Cube()
    cube.set_index_buffer()
    cube.set_vertex_buffer()
    
    sphere = Sphere()
    sphere.set_geometry()
    
    plane = Plane()
    plane.set_vertex_buffer()
    plane.set_index_buffer()
    
    matScale = Matrix4()
    matScale._11 = 800
    matScale._22 = 600
    matScale._33 = 1
    matScale._44 = 1
    
    #polygon.transform(matRotY * matRotX)
    cube.transform(matTrans * matRotY)
    cube.render(renderer)
    #cube.transform(matViewProj)
    #cube.transform(matScale)
    
    #sphere.transform(matTrans * matRotY)
    #sphere.render(renderer)

    
    #plane.transform(matTrans)
    #plane.transform(matViewProj)
    plane.render(renderer)
    
    deg += 1
    root.after(100, draw_cube)
    
    
def draw_edge():
    
    global root, canvas, width, height
    
    #canvas.create_line(0, 0, width, height, fill="black", width=1)
    #canvas.create_line(0, height, width, 0, fill="black", width=1)
    
    canvas.create_line(2, 0, 2, height, fill="black", width=3)
    canvas.create_line(0, 2, width, 2, fill="black", width=3)
    canvas.create_line(width - 2, 0, width - 2, height, fill="black", width=3)
    canvas.create_line(0, height - 2, width, height - 2, fill="black", width=3)

    #canvas.create_line(0, 0, 400, 0, fill="black", width=3)
    
def draw_circle_3d():
    global root, canvas, width, height, deg
    canvas.delete('all')
    
    basis = Basis2()
    screen = Screen()
    screen.SetInfo(Vector2(20, 0), Vector2(0, -20), Vector2(width * 0.5, height * 0.5))    
    
    camera = Camera()
    camera.set_projection(1, 1000, 30, width, height)
    camera.set_position(Vector3(0, 0, 200))
    camera.look_at(Vector3(0, 0, 0))
    
    renderer = Renderer(basis, screen, canvas, camera, width, height)    
    plane = Plane()
    plane.set_vertex_buffer()
    plane.set_index_buffer()
    #plane.render(renderer)
    
    matRotZ = Matrix4()
    matRotZ.set_rotaitionX(deg)
    #matRotZ.set_identity()
    #outputtext.gr
    
    matViewProj = renderer.camera.get_view_projection_matrix()
    mat = matViewProj * matRotZ
    
    r = 1
    rad = math.asin(0.3281)
    
    localOrigin = matViewProj * Vector3(0, 0, 0)
    localAxis = matViewProj * (Vector3(matRotZ._11, matRotZ._12, matRotZ._13) * r * 2)
    renderer.draw_line(localOrigin, localAxis, dash=True, color="blue")
    
    localAxis = matViewProj * (Vector3(matRotZ._21, matRotZ._22, matRotZ._23) * r * 2)
    renderer.draw_line(localOrigin, localAxis, dash=True, color="red")
    
    localAxis = matViewProj * (Vector3(matRotZ._31, matRotZ._32, matRotZ._33) * r * 2)
    renderer.draw_line(localOrigin, localAxis, dash=True, color="green")
    
    
    
    theta = (math.pi / 2) - rad
    l1 = draw_point(theta, 0, r, renderer, matRotZ)
    l2 = draw_point(theta, 0, r, renderer, matRotZ)
    renderer.draw_line(mat * l1, mat * l2, True, "cyan")
    
    l1 = draw_point(theta, math.pi * 0.5 + rad, r, renderer, matRotZ)
    l2 = draw_point(theta, math.pi * 0.5 + -rad, r, renderer, matRotZ)
    renderer.draw_line(mat * l1, mat * l2, True, "cyan")    
    
    l1 = draw_point(theta, math.pi + rad, r, renderer, matRotZ)
    l2 = draw_point(theta, math.pi + -rad, r, renderer, matRotZ)
    renderer.draw_line(mat * l1, mat * l2, True, "cyan")
    
    l1 = draw_point(theta, math.pi * 1.5 + rad, r, renderer, matRotZ)
    l2 = draw_point(theta, math.pi * 1.5 + -rad, r, renderer, matRotZ)    
    renderer.draw_line(mat * l1, mat * l2, True, "cyan")
    
    theta = (math.pi / 2) + rad
    draw_point(theta, rad, r, renderer, matRotZ)
    draw_point(theta, -rad, r, renderer, matRotZ)
    
    draw_point(theta, math.pi * 0.5 + rad, r, renderer, matRotZ)
    draw_point(theta, math.pi * 0.5 + -rad, r, renderer, matRotZ)
    
    draw_point(theta, math.pi + rad, r, renderer, matRotZ)
    draw_point(theta, math.pi + -rad, r, renderer, matRotZ)
    
    draw_point(theta, math.pi * 1.5 + rad, r, renderer, matRotZ)
    draw_point(theta, math.pi * 1.5 + -rad, r, renderer, matRotZ)    
    
    theta = rad
    l1 = draw_point(theta, math.pi * 0.5 - rad, r, renderer, matRotZ, "red")
    l2 = draw_point(theta, math.pi * 0.5 + rad, r, renderer, matRotZ, "blue")
    
    # draw_point(theta, -rad, r, renderer, matRotZ)
    # draw_point(-theta, -rad, r, renderer, matRotZ)
    
    # draw_point(math.pi + theta, rad, r, renderer, matRotZ)
    # draw_point(math.pi -theta, rad, r, renderer, matRotZ)
    
    # draw_point(math.pi + theta, -rad, r, renderer, matRotZ)
    # draw_point(math.pi -theta, -rad, r, renderer, matRotZ)
    

    # draw_point(theta, -rad, r, renderer, matRotZ)
    
    # draw_point(theta, math.pi * 0.5 + rad, r, renderer, matRotZ)
    # draw_point(theta, math.pi * 0.5 + -rad, r, renderer, matRotZ)
    
    # draw_point(theta, math.pi + rad, r, renderer, matRotZ)
    # draw_point(theta, math.pi + -rad, r, renderer, matRotZ)
    
    # draw_point(theta, math.pi * 1.5 + rad, r, renderer, matRotZ)
    # draw_point(theta, math.pi * 1.5 + -rad, r, renderer, matRotZ)    
    
    #sphere = Sphere()
    #sphere.set_geometry()
    #sphere.render(renderer)
        
    
    #theta = math.pi * 0.5 - rad        
    theta = math.pi * 0.5
    for i in range(360):
        
        sin_theta = math.sin(theta)
        cos_theta = math.cos(theta)
        
        phi = i * math.pi / 180
        sin_phi = math.sin(phi)
        cos_phi = math.cos(phi)        
        p1 = matViewProj * matRotZ * Vector3(r * sin_theta * cos_phi, r * cos_theta, r * sin_theta * sin_phi)
        
        phi = (i + 2) * math.pi / 180
        sin_phi = math.sin(phi)
        cos_phi = math.cos(phi)
        p2 = matViewProj * matRotZ * Vector3(r * sin_theta * cos_phi, r * cos_theta, r * sin_theta * sin_phi)
        
        renderer.draw_line(p1, p2, True, "red")
        
    #theta = math.pi * 0.5 + rad
    for i in range(360):        
        phi = 0        
        
        sin_phi = math.sin(phi)
        cos_phi = math.cos(phi) 
        
        theta = i * math.pi / 180
        
        sin_theta = math.sin(theta)
        cos_theta = math.cos(theta)       
        p1 = matViewProj * matRotZ * Vector3(r * sin_theta * cos_phi, r * cos_theta, r * sin_theta * sin_phi)
        
        #phi = (i + 2) * math.pi / 180
        
        theta = (i + 2) * math.pi / 180
        sin_theta = math.sin(theta)
        cos_theta = math.cos(theta)       
        
        p2 = matViewProj * matRotZ * Vector3(r * sin_theta * cos_phi, r * cos_theta, r * sin_theta * sin_phi)
        
        renderer.draw_line(p1, p2)
        
    deg += 1
    root.after(100, draw_circle_3d)
    
    # phi = theta
    
    # phi = math.
    # p1 = matViewProj * Vector3(0, 0, 0)
    # p2 = matViewProj * Vector3(r * math.cos(theta), r * math.sin(theta), 1)    
    # renderer.draw_line(p1, p2)
    
    # p1 = matViewProj * Vector3(0, 0, 0)
    # p2 = matViewProj * Vector3(r * math.cos(-theta), r * math.sin(-theta), 1)
    # renderer.draw_line(p1, p2)
    
# def draw_vert_point(theta, rad):
#     draw_point(theta, rad, r, renderer, matRotZ)
#     draw_point(theta, -rad, r, renderer, matRotZ)
    
#     draw_point(theta, math.pi * 0.5 + rad, r, renderer, matRotZ)
#     draw_point(theta, math.pi * 0.5 + -rad, r, renderer, matRotZ)
    
#     draw_point(theta, math.pi + rad, r, renderer, matRotZ)
#     draw_point(theta, math.pi + -rad, r, renderer, matRotZ)
    
#     draw_point(theta, math.pi * 1.5 + rad, r, renderer, matRotZ)
#     draw_point(theta, math.pi * 1.5 + -rad, r, renderer, matRotZ)    
    
def draw_point(theta, phi, r, renderer, matTransform, color="gray"):    
    matViewProj = renderer.camera.get_view_projection_matrix()
    mat = matViewProj * matTransform
    
    sin_theta = math.sin(theta)
    cos_theta = math.cos(theta)
    
    sin_phi = math.sin(phi)
    cos_phi = math.cos(phi)
    
    p1 = Vector3(0, 0, 0)
    p2 = Vector3(r * sin_theta * cos_phi, r * cos_theta, r * sin_theta * sin_phi)
    renderer.draw_line(mat * p1, mat * p2, False, color)
    
    e1 = Vector3(sin_theta * cos_phi, cos_theta, sin_theta * sin_phi)
    e1 *= 0.2
    e1 = p2 + e1        
    renderer.draw_line(mat * p2, mat * e1, True, "red")
    
    e2 = Vector3(cos_theta * cos_phi, -sin_theta, cos_theta * sin_phi)
    e2 *= 0.2
    e2 = p2 + e2
    renderer.draw_line(mat * p2, mat * e2, True, "blue")
    
    e3 = Vector3(-sin_phi, 0, cos_phi)
    e3 *= 0.2
    e3 = p2 + e3
    renderer.draw_line(mat * p2, mat * e3, True, "green")
    
    return p2
    
    
def draw_circle():
    global root, canvas, width, height, deg
    
    matScreen = Matrix3(
                    100, 0, width/2,
                    0, -100, height/2,
                    0, 0, 1
                )    
    
    r = 1
    theta = 0
    for i in range(360):
        theta = i * math.pi / 180
        v1 = Vector2(r * math.cos(theta), r * math.sin(theta))
        v1 = matScreen * v1
        
        theta = (i + 1) * math.pi / 180
        v2 = Vector2(r * math.cos(theta), r * math.sin(theta))
        v2 = matScreen * v2
        
        canvas.create_line(v1.x, v1.y, v2.x, v2.y, fill="black", width=2)
        print(i, theta)
        
    
    w1 = matScreen * Vector2(-2, 0)
    w2 = matScreen * Vector2(2, 0)    
    canvas.create_line(w1.x, w1.y, w2.x, w2.y, fill="blue", width=1, dash=(2,2))
    
    h1 = matScreen * Vector2(0, -2)
    h2 = matScreen * Vector2(0, 2)    
    canvas.create_line(h1.x, h1.y, h2.x, h2.y, fill="red", width=1, dash=(2,2))    
    
    # p1 = matScreen * Vector2(-1, 0.3281)
    # p2 = matScreen * Vector2(1, 0.3281)    
    # canvas.create_line(p1.x, p1.y, p2.x, p2.y, fill="gray", width=1, dash=(2,2))    
    
    # p1 = matScreen * Vector2(-1, -0.3281)
    # p2 = matScreen * Vector2(1, -0.3281)    
    # canvas.create_line(p1.x, p1.y, p2.x, p2.y, fill="gray", width=1, dash=(2,2))    
    
    # p1 = matScreen * Vector2(0.3281, -1)
    # p2 = matScreen * Vector2(0.3281, 1)    
    # canvas.create_line(p1.x, p1.y, p2.x, p2.y, fill="gray", width=1, dash=(2,2))    
    
    # p1 = matScreen * Vector2(-0.3281, -1)
    # p2 = matScreen * Vector2(-0.3281, 1)    
    # canvas.create_line(p1.x, p1.y, p2.x, p2.y, fill="gray", width=1, dash=(2,2))
    
    
    # 1사분면
    theta = math.asin(0.3281)
    p1 = matScreen * Vector3(0, 0, 1)
    p2 = matScreen * Vector3(r * math.cos(theta), r * math.sin(theta), 1)
    canvas.create_line(p1.x, p1.y, p2.x, p2.y, fill="green", width=1, dash=(1,1))
    
    theta = -math.asin(0.3281)
    p1 = matScreen * Vector3(0, 0, 1)
    p2 = matScreen * Vector3(r * math.cos(theta), r * math.sin(theta), 1)
    canvas.create_line(p1.x, p1.y, p2.x, p2.y, fill="green", width=1, dash=(1,1))
    
    # 2사분면
    theta = math.asin(0.3281)
    theta += math.pi * 0.5
    p1 = matScreen * Vector3(0, 0)
    p2 = matScreen * Vector3(r * math.cos(theta), r * math.sin(theta))
    canvas.create_line(p1.x, p1.y, p2.x, p2.y, fill="green", width=1, dash=(1,1))
    
    theta = -math.asin(0.3281)
    theta += math.pi * 0.5
    p1 = matScreen * Vector3(0, 0)
    p2 = matScreen * Vector3(r * math.cos(theta), r * math.sin(theta))
    canvas.create_line(p1.x, p1.y, p2.x, p2.y, fill="green", width=1, dash=(1,1))
    
    # 3사분면
    theta = math.asin(0.3281)
    theta += math.pi
    p1 = matScreen * Vector3(0, 0)
    p2 = matScreen * Vector3(r * math.cos(theta), r * math.sin(theta))
    canvas.create_line(p1.x, p1.y, p2.x, p2.y, fill="green", width=1, dash=(1,1))
    
    theta = -math.asin(0.3281)
    theta += math.pi
    p1 = matScreen * Vector3(0, 0)
    p2 = matScreen * Vector3(r * math.cos(theta), r * math.sin(theta))
    canvas.create_line(p1.x, p1.y, p2.x, p2.y, fill="green", width=1, dash=(1,1))
    
    # 4사분면    
    theta = math.asin(0.3281)
    theta += math.pi * 1.5
    p1 = matScreen * Vector3(0, 0)
    p2 = matScreen * Vector3(r * math.cos(theta), r * math.sin(theta))
    canvas.create_line(p1.x, p1.y, p2.x, p2.y, fill="green", width=1, dash=(1,1))
    
    theta = -math.asin(0.3281)
    theta += math.pi * 1.5
    p1 = matScreen * Vector3(0, 0)
    p2 = matScreen * Vector3(r * math.cos(theta), r * math.sin(theta))
    canvas.create_line(p1.x, p1.y, p2.x, p2.y, fill="green", width=1, dash=(1,1))
    
    #x = math.sin(theta)
    
    #deg =  theta * 180 / math.pi
    #print(deg)
    

def main():
    
    init()
    
    #draw()
    draw_cube()
    #draw_circle_3d()

    root.mainloop() # GUI가 보이고 종료될때까지 실행함
    
if __name__ == "__main__":
    main()
