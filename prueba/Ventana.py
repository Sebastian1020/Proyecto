from tkinter import *
from tkinter import  ttk
from tkinter.ttk import Combobox
from tokenize import Double


def pantalla():
    global Ventana, alto, ancho, largo 
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

    def pantalla2():
        global Ventana2, texturasP, alto, ancho, largo
        Ventana2 = Toplevel()
        texturasP=StringVar()
    #Parametros de la ventana
        Ventana2.geometry("350x650")
        Ventana2.title("Ingresar datos de la habitación")
        Ventana2.iconbitmap("Imagenes\Cat.ico")
        Ventana2.configure(bg="sky blue")
    #imagen del logo
        imagen2 = PhotoImage(file = "Imagenes\habitacion.gif").subsample(2,2)
        label2 = Label(Ventana2, image = imagen2)
        label2.pack()
    #letrero medidas
        letreroT2 = Label(Ventana2, text="Texturas", bg="brown", fg="white", width="300", height="3", font=("Arial Black", 15)).pack()
        Espacio = Label(Ventana2, text="", bg="sky blue").pack()
    #campo Texturas pisos
        letreroS4 = Label(Ventana2, text="Textura piso:", bg="sky blue", font=("Arial Black",10)).pack()
        texturasPisos = ttk.Combobox(Ventana2,  state="readonly", textvariable=texturasP)
        texturasPisos["values"] = ("madera", "Piso_madera2", "baldosa")
        texturasPisos.pack()
        Espacio = Label(Ventana2, text="", bg="sky blue").pack()
    #variables importantes a enteros
        alto = int(caja1.get())
        ancho = int(caja2.get())
        largo = int(caja3.get())
        
        from ursina import Entity, scene, Vec3, Ursina
        from ursina.prefabs.first_person_controller import FirstPersonController
        def ejecutable(): 
            global app  
        #texturas techo
            texturaTecho = "techo_negro"
        #texturas paredes
            texturaPared = "ladrilloBlanco"
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
                        origin = Vec3(0,0,0)
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
                        texture = texturaTecho,
                        collider = "box"
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
                        texture = texturaPared,
                        collider = "box"
                    )
        #seguir despues de Ventana2
            app = Toplevel(Ventana2)    
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

            player = FirstPersonController(x=1,z=ancho/2)

            app.run()
        boton2 = Button(Ventana2, text="Iniciar", height="3", width="20", bg="brown",command=ejecutable).pack()
        Ventana2.mainloop()      

    boton1 = Button(Ventana, text="Siguente", height="3", width="20", bg="green", command=pantalla2).pack()
    Ventana.mainloop()

pantalla()

