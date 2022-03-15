from pickle import TRUE
from turtle import position
from ursina import *

class inventario(Entity):
    def __init__(self, position = (0,0)):
        super().__init__(
            #parent = camera.ui,
            scale = (7,6),
            parent = scene,
            position = position,
            model = "cube",
            texture = "white_cube"
        )
    def espacios():
        for x in range(3):
            for z in range(6):
                Button(scale=(.09,.09),origen_x=2, model="cube", color=color.white, position=(x,z), texture = "grass")
                
        

app = Ursina()
if held_keys["e"]==TRUE:
    Inven = inventario()
    
    


app.run()
