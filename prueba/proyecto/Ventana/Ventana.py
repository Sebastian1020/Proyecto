from ast import In
from tkinter import  *
from tkinter import  ttk
from tkinter.ttk import Combobox
from tokenize import Double 

def pantalla():
    global Ventana
    Ventana = Tk()
    #Parametros de la ventana
    Ventana.geometry("350x650")
    Ventana.title("Ingresar datos de la habitación")
    Ventana.iconbitmap("Cat.ico")
    Ventana.configure(bg="sky blue")
    #imagen del logo
    image = PhotoImage(file = "Imgportada.gif")
    image = image.subsample(2,2)
    label =Label(image = image)
    label.pack()
    #letrero medidas
    Label(text="Medidas", bg="green", fg="white", width="300", height="3", font=("Arial Black", 15)).pack()
    Label(text="", bg="sky blue").pack()
    #variables importantes
    global alto
    global ancho
    global largo 
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
        global Ventana2
        Ventana2=Toplevel(Ventana)
        Ventana2 = Tk()
        #Parametros de la ventana
        Ventana2.geometry("350x650")
        Ventana2.title("Ingresar datos de la habitación")
        Ventana2.iconbitmap("Cat.ico")
        Ventana2.configure(bg="sky blue")
        #imagen del logo
        image = PhotoImage(file = "habitacion.gif")
        image = image.subsample(2,2)
        label =Label(image = image)
        label.pack()
        #letrero medidas
        Label(text="Texturas", bg="brown", fg="white", width="300", height="3", font=("Arial Black", 15)).pack()
        Label(text="", bg="sky blue").pack()
        #campo Texturas pisos
        Label(Ventana2, text="Textura piso:", bg="sky blue", font=("Arial Black",10)).pack()
        texturasPisos
        texturasPisos = ttk.Combobox(Ventana2)
        texturasPisos.place(x=100, y=450)
        texturasPisos["values"] = ("madera", "Piso_madera2", "baldosa")
        global texturasP
        texturasP=texturasPisos.get()
        
        Button(Ventana2, text="Iniciar", height="3", width="20", bg="brown").place(y=570, x=100)
        print (texturasPisos)
        Ventana2.mainloop()
    
    Button(Ventana, text="Siguente", height="3", width="20", bg="green", command=pantalla2).pack()
    Ventana.mainloop()
     
pantalla()