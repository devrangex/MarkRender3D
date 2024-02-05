import math
from vector3 import *
from matrix4 import *

class Polygon:
    def __init__(self) -> None:
        self.index_buffer: int = []
        self.index_size: int = 0
        self.vertex_buffer: Vector3 = []
        self.vertex_size = 0        
        
    def set_vertex_buffer(self):
        self.vertex_buffer = [Vector3(-5, -5, 5),
                                Vector3(-5, 5, 5),
                                Vector3(5, 5, 5),
                                Vector3(5, -5, 5)]
        self.vertex_size = 4
        
    def set_index_buffer(self):
        buffer: int = [
            0, 1,
            1, 3,
            3, 0,
            1, 2,
            2, 3,
            3, 1
        ]
        
        for i in range(12):
            self.index_buffer.append(buffer[i])
        index_size = 12
    
    def render(self, renderer):
        renderer.draw_indexed_primitive_line_list(self.index_buffer, 6, self.vertex_buffer)
        
    def transform(self, mat: Matrix4):
        buffer = []
        for i in range(len(self.vertex_buffer)):
            buffer.append(mat * self.vertex_buffer[i])
            
        self.vertex_buffer = buffer
        
    
        
            
        