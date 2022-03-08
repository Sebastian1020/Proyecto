from turtle import position
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

class Tecla(Button):
    def __init__(self, position = (0,0,0)):
        super().__init__(
            parent = scene,
            position = position,
            model = "sphere",
            origin_y = .5,
            texture = "grass",
            color = color.color(0,0, random.uniform(.9,1.0)),
            highlight_color = color.lime,
            
        )

#constructor y destructor de objetos
    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                tecla = Tecla(position = self.position + mouse.normal)
            if key == "right mouse down":
                destroy(self)        
    
#plano
for z in range(9):
    for x in range(8):
        tecla = Tecla(position = (x,0,z))   
        
player = FirstPersonController()


app.run()