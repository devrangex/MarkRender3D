import tkinter as tk
from vector2 import *
from vector3 import *
from basis2 import *
from screen import *

class Renderer:
    
    def __init__(self, basis: Basis2, screen: Screen, canvas) -> None:
        self.basis: Basis2 = basis        
        self.screen: Screen = screen
        self.canvas =  canvas
        
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
            
    def draw_line(self, v0: Vector2, v1: Vector2, dash:bool = False) -> None:
        v0 = (self.basis * v0)
        v1 = (self.basis * v1)
        
        v0 = self.screen * v0
        v1 = self.screen * v1
        #invZ = v0.z
        
        #if(dash):
        #    self.canvas.create_line(v0.x, v0.y, v1.x, v1.y, fill="red", width=2, dash=(2,2))
        #else:
        self.canvas.create_line(v0.x, v0.y, v1.x, v1.y, fill="gray", width=2)
        
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
        for i in range(primitive_counter):
            i1 = index_buffer[counter]
            i2 = index_buffer[counter+1]
            i3 = index_buffer[counter+2]
            
            u = vertex_buffer[i1] - vertex_buffer[i2]
            v = vertex_buffer[i1] - vertex_buffer[i3]
            n = u.cross(v)
            f = Vector3(0, 0, -1)
            
            dash: bool = False
            if(n.dot(f) > 0):
                dash = True
            
            self.draw_line(vertex_buffer[i1], vertex_buffer[i2], dash)
            self.draw_line(vertex_buffer[i2], vertex_buffer[i3], dash)
            self.draw_line(vertex_buffer[i3], vertex_buffer[i1], dash)
            
            counter += 3
        
        