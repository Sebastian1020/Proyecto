from tokenize import PlainToken
from turtle import position
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

class Cubo(Button):
    #atributos
    def __init__(self, position = (0,0,0)):
        super().__init__(
            parent = scene,
            position = position,
            model = "cube",
            texture = "borde",
            color = color.white,
            highlight_color = color.lime,  
        )
    #crear
    def input(self, key):
            if self.hovered:
                if key == "left mouse down":
                    cubo = Cubo(position = self.position + mouse.normal)
class Cubo2(Button):
    #atributos
    def __init__(self, position = (0,0,0)):
        super().__init__(
            parent = scene,
            position = position,
            model = "cube",
            color = color.white,
            highlight_color = color.lime, 
        )
    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                cubo = Cubo(position = self.position + mouse.normal)

def cuadro():
    for z in range(34):
        for x in range(34):
            cubo = Cubo2(position = (x,0,z))
     #paredes de exterior   
        for y in range(6):       
            cubo1 = Cubo(position = (x,y,z))
            cubo1 = Cubo(position = (z,y,x))
            cubo1 = Cubo(position = (z,y,0))
            cubo1 = Cubo(position = (0,y,z))
def filas():
    for z in range(3):
        for y in range(6):
            #fila 1
            pared1 = Cubo(position = (3,y,z+1))
            pared1 = Cubo(position = (3,y,z+6))
            pared1 = Cubo(position = (3,y,z+7))
            pared1 = Cubo(position = (3,y,z+12))
            pared1 = Cubo(position = (3,y,z+15))
            pared1 = Cubo(position = (3,y,z+16))
            pared1 = Cubo(position = (3,y,z+28))
            pared1 = Cubo(position = (3,y,z+27))
            pared1 = Cubo(position = (3,y,z+24))
            # #fila 2
            pared1 = Cubo(position = (6,y,z+3))
            pared1 = Cubo(position = (6,y,z+4))
            pared1 = Cubo(position = (6,y,z+9))
            pared1 = Cubo(position = (6,y,z+10))
            pared1 = Cubo(position = (6,y,z+18))
            pared1 = Cubo(position = (6,y,z+19))
            pared1 = Cubo(position = (6,y,z+22))
            pared1 = Cubo(position = (6,y,z+25))
            pared1 = Cubo(position = (6,y,z+27))
            pared1 = Cubo(position = (6,y,z+30))
            # #fila 3
            pared1 = Cubo(position = (9,y,z+1))
            pared1 = Cubo(position = (9,y,z+15))
            pared1 = Cubo(position = (9,y,z+17))
            pared1 = Cubo(position = (9,y,z+20))
            pared1 = Cubo(position = (9,y,z+23))
            pared1 = Cubo(position = (9,y,z+26))
            pared1 = Cubo(position = (9,y,z+28))
            # #fila 4
            pared1 = Cubo(position = (12,y,z+3))
            pared1 = Cubo(position = (12,y,z+4))
            pared1 = Cubo(position = (12,y,z+12))
            pared1 = Cubo(position = (12,y,z+13))
            pared1 = Cubo(position = (12,y,z+21))
            pared1 = Cubo(position = (12,y,z+22))
            pared1 = Cubo(position = (12,y,z+27))
            pared1 = Cubo(position = (12,y,z+28))
            #fila 5
            pared1 = Cubo(position = (15,y,z+3))
            pared1 = Cubo(position = (15,y,z+6))
            pared1 = Cubo(position = (15,y,z+7))
            pared1 = Cubo(position = (15,y,z+24))
            pared1 = Cubo(position = (15,y,z+25))
            #fila 6
            pared1 = Cubo(position = (18,y,z+3))
            pared1 = Cubo(position = (18,y,z+4))
            pared1 = Cubo(position = (18,y,z+9))
            pared1 = Cubo(position = (18,y,z+10))
            pared1 = Cubo(position = (18,y,z+21))
            pared1 = Cubo(position = (18,y,z+22))
            pared1 = Cubo(position = (18,y,z+27))
            pared1 = Cubo(position = (18,y,z+28))
            #fila 7
            pared1 = Cubo(position = (21,y,z))
            pared1 = Cubo(position = (21,y,z+3))
            pared1 = Cubo(position = (21,y,z+6))
            pared1 = Cubo(position = (21,y,z+7))
            pared1 = Cubo(position = (21,y,z+12))
            pared1 = Cubo(position = (21,y,z+13))
            pared1 = Cubo(position = (21,y,z+24))
            pared1 = Cubo(position = (21,y,z+25))
            #fila 8
            pared1 = Cubo(position = (24,y,z+9))
            pared1 = Cubo(position = (24,y,z+10))
            pared1 = Cubo(position = (24,y,z+15))
            pared1 = Cubo(position = (24,y,z+16))
            pared1 = Cubo(position = (24,y,z+27))
            pared1 = Cubo(position = (24,y,z+30))
            #fila 9
            pared1 = Cubo(position = (27,y,z+6))
            pared1 = Cubo(position = (27,y,z+9))
            pared1 = Cubo(position = (27,y,z+10))
            pared1 = Cubo(position = (27,y,z+15))
            pared1 = Cubo(position = (27,y,z+18))
            pared1 = Cubo(position = (27,y,z+19))
            pared1 = Cubo(position = (27,y,z+24))
            pared1 = Cubo(position = (27,y,z+25))
            #fila 10
            pared1 = Cubo(position = (30,y,z))
            pared1 = Cubo(position = (30,y,z+1))
            pared1 = Cubo(position = (30,y,z+12))
            pared1 = Cubo(position = (30,y,z+13))
            pared1 = Cubo(position = (30,y,z+21))
            pared1 = Cubo(position = (30,y,z+22))
def columnas():
    for x in range(4):
        for y in range(6):
            #columna 1
            pared2 = Cubo(position = (x+15,y,3))
            pared2 = Cubo(position = (x+24,y,3))
            pared2 = Cubo(position = (x+27,y,3))
            #columna 2
            pared2 = Cubo(position = (x+3,y,6))
            pared2 = Cubo(position = (x+7,y,6))
            pared2 = Cubo(position = (x+8,y,6))
            pared2 = Cubo(position = (x+21,y,6))
            pared2 = Cubo(position = (x+25,y,6))
            pared2 = Cubo(position = (x+27,y,6))
            #columna 3
            pared2 = Cubo(position = (x,y,9))
            pared2 = Cubo(position = (x+6,y,9))
            pared2 = Cubo(position = (x+10,y,9))
            pared2 = Cubo(position = (x+12,y,9))
            pared2 = Cubo(position = (x+18,y,9))
            pared2 = Cubo(position = (x+30,y,9))
            #colimna 4
            pared2 = Cubo(position = (x+3,y,12))
            pared2 = Cubo(position = (x+9,y,12))
            pared2 = Cubo(position = (x+13,y,12))
            pared2 = Cubo(position = (x+15,y,12))
            pared2 = Cubo(position = (x+21,y,12))
            pared2 = Cubo(position = (x+27,y,12))
            #Columna 5
            pared2 = Cubo(position = (x+3,y,15))
            pared2 = Cubo(position = (x+6,y,15))
            pared2 = Cubo(position = (x+12,y,15))
            pared2 = Cubo(position = (x+16,y,15))
            pared2 = Cubo(position = (x+18,y,15))
            pared2 = Cubo(position = (x+27,y,15))
            #columna 6
            pared2 = Cubo(position = (x+9,y,18))
            pared2 = Cubo(position = (x+13,y,18))
            pared2 = Cubo(position = (x+17,y,18))
            pared2 = Cubo(position = (x+21,y,18))
            pared2 = Cubo(position = (x+30,y,18))
            #columna 7
            pared2 = Cubo(position = (x+3,y,21))
            pared2 = Cubo(position = (x+12,y,21)) 
            pared2 = Cubo(position = (x+16,y,21))
            pared2 = Cubo(position = (x+20,y,21))
            pared2 = Cubo(position = (x+24,y,21))
            pared2 = Cubo(position = (x+26,y,21))
            #columna 8
            pared2 = Cubo(position = (x,y,24))
            pared2 = Cubo(position = (x+15,y,24))
            pared2 = Cubo(position = (x+21,y,24))
            pared2 = Cubo(position = (x+24,y,24))
            #columna 9
            pared2 = Cubo(position = (x+12,y,27))
            pared2 = Cubo(position = (x+18,y,27))
            #columna 10
            pared2 = Cubo(position = (x+9,y,30))
            pared2 = Cubo(position = (x+15,y,30))
            pared2 = Cubo(position = (x+18,y,30))
            pared2 = Cubo(position = (x+24,y,30))
            pared2 = Cubo(position = (x+27,y,30))
    
    
app = Ursina()
#plano
plano = cuadro()
fila = filas()
colomna = columnas() 


        
meta = Entity(model = "sphere", scale = (2,2,2), position = (29,3,1.5), color = color.green)
        
player = FirstPersonController(position = (1,0,1))

app.run()