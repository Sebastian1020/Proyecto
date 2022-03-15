from turtle import position
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
#pedir alto, ancho, largo
ancho = int(input("Digite el ancho de la habitación: \n"))
largo = int(input("Digite el largo de la habitación: \n"))
alto = int(input("Digite la altura de la habitación : \n"))
#texturas pisos
texturas = ["madera", "Piso_madera2", "baldosa"]
#pedir la textura piso
print("¿Qué textura desea?")
for i in texturas:
    print("     "+i)
textura = input("Textura del suelo: ")

#texturas techo
texturaTecho = "techo_negro"
#texturas paredes
texturaPared = "ladrilloBlanco"



class Suelo(Entity):
    #atributos
    def __init__(self, position = (0,-.2,0)):
        super().__init__(
            scale = (1,.2,1),
            parent = scene,
            position = position,
            model = "cube",
            texture = textura,
            collider = "box"
        )
class Techo(Entity):
    #atributos
    def __init__(self, position = (0,alto,0)):
        super().__init__(
            scale = (1,1,1),
            parent = scene,
            position = position,
            model = "cube",
            texture = texturaTecho,
            collider = "box"
        )

                
class Paredes(Entity):
    #atributos
    def __init__(self, position = (0,0,0)):
        super().__init__(
            scale = (1,1,1),
            parent = scene,
            position = position,
            model = "cube",
            texture = texturaPared,
            collider = "box"
        )
# class Inventory(Entity):
#     def __init__(self):
#         super().__init__(
#             parent = camera.ui,                                         
#             model = 'quad'                                       
#             )    
#         def input(self, key):
#             if self.hovered:
#                 if key == 'left mouse down':
#                     if __name__ == '__main__':
#                         inventory = Inventory()
                        
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
#Inventario
# Inventory()

#jugador
player = FirstPersonController(x=1,z=ancho/2)

app.run()




