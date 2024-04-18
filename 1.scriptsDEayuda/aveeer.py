from datetime import datetime
from tkinter import messagebox
from os import system

import seaborn as sns
import pandas as pd


system("cls")


"""
# Ejemplo de datos
data = pd.DataFrame({
    'Categoría': ['A', 'B', 'C', 'D'],
    'Valor': [10, 20, 15, 25]
})

# Crear gráfico de barras
sns.barplot(x='Categoría', y='Valor', data=data)
"""







def fecha_hora():
    today_date = datetime.today().strftime("%d/%m/%y")
    current_time = datetime.now().strftime("%H:%M:%S")
    return (today_date, current_time)

fecha_hora1 = fecha_hora()

print(f"fecha: {fecha_hora1[0]} y la hora: {fecha_hora1[1]}")






def mostrar_mensaje(tipo, contenido):

    if tipo == "Error":
        return messagebox.showerror(tipo, contenido)
    elif tipo == "Info":
        return messagebox.showinfo(tipo, contenido)
    elif tipo == "Warning":
        return messagebox.showwarning(tipo, contenido)



"""
mostrar_mensaje("Error", "cartel de error!")
mostrar_mensaje("Info", "cartel de info!")
mostrar_mensaje("Warning", "cartel de warning!")
"""


def mostrar_mensaje(tipo, contenido):
    messagebox_func = getattr(messagebox, f"show{tipo.lower()}")
    return messagebox_func(tipo, contenido)

mostrar_mensaje("Error", "cartel de error!")
mostrar_mensaje("Info", "cartel de info!")
mostrar_mensaje("Warning", "cartel de warning!")