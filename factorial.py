import tkinter as tk

def calcular_factorial():
    numero = int(entry.get())
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    resultado.config(text=f"El factorial de {numero} es {factorial}")

root = tk.Tk()
root.title("Calculadora de factorial")

# Crear una etiqueta y una entrada de texto para ingresar el número
label = tk.Label(root, text="Ingrese un número:")
label.pack()
entry = tk.Entry(root)
entry.pack()

# Crear un botón para calcular el factorial
boton_calcular = tk.Button(root, text="Calcular factorial", command=calcular_factorial)
boton_calcular.pack()

# Crear una etiqueta para mostrar el resultado
resultado = tk.Label(root, text="")
resultado.pack()

root.mainloop()