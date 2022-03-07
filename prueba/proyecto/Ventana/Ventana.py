from ast import In
from tkinter import  *
from tokenize import Double 
import proyecto as ejecutable

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
    #boton
   
    alto = int(caja1.get())
    ancho = int(caja2.get())
    largo = int(caja3.get())
        
    ejecutable()
    
    Button(Ventana, text="Iniciar", height="3", width="20", bg="green", command=ejecutable).pack()
    
    Ventana.mainloop()
    
pantalla()
