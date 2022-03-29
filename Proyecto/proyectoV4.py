from tkinter import *
from tkinter import  ttk
from tkinter.ttk import Combobox
from tokenize import Double

def pantalla():
    global Ventana, alto, ancho, largo, caja3, caja1, caja2
    Ventana = Tk()
#Parametros de la ventana
    Ventana.geometry("350x650")
    Ventana.title("Ingresar datos de la habitación")
    Ventana.iconbitmap("Imagenes\Cat.ico")
    Ventana.configure(bg="sky blue")
#imagen del logo
    image = PhotoImage(file = "Imagenes\Imgportada.gif")
    image = image.subsample(2,2)
    label =Label(image = image)
    label.pack()
#letrero medidas
    Label(text="Medidas", bg="green", fg="white", width="300", height="3", font=("Arial Black", 15)).pack()
    Label(text="", bg="sky blue").pack()
#campos ventana
#Alto
    Label(Ventana, text="Alto:", bg="sky blue", font=("Arial Black",10)).pack()
    alto=""
    caja1 = Entry(Ventana, textvariable=alto, width=20, font=("Arial",12), bg="light sky blue",
                justify="center",  fg="black",highlightbackground="green2", highlightcolor="green", highlightthickness=3)
    caja1.pack()
    Label(Ventana, bg="sky blue").pack()
#Ancho
    Label(Ventana, text="Ancho:", bg="sky blue", font=("Arial Black",10)).pack()
    ancho = ""
    caja2=Entry(Ventana, textvariable=ancho, width=20, font=("Arial",12), bg="light sky blue",
                justify="center",  fg="black",highlightbackground="green2", highlightcolor="green", highlightthickness=3)
    caja2.pack()
    Label(Ventana, bg="sky blue").pack()
#Largo
    Label(Ventana, text="Largo:", bg="sky blue", font=("Arial Black",10)).pack()
    largo=""
    caja3=Entry(Ventana, textvariable=largo, width=20, font=("Arial",12), bg="light sky blue",
                justify="center",  fg="black",highlightbackground="green2", highlightcolor="green", highlightthickness=3)
    caja3.pack()
    Label(Ventana, bg="sky blue").pack()
    
    boton1 = Button(Ventana, text="Siguente", height="3", width="20", bg="green", command=pantalla2).pack()
    Ventana.mainloop()

def pantalla2():
    global Ventana2, texturasP, alto, ancho, largo, texturasT, texturasPa, ColorP, ColorPa, ColorT
    Ventana2 = Toplevel()
    texturasP=StringVar()
    texturasPa=StringVar()
    texturasT=StringVar()
    ColorP = StringVar()
    ColorPa = StringVar()
    ColorT = StringVar()
#Parametros de la ventana
    Ventana2.geometry("450x650")
    Ventana2.title("Ingresar datos de la habitación")
    Ventana2.iconbitmap("Imagenes\Cat.ico")
    Ventana2.configure(bg="sky blue")
#imagen del logo
    imagen2 = PhotoImage(file = "Imagenes\habitacion.gif").subsample(2,2)
    label2 = Label(Ventana2, image = imagen2)
    label2.pack()
#letrero medidas
    letreroT2 = Label(Ventana2, text="Texturas", bg="brown", fg="white", width="300", height="3", font=("Arial Black", 15)).pack()
#campo Texturas y color pisos
    letreroS4 = Label(Ventana2, text="Textura piso:", bg="sky blue", font=("Arial Black",10)).place(x=60, y= 400)
    texturasPisos = ttk.Combobox(Ventana2,  state="readonly", textvariable=texturasP)
    texturasPisos["values"] = ("madera", "Piso_madera2", "baldosa")
    texturasPisos.place(x=50, y= 430)
    letreroS4 = Label(Ventana2, text="Color piso:", bg="sky blue", font=("Arial Black",10)).place(x=290, y= 400)
    caja4= Entry(Ventana2, width=20, textvariable=ColorP).place(x=280, y= 430)
#campo texturas techo
    letreroS5 = Label(Ventana2, text="Textura techo:", bg="sky blue", font=("Arial Black",10)).place(x=60, y= 460)
    texturasTecho = ttk.Combobox(Ventana2,  state="readonly", textvariable=texturasT)
    texturasTecho["values"] = ("techo_negro")
    texturasTecho.place(x=50, y= 490)
    #color
    letreroS6 = Label(Ventana2, text="Color techo:", bg="sky blue", font=("Arial Black",10)).place(x=290, y= 460)
    caja4= Entry(Ventana2, width=20, textvariable=ColorT).place(x=280, y= 490)
#campo tecturas paredes
    letreroS5 = Label(Ventana2, text="Textura paredes:", bg="sky blue", font=("Arial Black",10)).place(x=60, y= 520)
    texturasParedes = ttk.Combobox(Ventana2,  state="readonly", textvariable=texturasPa)
    texturasParedes["values"] = ("ladrilloBlanco")
    texturasParedes.place(x=50, y= 550)
    letreroS5 = Label(Ventana2, text="Color paredes:", bg="sky blue", font=("Arial Black",10)).place(x=290, y= 520)
    cajas= Entry(Ventana2, width=20, textvariable=ColorPa).place(x=280, y= 550)
#variables importantes a enteros
    alto = int(caja1.get())
    ancho = int(caja2.get())
    largo = int(caja3.get())
    boton2 = Button(Ventana2, text="Iniciar", height="3", width="20", bg="brown", command=ejecutable).place(x=170, y= 590)
    Ventana2.mainloop()
    

from ursina import scene, Vec3, Entity, Ursina, destroy, camera, Quad, color
from ursina.input_handler import held_keys, Keys
from ursina.prefabs.first_person_controller import FirstPersonController 
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
def input(Key):
    global inven
    if Key == "e":
        inven = Inventory()
    if Key == "q":
        destroy(inven)
def ejecutable(Key): 
        global app  
    #parametros suelo
        class Suelo(Entity):
            #atributos
            def __init__(self, position = (0,-.2,0)):
                super().__init__(
                    scale = (1,.2,1),
                    parent = scene,
                    position = position,
                    model = "cube",
                    texture = str(texturasP.get()),
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
                    texture = str(texturasT.get()),
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
                    texture = str(texturasPa.get()),
                    collider = "box",
                    # color = str(ColorPa.get())
                )
        
        app=Toplevel(Ventana2)
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

        input()


        player = FirstPersonController(x=1,z=ancho/2)

        app.run()
        
pantalla()

