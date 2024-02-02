import math
from vector2 import *

class Matrix3:
    def __init__(
            self, 
            _11: float = 1, _21: float = 0, _31: float = 0,
            _12: float = 0, _22: float = 1, _32: float = 0,
            _13: float = 0, _23: float = 0, _33: float = 1,
        ) -> None:
        self._11: float = _11
        self._21: float = _21
        self._31: float = _31
        
        self._12: float = _12
        self._22: float = _22
        self._32: float = _32
        
        self._13: float = _13
        self._23: float = _23
        self._33: float = _33
        
    def set(
        self, 
        _11: float = 1, _21: float = 0, _31: float = 0,
        _12: float = 0, _22: float = 1, _32: float = 0,
        _13: float = 0, _23: float = 0, _33: float = 1,
    ):    
        self._11: float = _11
        self._21: float = _21
        self._31: float = _31
        
        self._12: float = _12
        self._22: float = _22
        self._32: float = _32
        
        self._13: float = _13
        self._23: float = _23
        self._33: float = _33
        
        return self
    
    def set_identity(self) -> None:
        self._11 = 1
        self._21 = 0
        self._31 = 0
        
        self._12 = 0
        self._22 = 1
        self._32 = 0
        
        self._13 = 0
        self._23 = 0
        self._33 = 1
    
    def set_translation(self, tx: float, ty: float) -> None:        
        self.set_identity()
        
        self._31 = tx
        self._32 = ty
        
    def set_rotaition(self, deg) -> None:
        self.set_identity()
        
        rad = deg / 180 * math.pi
        self._11 = math.cos(rad)
        self._12 = math.sin(rad)
        self._21 = -math.sin(rad)
        self._22 = math.cos(rad)
    
    def __mul__(self, other):
        if isinstance(other, Matrix3):
            # Matrix multiplication            
            return Matrix3(
                (self._11 * other._11 + self._21 * other._12 + self._31 * other._13), (self._11 * other._21 + self._21 * other._22 + self._31 * other._23), (self._11 * other._31 + self._21 * other._32 + self._31 * other._33),
                (self._12 * other._11 + self._22 * other._12 + self._32 * other._13), (self._12 * other._21 + self._22 * other._22 + self._32 * other._23), (self._12 * other._31 + self._22 * other._32 + self._32 * other._33),
                (self._13 * other._11 + self._23 * other._12 + self._33 * other._13), (self._13 * other._21 + self._23 * other._22 + self._33 * other._23), (self._13 * other._31 + self._23 * other._32 + self._33 * other._33),
            )
        elif isinstance(other, Vector2):
            # Matrix and Vector multiplication
            x = self._11 * other.x + self._21 * other.y + self._31 * 1
            y = self._12 * other.x + self._22 * other.y + self._32 * 1
            z = self._13 * other.x + self._23 * other.y + self._33 * 1            
            
            return Vector2(x / z, y / z)
        else:
            raise TypeError("Unsupported multiplication type")
    
        