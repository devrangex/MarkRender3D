from mathmatic.vector2 import Vector2
from geometry.basis import Basis
from geometry.screencoordinator import ScreenCoordinator

class Renderer:
    def __init__(self, width, height, pixel_size = 1) -> None:
        # 축
        self.basis = Basis()
        
        # 픽셀 사이즈 정하기
        self.pixelSize = pixel_size        
        # 좌상단 0, 0이 되도록 이동
        self.screenCoordinates = ScreenCoordinator(Vector2(self.pixelSize, 0), 
                                                   Vector2(0, -self.pixelSize), 
                                                   Vector2(width, height))
        
    def put_pixel(self, surface, color, x, y):
        v0 = Vector2(x, y)
        v1 = Vector2(x + 1, y + 1)
        
        v0 = self.basis.trasnform(v0)
        v1 = self.basis.trasnform(v1)
        
        v0 = self.screenCoordinates.trasnform(v0)
        v1 = self.screenCoordinates.trasnform(v1)
        
        pw, ph = abs(v1.x - v0.x), abs(v1.y - v0.y)            
        #pygame.draw.rect(surface, color, [v0.x, v0.y - ph, pw, ph])
        
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