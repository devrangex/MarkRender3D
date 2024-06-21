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
        
        self.elements[0][3] = tx
        self.elements[1][3] = ty
        self.elements[2][3] = tz
        
    def set_rotaitionZByDeg(self, deg) -> None:
        self.set_identity()
        
        # cos,  -sin,   0,      0
        # sin,  cos,    0,      0
        # 0,    0,      1,      0
        # 0,    0,      0,      1
        
        self.set_identity()
        
        # degree to radian
        rad = deg / 180 * math.pi
        
        # basis 1
        self.elements[0][0] = math.cos(rad)
        self.elements[1][0] = math.sin(rad)
        
        # basis 2
        self.elements[0][1] = -math.sin(rad)
        self.elements[1][1] = math.cos(rad)    
        
    def set_rotaitionXByDeg(self, deg) -> None:
        self.set_identity()
        
        # 1,    0,      0,      0
        # 0,    cos,    -sin,   0
        # 0,    sin,    cos,    0
        # 0,    0,      0,      1
        
        rad = deg / 180 * math.pi
        
        # basis 1
        self.elements[1][1] = math.cos(rad)
        self.elements[2][1] = math.sin(rad)
        
        # basis 2
        self.elements[1][2] = -math.sin(rad)
        self.elements[2][2] = math.cos(rad)
        
    def set_rotaitionYByDeg(self, deg) -> None:
        self.set_identity()
        
        # cos,    0,    sin,    0
        # 0,      1,    0,      0
        # -sin,   0,    cos,    0
        # 0,      0,    0,      1
        
        rad = deg / 180 * math.pi
        
        # basis 1
        self.elements[0][0] = math.cos(rad)
        self.elements[2][0] = -math.sin(rad)
        
        # basis 2
        self.elements[0][2] = math.sin(rad)
        self.elements[2][2] = math.cos(rad)            
    
    def set_scale(self, sx, sy, sz):
        self.set_identity()
        
        # sx,     0,    0,     0
        # 0,      sy,   0,     0
        # 0,      0,    sz,    0
        # 0,      0,    0,     1
        
        self.elements[0][0] = sx
        self.elements[1][1] = sy
        self.elements[2][2] = sz
        
        
    def set_projection(self, near, far, fov, width, height) -> None:
        self.set_identity()
        
        rad = fov / 180 * math.pi
        d = 1 / math.tan(rad * 0.5)
        invA = 1 / (width / height)
        invNF = 1 / (near - far)
        k = (far + near) * invNF
        l = 2 * near * far * invNF
        
        # | d/a       0           0           0       |             | x |       | x * d/a                           |
        # | 0         d           0           0       |             | y |       | y * d                             |
        # | 0         0      (n+f)/(n-f) (2nf)/(n-f)  |    *        | z |  =    | z * (n+f)/(n-f) + z*(2nf)/(n-f)   |
        # | 0         0          -1           0       |             | w |       | z * -1                            |
        
        self.elements[0][0] = d * invA
        self.elements[1][1] = d
        self.elements[2][2] = k
        self.elements[2][3] = l
        self.elements[3][2] = -1
        self.elements[3][3] = 0
        
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
    
    def vector4_multiplication(self, rhs):
        x = self.elements[0][0] * rhs.x + self.elements[0][1] * rhs.y + self.elements[0][2] * rhs.z + self.elements[0][3]
        y = self.elements[1][0] * rhs.x + self.elements[1][1] * rhs.y + self.elements[1][2] * rhs.z + self.elements[1][3]
        z = self.elements[2][0] * rhs.x + self.elements[2][1] * rhs.y + self.elements[2][2] * rhs.z + self.elements[2][3]
        w = self.elements[3][0] * rhs.x + self.elements[3][1] * rhs.y + self.elements[3][2] * rhs.z + self.elements[3][3]
        
        # smaller value
        if w == 0:
            w = 0.00000000001 
            
        # for homogeneous devide
        invW = 1 / w
        
        return Vector3(x * invW, y * invW, z * invW, w * invW)
    
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
            
            # Matrix and Vector multiplication
            x = self.elements[0][0] * rhs.x + self.elements[0][1] * rhs.y + self.elements[0][2] * rhs.z + self.elements[0][3]
            y = self.elements[1][0] * rhs.x + self.elements[1][1] * rhs.y + self.elements[1][2] * rhs.z + self.elements[1][3]
            z = self.elements[2][0] * rhs.x + self.elements[2][1] * rhs.y + self.elements[2][2] * rhs.z + self.elements[2][3]
            w = self.elements[3][0] * rhs.x + self.elements[3][1] * rhs.y + self.elements[3][2] * rhs.z + self.elements[3][3]            
            
            return Vector3(x, y, z, w)
        else:
            raise TypeError("Unsupported multiplication type")
        
    def __rmul__(self, lhs):
        if isinstance(lhs, Matrix44):
            out = Matrix44()
            for i in range(4):
                for j in range(4):                    
                    v1 = lhs.get_row(i)
                    v2 = self.get_column(j)
                    # 내적으로 계산
                    out.elements[i][j] = v1 * v2
                    
            return out
        
        else:
            raise TypeError("Unsupported multiplication type")
    
        