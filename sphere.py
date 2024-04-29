import math
from vector3 import *
from matrix4 import *
from renderer import *

class Vertex:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class Sphere:
    def __init__(self) -> None:
        self.index_buffer: int = []
        self.index_size: int = 0
        self.vertex_buffer: Vector3 = []
        self.vertex_size = 0        
        
        self.radius = 1
        self.latitude_bands = 5
        self.longitude_bands = 5
        self.indices_cnt = 0
        
    def set_geometry(self):
        self.vertices, self.indices = self.generate_sphere_vertices(self.radius, self.latitude_bands, self.longitude_bands)
        
    def generate_sphere_vertices(self, radius, latitude_bands, longitude_bands):
        vertices = []
        indices = []

        for lat_number in range(latitude_bands + 1):
            theta = lat_number * math.pi / latitude_bands
            sin_theta = math.sin(theta)
            cos_theta = math.cos(theta)

            for long_number in range(longitude_bands + 1):
                phi = long_number * 2 * math.pi / longitude_bands
                sin_phi = math.sin(phi)
                cos_phi = math.cos(phi)

                x = radius * cos_phi * sin_theta
                y = radius * cos_theta
                z = radius * sin_phi * sin_theta
                vertices.append(Vector3(x, y, z))
                # Add calculations for texture coordinates and normals if needed
                
        self.indices_cnt = 0
        for lat_number in range(latitude_bands):
            for long_number in range(longitude_bands):
                first = lat_number * (longitude_bands + 1) + long_number
                second = first + longitude_bands + 1

                indices.append(first)
                indices.append(second)
                indices.append(first + 1)
                self.indices_cnt += 1

                indices.append(second)
                indices.append(second + 1)
                indices.append(first + 1)
                self.indices_cnt += 1

        return vertices, indices
    
    def render(self, renderer: Renderer):
        #matViewProj = renderer.camera.get_view_projection_matrix()
        #self.transform(matViewProj)
        
        #renderer.draw_primitive_line(self.vertices)
        renderer.draw_indexed_primitive_line_strip_2(self.indices, self.indices_cnt, self.vertices)
        
    def transform(self, mat: Matrix4):
        buffer = []
        for i in range(len(self.vertices)):
            buffer.append(mat * self.vertices[i])
            
        self.vertices = buffer
        
    
        
            
        