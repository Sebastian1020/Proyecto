import sys
from tkinter import *


def sumar():
    try:
        _valor1 = int(entrada_texto.get())
        _valor2 = int(entrada2_texto.get())
        _valor = _valor1+_valor2
        etiqueta3.config(text=_valor)
    except ValueError:
        etiqueta3.config(text="Introduce un numero")

def restar():
    try:
        _valor1 = int(entrada_texto.get())
        _valor2 = int(entrada2_texto.get())
        _valor = _valor1 - _valor2
        etiqueta4.config(text=_valor)
    except ValueError:
        etiqueta4.config(text="Introduce un numero")

def multiplicar():
    try:
        _valor1 = int(entrada_texto.get())
        _valor2 = int(entrada2_texto.get())
        _valor = _valor1 * _valor2
        etiqueta5.config(text=_valor)
    except ValueError:
        etiqueta5.config(text="Introduce un numero")


app = Tk()
app.title("Operaciones")

# Ventana Principal
vp = Frame(app)
vp.grid(column=0, row=0, padx=(50, 50), pady=(10, 10))
vp.columnconfigure(0, weight=1)
vp.rowconfigure(0, weight=1)

etiqueta = Label(vp, text="Numero 1")
etiqueta.grid(column=1, row=1, sticky=(W, E))
etiqueta2 = Label(vp, text="Numero 2")
etiqueta2.grid(column=3, row=1, sticky=(W, E))

etiqueta3= Label(vp, text="suma")
etiqueta3.grid(column=1, row=5, sticky=(W, E))
etiqueta4= Label(vp, text="resta")
etiqueta4.grid(column=2, row=5, sticky=(W, E))
etiqueta5= Label(vp, text="multiplicacion")
etiqueta5.grid(column=3, row=5, sticky=(W, E))

boton = Button(vp, text="sumar", command=sumar)
boton.grid(column=1, row=4)
boton2 = Button(vp, text="restar", command=restar)
boton2.grid(column=2, row=4)
boton3= Button(vp, text="multiplicar", command=multiplicar)
boton3.grid(column=3, row=4)

valor = ""
entrada_texto = Entry(vp, width=10, textvariable=valor)
entrada_texto.grid(column=2, row=1)
valor2 = ""
entrada2_texto = Entry(vp, width=10, textvariable=valor2)
entrada2_texto.grid(column=4, row=1)


app.mainloop()