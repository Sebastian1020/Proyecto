from turtle import delay, position 
from ursina import *

app = Ursina()
player = Entity(model="cube", color=color.white, Scale = (4,4), position = (0,0))
def update():
    
    player.x += held_keys["d"] * time.dt
    player.x -= held_keys["a"] * time.dt 
    player.y += held_keys["w"] * time.dt 
    player.y -= held_keys["s"] * time.dt
    player.z += held_keys["q"] * time.dt  
    player.z -= held_keys["e"] * time.dt 
    
def input(key):

    if key == "space":
        player.y += 1
        invoke(setattr, player, "y", player.y-1, delay=.25)
        
app.run()
