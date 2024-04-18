
import tkinter as tk
from tkinter import ttk





import tkinter as tk
from tkinter import ttk

def actualizar_combobox(event):
    opcion_seleccionada = combobox1.get()

    if opcion_seleccionada == "Opción 1":
        combobox2['values'] = ["A", "B", "C"]
        textvariable2.set("Valor A")
    elif opcion_seleccionada == "Opción 2":
        combobox2['values'] = ["X", "Y", "Z"]
        textvariable2.set("Valor X")
    elif opcion_seleccionada == "Opción 3":
        combobox2['values'] = ["1", "2", "3"]
        textvariable2.set("Valor 1")

# Crear la ventana principal
root = tk.Tk()
root.title("Ejemplo de ComboBox Dinámico")

# Variables para los ComboBox
opciones = ["Opción 1", "Opción 2", "Opción 3"]

# ComboBox 1
label1 = ttk.Label(root, text="ComboBox 1:")
label1.pack(pady=10)

combobox1 = ttk.Combobox(root, values=opciones, state="readonly")
combobox1.pack(pady=10)
combobox1.bind("<<ComboboxSelected>>", actualizar_combobox)

# ComboBox 2
label2 = ttk.Label(root, text="ComboBox 2:")
label2.pack(pady=10)

combobox2 = ttk.Combobox(root, state="readonly")
combobox2.pack(pady=10)

# Variable asociada al ComboBox 2
textvariable2 = tk.StringVar()
combobox2['textvariable'] = textvariable2

root.mainloop()

#///////////////////////////////////////////////////////////////////////////////
def actualizar_combobox(event):
    valor_seleccionado = combobox1.get()
    combobox2.set(valor_seleccionado)

# Crear la ventana principal
root = tk.Tk()
root.title("Ejemplo de ComboBox")

# Variables para los ComboBox
opciones = ["Opción 1", "Opción 2", "Opción 3"]

# ComboBox 1
label1 = ttk.Label(root, text="ComboBox 1:")
label1.pack(pady=10)

combobox1 = ttk.Combobox(root, values=opciones, state="readonly")
combobox1.pack(pady=10)

# ComboBox 2
label2 = ttk.Label(root, text="ComboBox 2:")
label2.pack(pady=10)

combobox2 = ttk.Combobox(root, values=opciones, state="readonly")
combobox2.pack(pady=10)

# Asociar el evento de selección en combobox1 a la función actualizar_combobox
combobox1.bind("<<ComboboxSelected>>", actualizar_combobox)

root.mainloop()




# ///////////////////////////////////////////////////////////////////////////////////////

def copiar_valor():
    valor_seleccionado = combobox1.get()
    combobox2.set(valor_seleccionado)

# Crear la ventana principal
root = tk.Tk()
root.title("Ejemplo de ComboBox")

# Variables para los ComboBox
opciones = ["Opción 1", "Opción 2", "Opción 3"]

# ComboBox 1
label1 = ttk.Label(root, text="ComboBox 1:")
label1.pack(pady=10)

combobox1 = ttk.Combobox(root, values=opciones, state="readonly")
combobox1.pack(pady=10)

# ComboBox 2
label2 = ttk.Label(root, text="ComboBox 2:")
label2.pack(pady=10)

combobox2 = ttk.Combobox(root, values=opciones, state="readonly")
combobox2.pack(pady=10)

# Botón para copiar el valor
boton_copiar = ttk.Button(root, text="Copiar Valor", command=copiar_valor)
boton_copiar.pack(pady=20)

root.mainloop()
