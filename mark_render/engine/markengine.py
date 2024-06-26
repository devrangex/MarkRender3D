import pygame
import pygame.freetype
from pygame._sdl2 import Window, Texture, Image, Renderer, get_drivers, messagebox
from engine.screen import Screen

class MarkEngine:
    
    def __init__(self, width, height) -> None:                
        self.width = width
        self.height = height
        self.fps = 60
        self.deltaTime = 0
        self.accumTime = 0
        
    def init(self):
        
        pygame.display.init()
        pygame.key.set_repeat(1000, 10)
        pygame.display.set_caption("Mark Render 3D")
        
        self.clock = pygame.time.Clock()
        
        for driver in get_drivers():
            print(driver)
        
        # self.win = Window("asdf", resizable=True)
        # self.renderer = Renderer(self.win)
        
        # self.backgrounds = [(255, 0, 0, 255), (0, 255, 0, 255), (0, 0, 255, 255)]
        # self.bg_index = 0
        # self.renderer.draw_color = self.backgrounds[self.bg_index]

        # self.win2 = Window("2nd window", size=(256, 256), always_on_top=True)
        # self.win2.opacity = 0.5
        # #self.win2.set_icon(load_img("bomb.gif"))
        # self.renderer2 = Renderer(self.win2)
        # #tex2 = Texture.from_surface(renderer2, load_img("asprite.bmp"))
        # self.renderer2.clear()
        # #tex2.draw()
        # self.renderer2.present()

        # pygame.font.init()        
        # self.font = pygame.font.Font(pygame.font.get_default_font(), 24)
        
        # self.clock = pygame.time.Clock()
        # self.screen = pygame.display.set_mode((self.width, self.height))
        # self.screen2 = pygame.display.set_mode((self.width, self.height), display=1)
        
        self.screen = Screen('screen', 800, 600)
        self.screen2 = Screen('screen2', 800, 600)
        
        self.running = True        
    
    def shutdown(self):
        pygame.quit()
    
    def loop(self):
        self.init()
        
        while self.running:
            
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            self.update()
            self.render()
            
            #self.deltaTime = self.clock.tick(self.fps)/1000.0
            #self.accumTime += self.deltaTime
        
        self.shutdown()
    
    def update(self):
        pass
    
    def render(self):
        self.screen.render()
        self.screen2.render()
        # self.renderer.clear()
        
        # self.renderer.draw_color = (255, 255, 255, 255)
        # self.renderer.draw_line((0, 0), (64, 64))
        # self.renderer.draw_line((64, 64), (128, 0))
        # self.renderer.draw_point((72, 32))
        # self.renderer.draw_rect(pygame.Rect(0, 64, 64, 64))
        # self.renderer.fill_rect(pygame.Rect(0, 128, 64, 64))
        # self.renderer.draw_color = self.backgrounds[self.bg_index]
        
        # self.renderer.present()

        self.clock.tick(60)
        self.screen.set_window_title(self.clock.get_fps())
        #self.win.title = str(f"FPS: {self.clock.get_fps()}")
        #self.screen.fill((255, 255, 255))
        
        #text_surface = self.font.render(str(self.accumTime), True, (0, 0, 0))
        #self.screen.blit(text_surface, dest=(0,0))
        
        #pygame.display.flip()