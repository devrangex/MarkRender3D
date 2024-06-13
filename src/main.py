import pygame
import pygame.freetype
from renderer.dd.vector2 import Vector2
from renderer.renderer import Renderer
from renderer.dd.matrix3 import Matrix3
from renderer.dd.matrix44 import Matrix44
from renderer.cube import Cube

import numpy as np

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640

def main():    

    pygame.init()

    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    

    pygame.display.set_caption("pygame test")
    pygame.font.init()
    #myfont = pygame.freetype.Font('Comic Sans MS', 30)
    
    #screen = pygame.display.set_mode((640, 480))
    font = pygame.font.Font(pygame.font.get_default_font(), 36)


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
    
    mat1 = Matrix44()
    mat2 = Matrix44()
    
    mat2.set_rotaitionZByDeg(45)    
    mat3 = mat1 * mat2
    
    cube = Cube()
    
    while playing:
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                playing = False
                pygame.quit()
                break
                
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
                
        deltaTime = clock.tick(fps)/1000.0
        
        SCREEN.fill((255, 255, 255))
        
        renderer.draw_grid(SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT)
        #renderer.put_pixel(SCREEN, (0, 255, 0), posx, posy)
        
        
        deltaRot += deltaTime * 45
        matRotation.set_rotaition(deltaRot)
        mv1 = matRotation * v1
        mv2 = matRotation * v2
        renderer.scan_line_segment(SCREEN, int(mv1.x), int(mv1.y), (0, 0, 0), int(mv2.x), int(mv2.y), (255, 0, 0))
        
        vv1 = Vector2(20, 20)
        vv2 = Vector2(-10, 10)
        vv3 = Vector2(10, -20)
        
        vv1 = matRotation * vv1
        vv2 = matRotation * vv2
        vv3 = matRotation * vv3
        
        renderer.fill_triangle(SCREEN, int(vv1.x), int(vv1.y), (255, 0, 0), 
                                        int(vv2.x), int(vv2.y), (0, 255, 0),
                                        int(vv3.x), int(vv3.y), (0, 0, 255))
        
        
        cube.update(deltaTime)
        cube.draw(SCREEN, renderer)
        #renderer.draw_indexed_primitive_line_strip(SCREEN, cube.index_buffer, 12, cube.vertex_buffer)
        
        
        #scaned = []
        #renderer.scan_line_segment(SCREEN, int(mv1.x), int(mv1.y), (0, 0, 0), int(mv2.x), int(mv2.y), (255, 0, 0), scaned)
        
        
        
        
        
        #myfont.render_to(SCREEN, (40, 350), "Hello World!", (0, 0, 0))
        text_surface = font.render(str(deltaTime), True, (0, 0, 0))
        SCREEN.blit(text_surface, dest=(0,0))
        
        text_surface = font.render(str(deltaRot), True, (0, 0, 0))
        SCREEN.blit(text_surface, dest=(0,50))
        
        #myfont.render(str(deltaTime), False, (0, 0, 0))
        #SCREEN.
        #clock.tick(60)
        pygame.display.flip()
        
if __name__ == '__main__':
    main()