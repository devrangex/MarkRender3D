import pygame
import numpy as np
import math
from renderer.dd.vector2 import Vector2
from renderer.dd.matrix44 import Matrix44


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
        
        # projection
        self.near = 5
        self.far = 1000
        self.fov = 60
        self.width = width
        self.height = height
        self.matProj = Matrix44()
        self.matProj.set_projection(self.near, self.far, self.fov, self.width, self.height)
        
        
        # 픽셀 크기 10
        pixelSize = 5
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
        
        pw, ph = abs(v1.x - v0.x), abs(v1.y - v0.y)            
        pygame.draw.rect(surface, color, [v0.x, v0.y - ph, pw, ph])
        
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
            
        self.draw_line(surface, (255, 0, 0), Vector2(0, 0), Vector2(0, 50))
        self.draw_line(surface, (0, 0, 255), Vector2(50, 0), Vector2(0, 0))
    
    def scan_line_segment(self, surface, x1, y1, c1, x2, y2, c2, scaned = None):
        swap_xy = False
        flip_y = False
        
        # 항상 좌측에서 우측으로 값이 커질수 있도록
        # x1 보다 x2가 큰 경우 모든 값을 swap 한다.
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
            c1, c2 = c2, c1
        
        # 아래에서 위로 그려야 하기때문에
        # y1이 y2보다 크다면 부호를 바꿔서
        # y1이 y2보다 작게 한다.
        # 4 > 3
        # (4, 3) => (-4, -3)
        flip_y = y1 > y2
        if flip_y:
            y1, y2 = -y1, -y2            
        
        swap_xy = (y2 - y1) > (x2 - x1)
        if swap_xy:
            x1, y1 = y1, x1
            x2, y2 = y2, x2
            
        # 수평으로 그려진다.
        horizontal = y1 == y2
        # 기울기를 계산해 대각선인지 체크
        diagonal = (y2 - y1) == (x2 - x1)        
        
        # 전체 길이를 정규화시킨다.
        b = (x2 - x1)
        if b == 0:
            b = 1
        scale = 1 / b
        
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
            
            if scaned is None:
                self.put_pixel(surface, (color.r, color.g, color.b), X, Y)
            else:
                scaned.append((X, Y, (color.r, color.g, color.b)))
            
            if horizontal == False:
                if diagonal:
                    y += 1
                else:
                    yy += y_step
                    y = int(round(yy))
                    
            color += col_step
            
    def fill_triangle(self, surface, x1, y1, c1, x2, y2, c2, x3, y3, c3):
        scanned_pnts = []
        
        # 외각 라인을 스캔히 배열에 넣는다.
        self.scan_line_segment(surface, x1, y1, c1, x2, y2, c2, scanned_pnts)
        self.scan_line_segment(surface, x2, y2, c2, x3, y3, c3, scanned_pnts)
        self.scan_line_segment(surface, x3, y3, c3, x1, y1, c1, scanned_pnts)
        
        # 점들을 y값과 x값의 크기순으로 정렬한다.
        sorted_scaned = sorted(scanned_pnts, key=lambda x: (x[1], x[0]))        
        
        cur_yval = math.inf
        same_yval = []
        
        # 정렬된 픽셀들을 순서대로 가져온다.
        for p in sorted_scaned:            
            y = p[1]
            # y값이 변경된 경우
            if cur_yval != y:
                # 픽셀이 하나 이상 존재하는 경우
                if len(same_yval) > 0:
                    # 라인글 그린다.
                    begin = same_yval[0]
                    end = same_yval[-1]
                    self.scan_line_segment(surface, begin[0], begin[1], begin[2], end[0], end[1], end[2])
                    
                    same_yval.clear()
            
                # 현재 y값 넣어주고
                cur_yval = y
            
            # 같은 y값을 같은 픽셀들을 계속 추가해준다.
            same_yval.append(p)
        
        # 마지막 같은 y위치의 픽셀을 그려준다.
        if len(same_yval) > 0:
            begin = same_yval[0]
            end = same_yval[-1]
            self.scan_line_segment(surface, begin[0], begin[1], begin[2], end[0], end[1], end[2])
            


        