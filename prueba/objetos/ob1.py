from email.mime import image
from tkinter import Scale
from turtle import position
from ursina import *
from PIL import Image

class ob1(Entity):
    def __init__(self, position=(0,0,0)):
        super().__init__(
            model = "sphere",
            scale = (5,5,5),
            parent = scene,
            texture = "im1.jpg",
        )
        
    def update(self):
        
            self.rotation_x += 40*held_keys["d"]*time.dt 
            self.rotation_y += 40*held_keys["s"]*time.dt 
            self.rotation_z += 40*held_keys["a"]*time.dt 
            

