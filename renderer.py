import tkinter as tk
from vector2 import *
from vector3 import *
from basis2 import *
from screen import *

class Renderer:
    
    def __init__(self, basis: Basis2, screen: Screen, canvas, camera) -> None:
        self.basis: Basis2 = basis        
        self.screen: Screen = screen
        self.canvas =  canvas
        self.camera = camera
        
    def draw_grid(self, numH: int, numV: int) -> None:
        h_begin = int(-numH * 0.5 - 0.5)
        for i in range(numH+1):
            v0 = Vector2(h_begin, 0) + Vector2(0, -numV * 0.5)
            v1 = Vector2(h_begin, 0) + Vector2(0, numV * 0.5)
            
            v0 = self.basis * v0
            v1 = self.basis * v1
            
            v0 = self.screen * v0
            v1 = self.screen * v1
            
            self.canvas.create_line(v0.x, v0.y, v1.x, v1.y, fill="gray", width=1, dash=(4,2))
            
            h_begin += 1
            
        v_begin = int(-numV * 0.5 - 0.5)
        for i in range(numV+1):
            v0 = Vector2(0, v_begin) + Vector2(-numH / 2, 0)
            v1 = Vector2(0, v_begin) + Vector2(numH / 2, 0)
            
            v0 = (self.basis * v0)
            v1 = (self.basis * v1)
            
            v0 = self.screen * v0
            v1 = self.screen * v1
            
            self.canvas.create_line(v0.x, v0.y, v1.x, v1.y, fill="gray", width=1, dash=(4,2))
            
            v_begin += 1
            
        o = Vector2(0,0)
        o = self.screen * o
        i = self.screen * (self.basis.axis1)
        j = self.screen * (self.basis.axis2)
        
        self.canvas.create_line(o.x, o.y, i.x, i.y, fill="blue", width=2, arrow=tk.LAST)
        self.canvas.create_line(o.x, o.y, j.x, j.y, fill="red", width=2, arrow=tk.LAST)

            
    def draw_line(self, v0: Vector3, v1: Vector3, dash:bool = False, color: str = "gray") -> None:
        #start = Vector3(v0.x / v0.w, v0.y / v0.w, v0.z / v0.w)
        #end = Vector3(v1.x / v1.w, v1.y / v1.w, v1.z / v1.w)
        
        
        
        start = Vector2(v0.x * 800 * 0.5, v0.y * 600 * 0.5)
        end = Vector2(v1.x * 800 * 0.5, v1.y * 600 * 0.5)
        
        start = self.screen * start
        end = self.screen * end
        #v0 = (self.basis * v0)
        #v1 = (self.basis * v1)
        
        #v0 = self.screen * v0 * 0.5
        #v1 = self.screen * v1 * 0.5
        #invZ = v0.z
        
        if(dash):
            self.canvas.create_line(start.x, start.y, end.x, end.y, fill=color, width=2, dash=(2,2))
        else:
            self.canvas.create_line(start.x, start.y, end.x, end.y, fill=color, width=2)
        
    def draw_indexed_primitive_line_list(self, index_buffer, primiteve_counter, vertex_buffer):
        i1 = 0
        i2 = 0
        counter = 0
        for i in range(primiteve_counter):
            i1 = index_buffer[counter]
            i2 = index_buffer[counter+1]
            
            self.draw_line(vertex_buffer[i1], vertex_buffer[i2])
            
            counter += 2
            
    def draw_indexed_primitive_line_strip(self, index_buffer, primitive_counter, vertex_buffer: Vector3):
        i1 = 0
        i2 = 0
        i3 = 0
        counter = 0
        matViewProj = self.camera.get_view_projection_matrix()
        
        for i in range(primitive_counter):
            i1 = index_buffer[counter]
            i2 = index_buffer[counter+1]
            i3 = index_buffer[counter+2]
            
            v1 = vertex_buffer[i1]
            v2 = vertex_buffer[i2]
            v3 = vertex_buffer[i3]
            
            u = v1 - v2
            v = v1 - v3
            n = u.cross(v)
            n.normalized()
            f = self.camera.lookDir
            
            color = "gray"
            dash: bool = False
            if(n.dot(f) > 0):
                color = "cyan"
                dash = True
                
            

            v1 = matViewProj * v1
            v2 = matViewProj * v2
            v3 = matViewProj * v3
            
            self.draw_line(v1, v2, dash, color)
            self.draw_line(v2, v3, dash, color)
            self.draw_line(v3, v1, dash, color)
            
            counter += 3
    
    def draw_primitive_line(self, vertex_buffer: Vector3):
        matViewProj = self.camera.get_view_projection_matrix()
        for vertex in vertex_buffer:
            #x2d, y2d = project_3d_to_2d(vertex.x, vertex.y, vertex.z)
            # Adjust the projected coordinates to fit the canvas
            v = matViewProj * vertex
            
            #x = (x2d + 1) * (width / 2)
            #y = (y2d + 1) * (height / 2)
            v = Vector2(v.x * 800 * 0.5, v.y * 600 * 0.5)            
            v = self.screen * v
            
            self.canvas.create_oval(v.x - 2, v.y - 2, v.x + 2, v.y + 2, fill='black')
        