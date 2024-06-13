import tkinter as tk
from renderer.dd.vector3 import Vector3
from renderer.dd.matrix44 import Matrix44

class GameObject:
    
    def __init__(self) -> None:
        self.position = Vector3()
        self.scale = Vector3()
        self.rotation = Vector3()
        
        self.localMatrix = Matrix44()
        
    def update(self):
        pass
        
    def get_position(self):
        return self.position
    
    def get_local_matrix():
        pass