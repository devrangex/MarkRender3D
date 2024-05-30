import pygame
from renderer.dd.vector2 import Vector2
from renderer.renderer import Renderer
from renderer.dd.matrix3 import Matrix3
import numpy as np

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640



def main():    

    pygame.init()

    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    pygame.display.set_caption("pygame test")

    clock = pygame.time.Clock()

    playing = True
    fps = 60
    deltaTime = 0
    posx = 0
    posy = 0
    
    v1 = Vector2(0, 0)
    v2 = Vector2(10, 0)
    matRotation = Matrix3()
    deltaRot = 0
    #matRotation.set_rotaition()
    
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
        
        renderer.draw_grid(SCREEN, 64, 64)
        #renderer.put_pixel(SCREEN, (0, 255, 0), posx, posy)
        
        
        deltaRot += deltaTime
        matRotation.set_rotaition(deltaRot)
        v1 = matRotation * v1
        v2 = matRotation * v2
        renderer.scan_line_segment(SCREEN, int(v1.x), int(v1.y), (0, 0, 0), int(v2.x), int(v2.y), (255, 0, 0))

        pygame.display.flip()
        
        deltaTime = clock.tick(fps)/1000.0
        #clock.tick(60)
        
if __name__ == '__main__':
    main()