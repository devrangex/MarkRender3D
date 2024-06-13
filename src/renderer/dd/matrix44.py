import math
import numpy as np
from .vector3 import Vector3

class Matrix44:
    
    # 11, 12, 13, 14
    # 21, 22, 23, 24
    # 31, 32, 33, 34
    # 41, 42, 43, 44
    def __init__(
            self, 
            _11: float = 1, _12: float = 0, _13: float = 0, _14: float = 0,
            _21: float = 0, _22: float = 1, _23: float = 0, _24: float = 0,
            _31: float = 0, _32: float = 0, _33: float = 1, _34: float = 0,
            _41: float = 0, _42: float = 0, _43: float = 0, _44: float = 1,
        ) -> None:
        
        self.elements = [
            [_11, _12, _13, _14],
            [_21, _22, _23, _24],
            [_31, _32, _33, _34],
            [_41, _42, _43, _44],
        ]
        
    def set(
        self, 
            _11: float = 1, _12: float = 0, _13: float = 0, _14: float = 0,
            _21: float = 0, _22: float = 1, _23: float = 0, _24: float = 0,
            _31: float = 0, _32: float = 0, _33: float = 1, _34: float = 0,
            _41: float = 0, _42: float = 0, _43: float = 0, _44: float = 1,
    ):    
        self.elements = [
            [_11, _12, _13, _14],
            [_21, _22, _23, _24],
            [_31, _32, _33, _34],
            [_41, _42, _43, _44],
        ]
        return self
    
    # 11, 12, 13, 14
    # 21, 22, 23, 24
    # 31, 32, 33, 34
    # 41, 42, 43, 44
    def set_element(self, i, j, v):
        self.elements[i - 1][j - 1] = v
    
    def set_identity(self) -> None:        
        self.set()
    
    def set_translation(self, tx: float, ty: float, tz: float) -> None:        
        self.set_identity()
        
        self.set_element(1, 4, tx)
        self.set_element(2, 4, ty)
        self.set_element(3, 4, tz)
        
    def set_rotaitionZByDeg(self, deg) -> None:
        self.set_identity()
        
        rad = deg / 180 * math.pi
        
        # basis
        self.set_element(1, 1, math.cos(rad))
        self.set_element(2, 1, math.sin(rad))
        
        # basis
        self.set_element(1, 2, -math.sin(rad))
        self.set_element(2, 2, math.cos(rad))
        
    def set_rotaitionXByDeg(self, deg) -> None:
        self.set_identity()
        
        rad = deg / 180 * math.pi
        
        # basis
        self.set_element(2, 2, math.cos(rad))
        self.set_element(3, 2, math.sin(rad))
        
        # basis
        self.set_element(2, 3, -math.sin(rad))
        self.set_element(3, 3, math.cos(rad))
        
    def set_rotaitionYByDeg(self, deg) -> None:
        self.set_identity()
        
        rad = deg / 180 * math.pi
        
        # basis
        self.set_element(1, 1, math.cos(rad))
        self.set_element(3, 1, -math.sin(rad))
        
        # basis
        self.set_element(1, 3, math.sin(rad))
        self.set_element(3, 3, math.cos(rad))       
    
    def set_scale(self, sx, sy, sz):
        self.set_identity()
        
        self.set_element(1, 1, sx)
        self.set_element(2, 2, sy)
        self.set_element(3, 3, sz)
        
        
    def set_projection(self, near, far, fov, width, height) -> None:
        self.set_identity()
        
        rad = fov / 180 * math.pi
        d = 1 / math.tan(rad * 0.5)
        invA = width / height
        
        self.set_element(1, 1, d * ( 1 / invA ))
        self.set_element(2, 2, d)
        #self._33 = -1
        self.set_element(3, 3, (near + far) / (near - far))
        self.set_element(4, 3, (2 * near * far) / (near - far))
        self.set_element(3, 4, -1)
        self.set_element(4, 4, 0)
        
        # self._33 = (near + far) / (near - far)
        # self._43 = (2 * near * far) / (near - far)
        # self._34 = -1
        # self._44 = 0
        
    def transpose(self):
        return Matrix44(
            self.elements[0][0], self.elements[1][0], self.elements[2][0], self.elements[3][0],
            self.elements[0][1], self.elements[1][1], self.elements[2][1], self.elements[3][1],
            self.elements[0][2], self.elements[1][2], self.elements[2][2], self.elements[3][2],
            self.elements[0][3], self.elements[1][3], self.elements[2][3], self.elements[3][3],
        )
        
    def get_row(self, row):
        return Vector3(self.elements[row][0], self.elements[row][1], self.elements[row][2], self.elements[row][3])
    
    def get_column(self, column):
        return Vector3(self.elements[0][column], self.elements[1][column], self.elements[2][column], self.elements[3][column])
    
    def __mul__(self, rhs):
        if isinstance(rhs, Matrix44):
            out = Matrix44()
            for i in range(4):
                for j in range(4):                    
                    v1 = self.get_row(i)
                    v2 = rhs.get_column(j)
                    # 내적으로 계산                    
                    out.elements[i][j] = v1.x * v2.x + v1.y * v2.y + v1.z * v2.z + v1.w * v2.w
                    
            return out
                
        elif isinstance(rhs, Vector3):
            
            v1 = self.get_column(0) * rhs.x
            v2 = self.get_column(1) * rhs.y
            v3 = self.get_column(2) * rhs.z
            v4 = self.get_column(3) * rhs.w
            
            v5 = v1 + v2 + v3 + v4
            # Matrix and Vector multiplication
            # x = self.elements[0][0] * rhs.x + self._21 * rhs.y + self._31 * rhs.z + self._41 * rhs.w
            # y = self._12 * rhs.x + self._22 * rhs.y + self._32 * rhs.z + self._42 * rhs.w
            # z = self._13 * rhs.x + self._23 * rhs.y + self._33 * rhs.z + self._43 * rhs.w            
            # w = self._14 * rhs.x + self._24 * rhs.y + self._34 * rhs.z + self._44 * rhs.w           
            
            if v5.w == 0:
                v5.w = 0.00000000001 
            
            return Vector3(v5.x / v5.w, v5.y / v5.w, v5.z / v5.w, v5.w / v5.w)
        else:
            raise TypeError("Unsupported multiplication type")
        
    def __rmul__(self, rhs):
        if isinstance(rhs, Matrix44):
            out = Matrix44()
            for i in range(4):
                for j in range(4):                    
                    v1 = self.get_row(i)
                    v2 = rhs.get_column(j)
                    # 내적으로 계산
                    out.elements[i][j] = v1 * v2
                    
            return out
        
        else:
            raise TypeError("Unsupported multiplication type")

        # else:
        #     raise TypeError("Unsupported multiplication type")
    
        