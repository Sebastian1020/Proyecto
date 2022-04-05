from turtle import position
from ursina.mesh_importer import *
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()

piso = Entity(model= "cube", scale = (8,1,8), position=(0,2,0), collider = "box", color=color.brown)
class cocina(Entity):
    def __init__(self, **kwargs):
        super().__init__(
            parent = camera.ui,
            scale = (.3,.3,.3),
            model = "cube",
            color = color.white,
            rotation = (0,0,0),
            
        )
cocinaaa = cocina()
player = FirstPersonController()
app.run()