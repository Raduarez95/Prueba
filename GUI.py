import tkinter as tk
#Funcion para el boton
def BotonPresionado():
    print("Click!!")
#Ventana
ventana = tk.Tk()
ventana.title("Prueba Ventana")
ventana.geometry("500x400")
ventana.resizable(0,0)
#etiquetas
etiqueta = tk.Label(ventana, text = "Hola mundo")
#etiqueta.place(x = 400, y = 380, width = 100, height = 20)
etiqueta.grid(padx=20,pady=10, column=0, row = 0)
#etiqueta.pack()
#boton
boton = tk.Button(ventana, text = "Click!", command = BotonPresionado)
boton.grid(padx=20,pady=10,column = 0, row = 1)
#boton.pack()
#Input
etiqueta = tk.Label(ventana, text = "Ingresa tu nombre")
etiqueta.grid(padx=20,pady=10,column = 1, row = 0)
#etiqueta.pack()
#Definicion de la accion para leer el dato:
def RecibirValor():
    nombre = entrada.get()
    print("Ingresaste el dato: "+nombre)
entrada = tk.Entry(ventana)
entrada.grid(padx=20,pady=10,column = 1, row = 1)
botoninput = tk.Button(ventana, text = "Aceptar", command = RecibirValor)
botoninput.grid(padx=20,pady=10,column = 1, row = 2)
ventana.mainloop()