from tkinter import  *
from tkinter import  ttk
from tkinter.ttk import Combobox
from tokenize import Double

def pantalla2():
    
    Ventana2 = Tk()
    global texturasP
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
    texturasPisos["values"] = ('"madera"', '"Piso_madera2"', '"baldosa"')
    texturasPisos.pack()
   
    Espacio = Label(Ventana2, text="", bg="sky blue").pack()
    def imprimir():
            texturasPi = texturasP.get()
            print(texturasPi)

    boton2 = Button(Ventana2, text="Iniciar", height="3", width="20", bg="brown", command=imprimir).pack()
    Ventana2.mainloop()

pantalla2()