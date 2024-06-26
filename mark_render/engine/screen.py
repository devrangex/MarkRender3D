import pygame
from pygame._sdl2 import Window, Texture, Image, Renderer, get_drivers, messagebox

from cameraobject import CameraObject
from engine.renderobject import RenderObject

class Screen:
    
    def __init__(self, name, width, height, pixel_size = 1, bg_color=(0, 0, 0, 255)) -> None:        
        self.window = Window(name, size=(width, height), resizable=False)
        self.renderer = Renderer(self.window)
        self.bg_color = bg_color
        self.renderer.draw_color = bg_color
        
        self.camera = CameraObject()
        self.renderer = RenderObject(self.renderer, width, height, pixel_size)
        
    def update(self):
        pass
    
    
    def render(self):
        self.renderer.clear()
        
        self.renderer.draw_color = (255, 255, 255, 255)
        self.renderer.draw_line((0, 0), (64, 64))
        self.renderer.draw_line((64, 64), (128, 0))
        self.renderer.draw_point((72, 32))
        self.renderer.draw_rect(pygame.Rect(0, 64, 64, 64))
        self.renderer.fill_rect(pygame.Rect(0, 128, 64, 64))
        self.renderer.draw_color = self.bg_color
        
        self.renderer.present()
        
    def set_window_title(self, s):
        self.window.title = str(f"FPS: {s}")