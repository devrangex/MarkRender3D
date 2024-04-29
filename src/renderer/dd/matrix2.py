from .vector2 import Vector2

class Matrix2:
    def __init__(
            self, 
            _11: float = 1, _12: float = 0,
            _21: float = 0, _22: float = 1,
        ) -> None:
        self._11: float = _11
        self._12: float = _12
        self._21: float = _21
        self._22: float = _22
        
    def set(
        self, 
        _11: float = 1, _12: float = 0,
        _21: float = 0, _22: float = 1,
    ):    
        self._11: float = _11
        self._11: float = _12
        self._21: float = _21
        self._22: float = _22
        
        return self
    
    def __mul__(self, other):
        if isinstance(other, Matrix2):
            return Matrix2(
                self._11 * other._11 + self._21 * other._12, self._11 * other._21 + self._21 * other._22,
                self._12 * other._11 + self._22 * other._12, self._12 * other._21 + self._22 * other._22
            )
        elif isinstance(other, Vector2):            
            return Vector2(
                self._11 * other.x + self._21 * other.y, 
                self._12 * other.x + self._22 * other.y
            )
        else:
            raise TypeError("Unsupported multiplication type")
    
        