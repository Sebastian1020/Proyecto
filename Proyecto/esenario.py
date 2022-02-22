from turtle import position
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

level = load_blender_scene('bedroom')


app.run()