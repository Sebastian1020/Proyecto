from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

ancho = 10
largo = 10
alto = 8  
#parametros suelo
class Suelo(Entity):
    #atributos
    def __init__(self, position = (0,-.2,0)):
        super().__init__(
            scale = (1,.2,1),
            parent = scene,
            position = position,
            model = "cube",
            texture = "madera",
            collider = "box",
            origin = Vec3(0,0,0),
            # color = str(ColorP.get())
        )
#parametros techo
class Techo(Entity):
    #atributos
    def __init__(self, position = (0,0,0)):
        super().__init__(
            scale = (1,1,1),
            parent = scene,
            position = position,
            model = "cube",
            texture = "techo_negro",
            collider = "box",
            # color = str(ColorT.get()) 
        ) 
#parametros Paredes    
class Paredes(Entity):
    #atributos
    def __init__(self, position = (0,0,0)):
        super().__init__(
            scale = (1,1,1),
            parent = scene,
            position = position,
            model = "cube",
            texture = "ladrilloBlanco",
            collider = "box",
            # color = str(ColorPa.get())
        )

class Inventory(Entity):
    def __init__(self, **kwargs):
        super().__init__(
            parent = camera.ui,
            model = Quad(radius=.1),
            texture = 'white_cube',
            texture_scale = (5,7),
            scale = (.6, .8),
            origin = (-.5, .5),
            position = (-.3,.4),
            color = color.color(0,0,.1,.9),
            visible = True,
            )
        
#app=Toplevel(Ventana2)
#seguir despues de Ventana2    
app = Ursina()
#suelo y techo
for z in range(ancho):
        for x in range(largo):
            suelo = Suelo(position = (x,0,z))
            techo = Techo(position = (x,alto,z))
#Paredes izquierda y derecha
        for y in range(alto):       
            paredIz = Paredes(position = (0,y,z))           
            paredDer = Paredes(position = (largo,y,z))
#Paredes delante y atras
for x in range(largo):
    for y in range(alto):
        paredAt = Paredes(position = (x,y,0))
        paredDel = Paredes(position = (x,y,ancho))
def input(Key):
    global inven
    if Key == "e":
        inven = Inventory()
    if Key == "q":
        destroy(inven)



                
            
player = FirstPersonController(x=1,z=ancho/2)
app.run()

