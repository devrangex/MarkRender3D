import pygame
import numpy as np
import math
from renderer.dd.vector2 import Vector2


# 기저 벡터 축으로 변환
class Basis:
    def __init__(self, basis1: Vector2 = Vector2(1, 0), basis2: Vector2 = Vector2(0, 1)) -> None:
        self.basis1 = basis1
        self.basis2 = basis2
        
    def trasnform(self, input) -> Vector2:
        # linear combination
        #
        # x * basis1 + y * basis2 = x'
        #
        t0 = self.basis1 * input.x
        t1 = self.basis2 * input.y
        return Vector2(t0.x + t1.x, t0.y + t1.y)
    
class Color:
    def __init__(self, r, g, b) -> None:
        self.rgb = np.array([r, g, b])
        
    @property
    def r(self):
        return self.rgb[0]
    
    @property
    def g(self):
        return self.rgb[1]
    
    @property
    def b(self):
        return self.rgb[2]   
    
    def __add__(self, right):        
        return Color(self.r + right.r, self.g + right.g, self.b + right.b)
    
    def __sub__(self, right):
        return Color(self.r - right.r, self.g - right.g, self.b - right.b)
    
    def __mul__(self, scalar):
        return Color(self.r * scalar, self.g * scalar, self.b * scalar)

# 스크린 좌표계로 변환      
class ScreenCoordinates:
    def __init__(self, axis1: Vector2, axis2: Vector2, origin: Vector2) -> None:
        
        #pixelWidth = 10
        #self.origin = np.array([width * 0.5, height * 0.5])
        #self.axis1 = Vector2(pixelWidth, 0)
        #self.axis2 = Vector2(0, -pixelWidth)
        self.axis1 = axis1
        self.axis2 = axis2
        self.origin = origin
        
    def trasnform(self, input) -> Vector2:
        t0 = self.axis1 * input.x
        t1 = self.axis2 * input.y
        return Vector2(t0.x + t1.x + self.origin.x, t0.y + t1.y + self.origin.y)

# 렌더러 클래스
class Renderer:
    def __init__(self, width, height) -> None:
        self.basis = Basis()
        # 픽셀 크기 10
        pixelSize = 10        
        # 좌상단이 0, 0
        self.screenCoordinates = ScreenCoordinates(Vector2(pixelSize, 0), Vector2(0, -pixelSize), Vector2(width * 0.5, height * 0.5))
        pass
    
    def update(self):
        pass
    
    def draw(self):
        pass
    
    def draw_line(self, surface, color, p0, p1):
        
        v0 = self.basis.trasnform(p0)
        v1 = self.basis.trasnform(p1)
        
        v0 = self.screenCoordinates.trasnform(v0)
        v1 = self.screenCoordinates.trasnform(v1)
        
        pygame.draw.line(surface, color, (v0.x, v0.y), (v1.x, v1.y))
    
    def put_pixel(self, surface, color, x, y):
        v0 = Vector2(x, y)
        v1 = Vector2(x + 1, y + 1)
        
        v0 = self.basis.trasnform(v0)
        v1 = self.basis.trasnform(v1)
        
        v0 = self.screenCoordinates.trasnform(v0)
        v1 = self.screenCoordinates.trasnform(v1)
            
        pygame.draw.rect(surface, color, [v0.x, v0.y, abs(v1.x - v0.x), abs(v1.y - v0.y)])
        
    def draw_grid(self, surface, v, h):
        self.horizontal = h
        self.vertical = v
        
        for i in range(self.horizontal + 1):
            p0 = Vector2(-self.vertical * 0.5, 0) + Vector2(0, (i - self.horizontal * 0.5))
            p1 = Vector2(self.vertical * 0.5, 0) + Vector2(0, (i - self.horizontal * 0.5))    
            self.draw_line(surface, (200, 200, 200), p0, p1)
            
        for i in range(self.vertical + 1):
            p0 = Vector2(i - self.vertical * 0.5, 0) + Vector2(0, - self.horizontal * 0.5)
            p1 = Vector2(i - self.vertical * 0.5, 0) + Vector2(0, self.horizontal * 0.5)   
            self.draw_line(surface, (200, 200, 200), p0, p1)
            
        self.draw_line(surface, (255, 0, 0), Vector2(0, 0), Vector2(0, 5))
        self.draw_line(surface, (0, 0, 255), Vector2(5, 0), Vector2(0, 0))
    
    def scan_line_segment(self, surface, x1, y1, c1, x2, y2, c2):
        swap_xy = False
        flip_y = False
        
        # always scan convert from left to right
        if x1 > x2:
            x1, x2 = x2, x1
        
        # always scan convert from down to up
        # 4 > 3
        # -4, -3
        flip_y = y1 > y2
        if flip_y:
            y1, y2 = -y1, -y2            
        
        swap_xy = (y2 - y1) > (x2 - x1)
        if swap_xy:
            x1, y1 = y1, x1
            x2, y2 = y2, x2
            
        # 수평 라인
        horizontal = y1 == y2
        # 대각선
        diagonal = (y2 - y1) == (x2 - x1)
        # 정규화
        scale = 1 / (x2 - x1)
        
        color = Color(c1[0], c1[1], c1[2])
        color1 = Color(c1[0], c1[1], c1[2])
        color2 = Color(c2[0], c2[1], c2[2])
        
        col_step = (color2 - color1) * scale * 0.99999
        
        y = y1
        yy = float(y1)
        y_step = float(y2 - y1) * scale
        
        for x in range(x1, x2 + 1):
            X = int(x)
            Y = int(y)
            if swap_xy:
                X, Y = Y, X
                
            if flip_y:
                Y = -Y
                
            self.put_pixel(surface, (color.r, color.g, color.b), X, Y)
            
            if horizontal == False:
                if diagonal:
                    y += 1
                else:
                    yy += y_step
                    y = int(round(yy))
                    
            color += col_step
        
        