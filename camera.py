import math
from vector3 import *
from matrix4 import *
from renderer import *

class Camera:
    def __init__(self) -> None:
        self.localPosition: Vector3 = Vector3.zero
        self.localRotation: Vector3 = Vector3.zero
        self.near = 5
        self.far = 1000
        self.fov = 60
        self.width = 800
        self.height = 600
        self.look_at(Vector3(0, 0, -1))

    def set_projection(self, near, far, fov, width, height):
        self.near = near
        self.far = far
        self.fov = fov
        self.width = width
        self.height = height
        
    def get_projection_matrix(self):
        matProj = Matrix4()
        matProj.set_projection(self.near, self.far, self.fov, self.width, self.height)
        return matProj
    
    def get_view_matrix(self):
        matTranslate = Matrix4()
        matTranslate.set_translation(-self.localPosition.x, -self.localPosition.y, -self.localPosition.z)
        
        #dir = self.lookAt - self.localPosition
        #dir.normalized()
        
        axisZ = self.lookDir
        axisX = Vector3.up.cross(axisZ)#.cross()
        axisY = axisX.cross(axisZ)
        
        matRotation = Matrix4(
            axisX.x, axisY.x, axisZ.x, 0,
            axisX.y, axisY.y, axisZ.y, 0,
            axisX.z, axisY.z, axisZ.z, 0,
            0, 0, 0, 1
        )
        matRotInv = matRotation.transpose()
        return matRotInv * matTranslate 
    
    def get_view_projection_matrix(self):
        matProj = self.get_projection_matrix()
        matView = self.get_view_matrix()
        
        return matProj * matView
    
    def set_position(self, position: Vector3):
        self.localPosition = position
    
    def look_at(self, lookPos: Vector3):
        #self.lookAt = lookAt
        dir = lookPos - self.localPosition
        dir.normalized()
        self.lookDir = dir
