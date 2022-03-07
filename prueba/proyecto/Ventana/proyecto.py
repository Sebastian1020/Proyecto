from turtle import position
from ursina import *
from tkinter import  *
from ursina.prefabs.first_person_controller import FirstPersonController
# from Ventana.Ventana import pantalla
# from Ventana.Ventana import *

def pantalla():
    global Ventana
    Ventana = Tk()
    #Parametros de la ventana
    Ventana.geometry("350x650")
    Ventana.title("Ingresar datos de la habitación")
    Ventana.iconbitmap("Cat.ico")
    #imagen del logo
    image = PhotoImage(file = "Cat.gif")
    image = image.subsample(7,7)
    label =Label(image = image)
    label.pack()
    #letrero medidas
    Label(text="Medidas", bg="green", fg="white", width="300", height="3", font=("Arial", 15)).pack()
    Label(text="").pack()
    #campos
    global alto
    global ancho
    global largo 

    Label(Ventana, text="Alto").pack()
    alto=""
    caja1 = Entry(Ventana, textvariable=alto)
    caja1.pack()
    Label(Ventana).pack()

    Label(Ventana, text="Ancho").pack()
    ancho = ""
    caja2=Entry(Ventana, textvariable=ancho)
    caja2.pack()
    Label(Ventana).pack()

    Label(Ventana, text="Largo").pack()
    largo=""
    caja3=Entry(Ventana, textvariable=largo)
    caja3.pack()
    Label(Ventana).pack()

    def ejecutable(): 
        alto = int(caja1.get())
        ancho = int(caja2.get())
        largo = int(caja3.get())
        global app  
        #texturas pisos
        texturas = ["madera", "Piso_madera2", "baldosa"]

        #pedir la textura piso
        textura = "Piso_madera2"

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
                    collider = "box",
                    origin = Vec3(0,0,0)
                )
        class Techo(Entity):
            #atributos
            def __init__(self, position = (0,0,0)):
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
        
        app = Toplevel(Ventana)    
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

    Button(Ventana, text="Iniciar", height="3", width="20", bg="green", command=ejecutable).pack()
    Ventana.mainloop()
pantalla()