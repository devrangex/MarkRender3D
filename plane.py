import math
from vector3 import *
from matrix4 import *
from renderer import *

class Plane:
    def __init__(self) -> None:
        self.index_buffer: int = []
        self.index_size: int = 0
        self.vertex_buffer: Vector3 = []
        self.vertex_size = 0        
        
    def set_vertex_buffer(self):
        self.vertex_buffer = [Vector3(0, 0, 0),
                                Vector3(10, 0, 0),
                                Vector3(0, 10, 0),
                                Vector3(0, 0, 10)]
        self.vertex_size = 4
        
    def set_index_buffer(self):
        buffer: int = [
            0, 1,
            0, 2,
            0, 3
        ]
        
        for i in range(len(buffer)):
            self.index_buffer.append(buffer[i])
        self.index_size = len(buffer)
    
    def render(self, renderer: Renderer):
        matViewProj = renderer.camera.get_view_projection_matrix()
        self.transform(matViewProj)
        
        i1 = self.index_buffer[0]
        i2 = self.index_buffer[1]
        renderer.draw_line(self.vertex_buffer[i1], self.vertex_buffer[i2], True, "red")
        
        i1 = self.index_buffer[2]
        i2 = self.index_buffer[3]
        renderer.draw_line(self.vertex_buffer[i1], self.vertex_buffer[i2], True, "blue")
        
        i1 = self.index_buffer[4]
        i2 = self.index_buffer[5]
        renderer.draw_line(self.vertex_buffer[i1], self.vertex_buffer[i2], True, "green")
        
        #renderer.draw_indexed_primitive_line_list(self.index_buffer, 1, self.vertex_buffer)
        
    def transform(self, mat: Matrix4):
        buffer = []
        for i in range(len(self.vertex_buffer)):
            buffer.append(mat * self.vertex_buffer[i])
            
        self.vertex_buffer = buffer
        
    
        
            
        