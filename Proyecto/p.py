from tkinter import *
from tkinter import  ttk
from tkinter.ttk import Combobox
from tokenize import Double

from numpy import integer

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
    letreroS4 = Label(Ventana2, text="Color piso:", bg="sky blue", font=("Arial Black",10)).place(x=300, y= 400)
    caja4= Entry(Ventana2, width=20, textvariable=ColorP).place(x=280, y= 430)
#campo texturas techo
    letreroS5 = Label(Ventana2, text="Textura techo:", bg="sky blue", font=("Arial Black",10)).place(x=60, y= 460)
    texturasTecho = ttk.Combobox(Ventana2,  state="readonly", textvariable=texturasT)
    texturasTecho["values"] = ("techo_negro")
    texturasTecho.place(x=50, y= 490)
    letreroS6 = Label(Ventana2, text="Color piso:", bg="sky blue", font=("Arial Black",10)).place(x=300, y= 460)
    caja4= Entry(Ventana2, width=20, textvariable=ColorT).place(x=280, y= 490)
#campo tecturas paredes
    letreroS5 = Label(Ventana2, text="Textura paredes:", bg="sky blue", font=("Arial Black",10)).place(x=60, y= 520)
    texturasParedes = ttk.Combobox(Ventana2,  state="readonly", textvariable=texturasPa)
    texturasParedes["values"] = ("ladrilloBlanco")
    texturasParedes.place(x=50, y= 550)
    letreroS5 = Label(Ventana2, text="Color piso:", bg="sky blue", font=("Arial Black",10)).place(x=300, y= 520)
    cajas= Entry(Ventana2, width=20, textvariable=ColorPa).place(x=280, y= 550)
#variables importantes a enteros

    boton2 = Button(Ventana2, text="Iniciar", height="3", width="20", bg="brown").place(x=170, y= 590)
    Ventana2.mainloop()
    
pantalla2()