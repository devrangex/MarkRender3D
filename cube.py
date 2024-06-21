import math
from vector3 import *
from matrix4 import *
from renderer import *

class Cube:
    def __init__(self) -> None:
        self.index_buffer: int = []
        self.index_size: int = 0
        self.vertex_buffer: Vector3 = []
        self.vertex_size = 0        
        
    def set_vertex_buffer(self):
        self.vertex_buffer = [Vector3(-50, -50, 50),
                                Vector3(-50, 50, 50),
                                Vector3(50, 50, 50),
                                Vector3(50, -50, 50),
                                Vector3(-50, -50, -50),
                                Vector3(-50, 50, -50),
                                Vector3(50, 50, -50),
                                Vector3(50, -50, -50)]
        self.vertex_size = 4
        
    def set_index_buffer(self):
        buffer: int = [
            0, 2, 1,
            2, 0, 3,
            3, 6, 2,
            6, 3, 7,
            7, 5, 6,
            5, 7, 4,
            4, 1, 5,
            1, 4, 0,
            4, 3, 0,
            3, 4, 7,
            1, 6, 5,
            6, 1, 2
        ]
        
        for i in range(len(buffer)):
            self.index_buffer.append(buffer[i])
        index_size = len(buffer)
    
    def render(self, renderer: Renderer):
        #matViewProj = renderer.camera.get_view_projection_matrix()
        #self.transform(matViewProj)
        
        renderer.draw_indexed_primitive_line_strip(self.index_buffer, 12, self.vertex_buffer)
        
    def transform(self, mat: Matrix4):
        buffer = []
        for i in range(len(self.vertex_buffer)):
            buffer.append(mat * self.vertex_buffer[i])
            
        self.vertex_buffer = buffer
        
    
        
            
        