from mathmatic.vector3 import Vector3
from mathmatic.matrix44 import Matrix44

class Transform:
    def __init__(self):
        
        self.__pos = Vector3.zero
        # degree
        self.__rotation = Vector3.zero
        self.__scale = Vector3.one
        
    @property
    def pos(self):
        return self.__pos
    
    @pos.setter
    def pos(self, v):
        self.__pos = v
        
    @property
    def rot(self):
        return self.__rotation
    
    @rot.setter
    def rot(self, v):
        self.__rotation = v
        
    @property
    def scale(self):
        return self.__scale
    
    @scale.setter
    def scale(self, v):
        self.__scale = v
        
    def get_transform_matrix(self):
        translate_matrix = Matrix44()
        translate_matrix.set_translation(self.pos.x, self.pos.y, self.pos.z)
        
        x_rot_matrix = Matrix44()
        x_rot_matrix.set_rotaitionXByDeg(self.rot.x)
        
        y_rot_matrix = Matrix44()
        y_rot_matrix.set_rotaitionYByDeg(self.rot.y)
        
        z_rot_matrix = Matrix44()
        z_rot_matrix.set_rotaitionZByDeg(self.rot.z)
        
        scale_matrix = Matrix44()
        scale_matrix.set_scale(self.scale.x, self.scale.y, self.scale.z)
        
        return translate_matrix * x_rot_matrix * y_rot_matrix * z_rot_matrix * scale_matrix