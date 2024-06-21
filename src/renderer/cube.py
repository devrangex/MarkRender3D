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
        size = 1
        self.vertex_buffer = [Vector3(-size, -size, size),
                                Vector3(-size, size, size),
                                Vector3(size, size, size),
                                Vector3(size, -size, size),
                                Vector3(-size, -size, -size),
                                Vector3(-size, size, -size),
                                Vector3(size, size, -size),
                                Vector3(size, -size, -size)]
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
        
        matTranslate = Matrix44()
        matTranslate.set_translation(0, 0, 100)
        
        matRotY = Matrix44()
        matRotY.set_rotaitionYByDeg(self.deltaRot)
        
        matRotZ = Matrix44()
        matRotZ.set_rotaitionZByDeg(self.deltaRot)
        
        matRotX = Matrix44()
        matRotX.set_rotaitionXByDeg(self.deltaRot)
        
        matScale = Matrix44()
        matScale.set_scale(5, 5, 5)
        
        #self.matLocal = matTranslate * matRotY * matRotZ * matScale
        #self.matLocal = matTranslate * matScale
        self.matLocal = matRotZ * matScale
        #self.matLocal.set_identity()
        
    
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
            
            p1 = self.vertex_buffer[i1]
            p2 = self.vertex_buffer[i2]
            p3 = self.vertex_buffer[i3]
            
            # u = v1 - v2
            # v = v1 - v3
            # n = u.cross(v)
            # n.normalized()
            # f = self.camera.lookDir
            
            # color = "gray"
            # dash: bool = False
            # if(n.dot(f) > 0):a
            #     color = "cyan"
            #     dash = True
            
            matView = renderer.get_main_camera().get_view_matrix()
            matProj = renderer.get_main_camera().get_projection_matrix()
            
            # modeling matrix
            matViewLocal = matView * self.matLocal
            matProjViewLocal = matProj * matViewLocal
            #p2 = self.matLocal * p2
            #p3 = self.matLocal * p3
            
            # NDC 좌표로 변환
            p1 = matProjViewLocal.vector4_multiplication(p1)
            p2 = matProjViewLocal.vector4_multiplication(p2)
            p3 = matProjViewLocal.vector4_multiplication(p3)
            
            # Screen 좌표로 변환
            v1 = Vector3(p1.x * renderer.width * 0.5, p1.y * renderer.height * 0.5, p1.z)
            v2 = Vector3(p2.x * renderer.width * 0.5, p2.y * renderer.height * 0.5, p2.z)
            v3 = Vector3(p3.x * renderer.width * 0.5, p3.y * renderer.height * 0.5, p3.z)
            
            # v1 = renderer.screenCoordinates.trasnform(v1)
            # v2 = renderer.screenCoordinates.trasnform(v2)
            # v3 = renderer.screenCoordinates.trasnform(v3)
            
            
            # projection matrix                        
            #v1 = matProj * p1
            #v2 = matProj * p2
            #v3 = matProj * p3

            #matWorldViewProj = matViewProj * self.matLocal
            #matWorldViewProj = matViewProj
            
            # v1 = matWorldViewProj * p1
            # v2 = matWorldViewProj * p2
            # v3 = matWorldViewProj * p3
            
            # v1 = Vector3(v1.x / v1.w, v1.y / v1.w, v1.z / v1.w)
            # v2 = Vector3(v2.x / v2.w, v2.y / v2.w, v2.z / v2.w)
            # v3 = Vector3(v3.x / v3.w, v3.y / v3.w, v3.z / v3.w)
            
            renderer.fill_triangle(surface, int(v1.x), int(v1.y), (255, 0, 0), 
                                        int(v2.x), int(v2.y), (0, 255, 0),
                                        int(v3.x), int(v3.y), (0, 0, 255))
            
            # self.draw_line(v1, v2, dash, color)
            # self.draw_line(v2, v3, dash, color)
            # self.draw_line(v3, v1, dash, color)
            
            counter += 3
    
        
            
        