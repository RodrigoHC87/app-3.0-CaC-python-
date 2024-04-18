import tkinter as tk
from tkinter import ttk


def actualizar_combobox(*args):
    categoria_seleccionada = cmbPadre.get()

    # Limpiar el cmbHijo
    cmbHijo['values'] = []

    # Añadir elementos al cmbHijo según la selección de cmbPadre
    if categoria_seleccionada == "Categoria 1":
        cmbHijo['values'] = ["Subcategoria 1.1", "Subcategoria 1.2"]
    elif categoria_seleccionada == "Categoria 2":
        cmbHijo['values'] = ["Subcategoria 2.1", "Subcategoria 2.2"]
    elif categoria_seleccionada == "Categoria 3":
        cmbHijo['values'] = ["Subcategoria 3.1", "Subcategoria 3.2"]

# Crear la ventana principal
root = tk.Tk()
root.title("ComboBox dinámico")

# ComboBox Padre
lblPadre = ttk.Label(root, text="Categoría Padre:")
lblPadre.grid(column=0, row=0)

cmbPadre = ttk.Combobox(root, values=["Categoria 1", "Categoria 2", "Categoria 3"])
cmbPadre.grid(column=1, row=0)
cmbPadre.bind("<<ComboboxSelected>>", actualizar_combobox)

# ComboBox Hijo
lblHijo = ttk.Label(root, text="Subcategoría Hijo:")
lblHijo.grid(column=0, row=1)

cmbHijo = ttk.Combobox(root, values=[])
cmbHijo.grid(column=1, row=1)

root.mainloop()


# //////////////////////////////////////////////////////////////////////


def update_combobox_options():
    selected_category = category.get()
    
    if selected_category == "Frutas":
        second_combobox['values'] = ["Manzana", "Plátano", "Fresa"]
    elif selected_category == "Verduras":
        second_combobox['values'] = ["Zanahoria", "Espinaca", "Brócoli"]
    elif selected_category == "Carnes":
        second_combobox['values'] = ["Pollo", "Res", "Cerdo"]
    else:
        second_combobox['values'] = []

# Crear la ventana principal
root = tk.Tk()
root.title("Filtrar Combobox con Radiobuttons")

# Variables de control para los Radiobuttons
category = tk.StringVar()

# Radiobuttons
fruits_radio = ttk.Radiobutton(root, text="Frutas", variable=category, value="Frutas", command=update_combobox_options)
fruits_radio.pack(pady=10)

vegetables_radio = ttk.Radiobutton(root, text="Verduras", variable=category, value="Verduras", command=update_combobox_options)
vegetables_radio.pack(pady=10)

meat_radio = ttk.Radiobutton(root, text="Carnes", variable=category, value="Carnes", command=update_combobox_options)
meat_radio.pack(pady=10)

# Combobox
second_combobox = ttk.Combobox(root, values=[])
second_combobox.pack(pady=20)

root.mainloop()

#//////////////////////////////////////////////////////////////////////////////

import tkinter as tk
from tkinter import ttk

def update_second_combobox(event):
    selected_item = first_combobox.get()
    
    if selected_item == "Frutas":
        second_combobox['values'] = ["Manzana", "Plátano", "Fresa"]
    elif selected_item == "Verduras":
        second_combobox['values'] = ["Zanahoria", "Espinaca", "Brócoli"]
    elif selected_item == "Carnes":
        second_combobox['values'] = ["Pollo", "Res", "Cerdo"]
    else:
        second_combobox['values'] = []

# Crear la ventana principal
root = tk.Tk()
root.title("Filtrar Combobox con otro Combobox")

# Primer Combobox
first_combobox = ttk.Combobox(root, values=["Frutas", "Verduras", "Carnes"])
first_combobox.pack(pady=20)
first_combobox.bind("<<ComboboxSelected>>", update_second_combobox)

# Segundo Combobox
second_combobox = ttk.Combobox(root, values=[])
second_combobox.pack(pady=20)

root.mainloop()

def update_second_combobox(event):
    selected_item = first_combobox.get()

    if selected_item == "Opción 1":
        second_combobox['values'] = ["Subopción 1.1", "Subopción 1.2"]
    elif selected_item == "Opción 2":
        second_combobox['values'] = ["Subopción 2.1", "Subopción 2.2"]
    else:
        second_combobox['values'] = ["hola", "chau", 21]

# Crear la ventana principal
root = tk.Tk()
root.title("Combobox dentro de Combobox")

# Primer Combobox
first_combobox = ttk.Combobox(root, values=["Opción 1", "Opción 2", "Opción 3"])
first_combobox.pack(pady=20)
first_combobox.bind("<<ComboboxSelected>>", update_second_combobox)

# Segundo Combobox
second_combobox = ttk.Combobox(root, values=[])
second_combobox.pack(pady=20)

root.mainloop()