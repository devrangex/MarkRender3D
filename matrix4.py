import math
from vector2 import *
from vector3 import *

class Matrix4:
    def __init__(
            self, 
            _11: float = 1, _21: float = 0, _31: float = 0, _41: float = 0,
            _12: float = 0, _22: float = 1, _32: float = 0, _42: float = 0,
            _13: float = 0, _23: float = 0, _33: float = 1, _43: float = 0,
            _14: float = 0, _24: float = 0, _34: float = 0, _44: float = 1,
        ) -> None:
        self._11: float = _11
        self._21: float = _21
        self._31: float = _31
        self._41: float = _41
        
        self._12: float = _12
        self._22: float = _22
        self._32: float = _32
        self._42: float = _42
        
        self._13: float = _13
        self._23: float = _23
        self._33: float = _33
        self._43: float = _43
        
        self._14: float = _14
        self._24: float = _24
        self._34: float = _34
        self._44: float = _44
        
    def set(
        self, 
        _11: float = 1, _21: float = 0, _31: float = 0, _41: float = 0,
        _12: float = 0, _22: float = 1, _32: float = 0, _42: float = 0,
        _13: float = 0, _23: float = 0, _33: float = 1, _43: float = 0,
        _14: float = 0, _24: float = 0, _34: float = 0, _44: float = 1,
    ):    
        self._11: float = _11
        self._21: float = _21
        self._31: float = _31
        self._41: float = _41
        
        self._12: float = _12
        self._22: float = _22
        self._32: float = _32
        self._42: float = _42
        
        self._13: float = _13
        self._23: float = _23
        self._33: float = _33
        self._43: float = _43
        
        self._14: float = _14
        self._24: float = _24
        self._34: float = _34
        self._44: float = _44
        
        return self
    
    def set_identity(self) -> None:        
        self.set()
    
    def set_translation(self, tx: float, ty: float, tz: float) -> None:        
        self.set_identity()
        
        self._41 = tx
        self._42 = ty
        self._43 = tz
        
    def set_rotaitionZ(self, deg) -> None:
        self.set_identity()
        
        rad = deg / 180 * math.pi
        self._11 = math.cos(rad)
        self._12 = math.sin(rad)
        self._21 = -math.sin(rad)
        self._22 = math.cos(rad)
        
    def set_rotaitionX(self, deg) -> None:
        self.set_identity()
        
        rad = deg / 180 * math.pi
        self._22 = math.cos(rad)
        self._23 = math.sin(rad)
        self._32 = -math.sin(rad)
        self._33 = math.cos(rad)
        
    def set_rotaitionY(self, deg) -> None:
        self.set_identity()
        
        rad = deg / 180 * math.pi
        self._11 = math.cos(rad)
        self._31 = math.sin(rad)
        self._13 = -math.sin(rad)
        self._33 = math.cos(rad)
        
    def set_projection(self, near, far, fov, width, height) -> None:
        self.set_identity()
        
        rad = fov / 180 * math.pi
        d = 1 / math.tan(rad * 0.5)
        invA = width / height
        
        self._11 = d * ( 1 / invA )
        self._22 = d
        #self._33 = -1
        self._33 = (near + far) / (near - far)
        self._43 = (2 * near * far) / (near - far)
        self._34 = -1
    
    def __mul__(self, other):
        if isinstance(other, Matrix4):
            # Matrix multiplication            
            return Matrix4(
                (self._11 * other._11 + self._21 * other._12 + self._31 * other._13 + self._41 * other._14), (self._11 * other._21 + self._21 * other._22 + self._31 * other._23 + self._41 * other._24), (self._11 * other._31 + self._21 * other._32 + self._31 * other._33 + self._41 * other._34), (self._11 * other._41 + self._21 * other._42 + self._31 * other._43 + self._41 * other._44), 
                (self._12 * other._11 + self._22 * other._12 + self._32 * other._13 + self._42 * other._14), (self._12 * other._21 + self._22 * other._22 + self._32 * other._23 + self._42 * other._24), (self._12 * other._31 + self._22 * other._32 + self._32 * other._33 + self._42 * other._34), (self._12 * other._41 + self._22 * other._42 + self._32 * other._43 + self._42 * other._44), 
                (self._13 * other._11 + self._23 * other._12 + self._33 * other._13 + self._43 * other._14), (self._13 * other._21 + self._23 * other._22 + self._33 * other._23 + self._43 * other._24), (self._13 * other._31 + self._23 * other._32 + self._33 * other._33 + self._43 * other._34), (self._13 * other._41 + self._23 * other._42 + self._33 * other._43 + self._43 * other._44), 
                (self._14 * other._11 + self._24 * other._12 + self._34 * other._13 + self._44 * other._14), (self._14 * other._21 + self._24 * other._22 + self._34 * other._23 + self._44 * other._24), (self._14 * other._31 + self._24 * other._32 + self._34 * other._33 + self._44 * other._34), (self._14 * other._41 + self._24 * other._42 + self._34 * other._43 + self._44 * other._44), 
            )
        elif isinstance(other, Vector3):
            # Matrix and Vector multiplication
            x = self._11 * other.x + self._21 * other.y + self._31 * other.z + self._41 * 1
            y = self._12 * other.x + self._22 * other.y + self._32 * other.z + self._42 * 1
            z = self._13 * other.x + self._23 * other.y + self._33 * other.z + self._43 * 1            
            w = self._14 * other.x + self._24 * other.y + self._34 * other.z + self._44 * 1            
            
            return Vector3(x / w, y / w, z / w)
        else:
            raise TypeError("Unsupported multiplication type")
    
        