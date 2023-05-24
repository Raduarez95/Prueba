from PIL import Image, ImageTk
import tkinter as tk

# Crear la ventana
ventana = tk.Tk()

# Abrir la imagen con PIL
imagen = Image.open("0Wk5gN4R_400x400.jpg")

# Convertir la imagen a un objeto de imagen de Tkinter
imagen_tk = ImageTk.PhotoImage(imagen)

# Crear un widget de imagen y mostrar la imagen en la ventana
etiqueta_imagen = tk.Label(ventana, image=imagen_tk)
etiqueta_imagen.pack()

# Mostrar la ventana
ventana.mainloop()