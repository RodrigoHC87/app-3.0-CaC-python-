import tkinter as tk
from tkinter import messagebox




import tkinter as tk

def nueva_funcion():
    # Código de la función asociada al elemento "Nuevo"
    print("¡Se ha creado un nuevo archivo!")

ventana = tk.Tk()
ventana.title("Ventana con Menú")

barra_menus = tk.Menu(ventana, tearoff=0)
ventana.config(menu=barra_menus)

menu_archivo = tk.Menu(barra_menus, tearoff=0)
menu_archivo.add_command(label="Nuevo", command=nueva_funcion)
menu_archivo.add_command(label="Abrir...")
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=ventana.quit)

barra_menus.add_cascade(label="Archivo", menu=menu_archivo)

ventana.mainloop()






#/////////////////////////////////////////////////////////////////
def opcion1():
    messagebox.showinfo("Información", "Has seleccionado la opción 1")

def opcion2():
    messagebox.showinfo("Información", "Has seleccionado la opción 2")

def salir():
    ventana.quit()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Menú con Tkinter")

# Crear un menú
menu_principal = tk.Menu(ventana)
ventana.config(menu=menu_principal)

# Crear opciones en el menú
menu_archivo = tk.Menu(menu_principal)
menu_principal.add_cascade(label="Archivo", menu=menu_archivo)
menu_archivo.add_command(label="Opción 1", command=opcion1)
menu_archivo.add_command(label="Opción 2", command=opcion2)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=salir)

# Mostrar la ventana
ventana.mainloop()