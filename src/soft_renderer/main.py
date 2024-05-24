import pygame

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 500

def main():    

    pygame.init()

    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    pygame.display.set_caption("pygame test")

    clock = pygame.time.Clock()

    playing = True
    startx = 100

    while playing:
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                playing = False
                pygame.quit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print("왼쪽 키 눌림")
                    startx -= 1
                if event.key == pygame.K_RIGHT:
                    print("오른쪽 키 눌림")
                    startx += 1

                if event.key == pygame.K_UP:
                    print("위로 키 눌림")
                if event.key == pygame.K_DOWN:
                    print("아래로 키 눌림")

 
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
        pygame.draw.line(SCREEN, (255, 0, 0), (startx, 60), (startx + 100, 150), 5)
        
        # 키가 눌렸을 때


        pygame.display.flip()
        clock.tick(60)
        
if __name__ == '__main__':
    main()