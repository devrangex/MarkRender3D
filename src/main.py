import pygame
from renderer.dd.vector2 import Vector2
import numpy as np

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640

class Basis:
    def __init__(self) -> None:
        self.axis1 = Vector2(1, 0)
        self.axis2 = Vector2(0, 1)
        
    def trasnform(self, input) -> Vector2:
        t0 = self.axis1 * input.x
        t1 = self.axis2 * input.y
        return Vector2(t0.x + t1.x, t0.y + t1.y)
        
class ScreenCoordinates:
    def __init__(self, width, height) -> None:
        
        pixelWidth = 10
        self.origin = np.array([width * 0.5, height * 0.5])        
        self.axis1 = Vector2(pixelWidth, 0)
        self.axis2 = Vector2(0, -pixelWidth)
        
    def trasnform(self, input) -> Vector2:
        t0 = self.axis1 * input.x
        t1 = self.axis2 * input.y
        return Vector2(t0.x + t1.x + self.origin[0], t0.y + t1.y + self.origin[1])
    
class Renderer:
    def __init__(self, width, height) -> None:
        self.basis = Basis()
        self.screenCoordinates = ScreenCoordinates(width, height)
        pass
    
    def update(self):
        pass
    
    def draw(self):
        pass
    
    def draw_line(self, SCREEN, color, p0, p1):
        
        v0 = self.basis.trasnform(p0)
        v1 = self.basis.trasnform(p1)
        
        v0 = self.screenCoordinates.trasnform(v0)
        v1 = self.screenCoordinates.trasnform(v1)
        
        pygame.draw.line(SCREEN, color, (v0.x, v0.y), (v1.x, v1.y))
    
    def put_pixel(self, SCREEN, color, x, y):
        v0 = Vector2(x, y)
        v1 = Vector2(x + 1, y + 1)
        
        v0 = self.basis.trasnform(v0)
        v1 = self.basis.trasnform(v1)
        
        v0 = self.screenCoordinates.trasnform(v0)
        v1 = self.screenCoordinates.trasnform(v1)
            
        pygame.draw.rect(SCREEN, color, [v0.x, v0.y, abs(v1.x - v0.x), abs(v1.y - v0.y)])
        
    def draw_grid(self, SCREEN, v, h):
        self.horizontal = h
        self.vertical = v
        
        for i in range(self.horizontal + 1):
            p0 = Vector2(-self.vertical * 0.5, 0) + Vector2(0, (i - self.horizontal * 0.5))
            p1 = Vector2(self.vertical * 0.5, 0) + Vector2(0, (i - self.horizontal * 0.5))    
            self.draw_line(SCREEN, (200, 200, 200), p0, p1)
            
        for i in range(self.vertical + 1):
            p0 = Vector2(i - self.vertical * 0.5, 0) + Vector2(0, - self.horizontal * 0.5)
            p1 = Vector2(i - self.vertical * 0.5, 0) + Vector2(0, self.horizontal * 0.5)   
            self.draw_line(SCREEN, (200, 200, 200), p0, p1)


def main():    

    pygame.init()

    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    pygame.display.set_caption("pygame test")

    clock = pygame.time.Clock()

    playing = True
    posx = 0
    posy = 0
    
    renderer = Renderer(SCREEN_WIDTH, SCREEN_HEIGHT)

    while playing:
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                playing = False
                pygame.quit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print("왼쪽 키 눌림")
                    posx -= 1
                if event.key == pygame.K_RIGHT:
                    print("오른쪽 키 눌림")
                    posx += 1

                if event.key == pygame.K_UP:
                    print("위로 키 눌림")
                    posy += 1
                if event.key == pygame.K_DOWN:
                    print("아래로 키 눌림")
                    posy -= 1

 
            # 키가 떼졌을 때
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    print("왼쪽 키 떼짐")
                if event.key == pygame.K_RIGHT:
                    print("오른쪽 키 떼짐")

                if event.key == pygame.K_UP:
                    print("위로 키 떼짐")
                if event.key == pygame.K_DOWN:
                    print("아래로 키 떼짐")
                
        SCREEN.fill((255, 255, 255))
        
        renderer.draw_grid(SCREEN, 10, 10)
        renderer.put_pixel(SCREEN, (0, 255, 0), posx, posy)
        renderer.draw_line(SCREEN, (255, 0, 0), Vector2(0, 0), Vector2(0, 5))
        renderer.draw_line(SCREEN, (0, 0, 255), Vector2(5, 0), Vector2(0, 0))
        # 키가 눌렸을 때


        pygame.display.flip()
        clock.tick(60)
        
if __name__ == '__main__':
    main()