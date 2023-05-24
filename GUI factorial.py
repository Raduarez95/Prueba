import tkinter as tk

def CalcularFact():
    n = int(numero.get()) #Parseo "5"-> 5
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
    resultado.config(text=f"El factorial de {n} es {fact}")

ventana = tk.Tk()
ventana.title("Calculadora Factorial")
ventana.geometry("200x200")


instrucciones = tk.Label(ventana,text="Ingresa tu número...")
instrucciones.pack();

numero = tk.Entry(ventana)
numero.insert(0,"5")
numero.pack()

botonAceptar = tk.Button(ventana,command=CalcularFact,text="Aceptar")
botonAceptar.pack()

resultado = tk.Label(ventana, text="")
resultado.pack()

ventana.mainloop()