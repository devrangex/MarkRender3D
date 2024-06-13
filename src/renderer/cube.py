import math
from .gameobject import GameObject
from renderer.dd.vector3 import Vector3
from renderer.dd.matrix44 import Matrix44

class Cube(GameObject):
    def __init__(self) -> None:         
        self.index_buffer: int = []
        self.index_size: int = 0
        self.vertex_buffer: Vector3 = []
        self.vertex_size = 0   
        self.primitive_counter = 12     
        
        self.set_vertex_buffer()
        self.set_index_buffer()
        
        self.deltaRot = 0
        self.matLocal = Matrix44()
        #self.matLocal.set_translation(10, 10, 10)
        
    def set_vertex_buffer(self):
        self.vertex_buffer = [Vector3(-5, -5, 5),
                                Vector3(-5, 5, 5),
                                Vector3(5, 5, 5),
                                Vector3(5, -5, 5),
                                Vector3(-5, -5, -5),
                                Vector3(-5, 5, -5),
                                Vector3(5, 5, -5),
                                Vector3(5, -5, -5)]
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
    
    #def draw(self, renderer: Renderer):
        #matViewProj = renderer.camera.get_view_projection_matrix()
        #self.transform(matViewProj)
        
        #renderer.draw_indexed_primitive_line_strip(self.index_buffer, 12, self.vertex_buffer)
        
    # def transform(self, mat: Matrix4):
    #     buffer = []
    #     for i in range(len(self.vertex_buffer)):
    #         buffer.append(mat * self.vertex_buffer[i])
            
    #     self.vertex_buffer = buffer
    
    def update(self, deltaTime):
        self.deltaRot += deltaTime * 45
        
        matRotY = Matrix44()
        matRotY.set_rotaitionYByDeg(self.deltaRot)
        
        matRotZ = Matrix44()
        matRotZ.set_rotaitionZByDeg(self.deltaRot)
        
        matScale = Matrix44()
        matScale.set_scale(1, 1, 1)
        
        self.matLocal = matRotY * matRotZ * matScale
        
    
    def draw(self, surface, renderer):
        i1 = 0
        i2 = 0
        i3 = 0
        counter = 0
        #matViewProj = self.camera.get_view_projection_matrix()
        
        for i in range(self.primitive_counter):
            i1 = self.index_buffer[counter]
            i2 = self.index_buffer[counter+1]
            i3 = self.index_buffer[counter+2]
            
            v1 = self.vertex_buffer[i1]
            v2 = self.vertex_buffer[i2]
            v3 = self.vertex_buffer[i3]
            
            # u = v1 - v2
            # v = v1 - v3
            # n = u.cross(v)
            # n.normalized()
            # f = self.camera.lookDir
            
            # color = "gray"
            # dash: bool = False
            # if(n.dot(f) > 0):
            #     color = "cyan"
            #     dash = True

            v1 = renderer.matProj * self.matLocal * v1
            v2 = renderer.matProj * self.matLocal * v2
            v3 = renderer.matProj * self.matLocal * v3
            
            renderer.fill_triangle(surface, int(v1.x), int(v1.y), (255, 0, 0), 
                                        int(v2.x), int(v2.y), (0, 255, 0),
                                        int(v3.x), int(v3.y), (0, 0, 255))
            
            # self.draw_line(v1, v2, dash, color)
            # self.draw_line(v2, v3, dash, color)
            # self.draw_line(v3, v1, dash, color)
            
            counter += 3
    
        
            
        