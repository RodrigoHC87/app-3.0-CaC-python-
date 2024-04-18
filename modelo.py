from tkinter import messagebox
from peewee import SqliteDatabase, Model, AutoField, CharField, IntegerField, IntegrityError
from datetime import datetime
from pathlib import Path


from validar_campos import ValidarDatos
from decorador import tipo_de_entrada
from observador import Subject


ruta_db = Path("bases_de_datos/data_base.db")

db = SqliteDatabase(ruta_db)
db.connect()

class BaseModel(Model):
    class Meta:
        database = db


class Encuestaa(BaseModel):
    id = AutoField()
    nombre = CharField()
    edad = IntegerField()
    email = CharField(unique=True)
    provincia = CharField()
    voto = CharField()


db.create_tables([Encuestaa], safe=True)


class Abmc(Subject):

    @tipo_de_entrada("ALTA")
    def alta(self, nombre, edad, email, provincia, voto, my_tree):

        code = ValidarDatos.validar_campos(self, nombre, edad, email, provincia, voto)

        if code == 0:

            with db.atomic():
                encuesta1 = Encuestaa(
                    nombre = nombre.get(),
                    edad = edad.get(),
                    email = email.get(),
                    provincia = provincia.get(),
                    voto = voto.get()
                )

                try:
                    encuesta1.save()
                    self.actualizar_treeview(my_tree)
                    messagebox.showinfo("Guardar", "Elemento insertado correctamente")
                    fecha_hora1 = fecha_hora()

                    self.notificar("Alta", nombre.get(), email.get(),
                                   fecha_hora1[0], fecha_hora1[1]
                                )
                    return code

                except IntegrityError:
                    messagebox.showerror("Error", f"El correo {email.get()} ya fue ingresado")
                    code = 3
                    return code

                except Exception as e:
                    print(e)
        else:
            return code


    @tipo_de_entrada("MODIFICAR")
    def modificar(self, nombre, edad, email, provincia, voto, my_tree):

        item_seleccionado = my_tree.focus()
        valor_id = my_tree.item(item_seleccionado)
        code = ValidarDatos.validar_campos(self, nombre, edad, email, provincia, voto)

        if code == 0:
            try:
                actualizar = Encuestaa.update(nombre=nombre.get(), edad=edad.get(), email=email.get(),
                                              provincia=provincia.get(), voto=voto.get()
                                              ).where(Encuestaa.id==valor_id["text"])

                actualizar.execute()

                self.actualizar_treeview(my_tree)
                messagebox.showinfo("Guardar", "Elemento modificado correctamente")

                fecha_hora1 = fecha_hora()

                self.notificar("Modificar", nombre.get(), email.get(),
                               fecha_hora1[0], fecha_hora1[1]
                               )
                return code

            except IntegrityError:
                messagebox.showerror("Error", f"El correo {email.get()} ya fue ingresado")
                code = 3
                return code

        else:
            return code


    @tipo_de_entrada("BAJA")
    def baja(self, my_tree):

        code = 1
        item_seleccionado = my_tree.focus()
        valor_id = my_tree.item(item_seleccionado)

        if valor_id["text"] == "":
            messagebox.showwarning("Eliminar", "Debes seleccionar un elemento de la tabla")
            return code

        else:
            data = f'{valor_id["values"][0]} - {valor_id["values"][1]} - {valor_id["values"][2]}'
            respuesta = messagebox.askquestion("Eliminar", "Deseas eliminar el registro seleccionado?\n   " + data)

            if respuesta == messagebox.YES:
                borrar = Encuestaa.get(Encuestaa.id==valor_id["text"])
                borrar.delete_instance()
                self.actualizar_treeview(my_tree)
                code = 0
                messagebox.showinfo("Eliminar", "Elemento eliminado correctamente")

                fecha_hora1 = fecha_hora()

                self.notificar("Baja", valor_id["values"][0], valor_id["values"][2],
                               fecha_hora1[0], fecha_hora1[1]
                               )
                return code

            else:
                messagebox.showinfo("Eliminar", "No fué posible eliminar el elemento")
                return code


# ----------------------------------Fun. actualizar treevieew
    def actualizar_treeview(self, my_tree):
        #limpieza de tabla
        records = my_tree.get_children()
        for element in records:
            my_tree.delete(element)
        #consiguiendo datos:
        for fila in Encuestaa.select():
            my_tree.insert("", 0, text=fila.id, values=(fila.nombre, fila.edad,fila.email, fila.provincia, fila.voto))


# ----------------------------------Fun. conteo_de_votos:
# ------------------------------------------------------------NUEVO!!
    def conteo_de_votos_1(self, categoria, prov_o_reg_selec, rango_edad, partido, my_tree):


        conj_de_prov = {
            'Noroeste': {"Jujuy", "Salta", "Tucumán", "Santiago del Estero", "Catamarca", "La Rioja"},
            'Nordeste': {"Corrientes", "Misiones", "Chaco", "Formosa"},
            'Cuyo': {"San Luis", "Mendoza", "San Juan"},
            'Pampeana': {"Córdoba", "La Pampa", "Buenos Aires", "CABA", "Santa Fe", "Entre Ríos"},
            'Patagonia': {"Neuquén", "Río Negro", "Chubut", "Santa Cruz", "Tierra del Fuego, Antártida e Islas del Atlántico Sur"},
        }

        conteos_0 = {
            "Voto en Blanco": 0,
            "Juntos sin el cambio": 0,
            "La SINiestra": 0,
            "La libertad no avanza": 0,
            "Por unión la patria": 0
        }

        if (categoria.get() != "" and prov_o_reg_selec.get() != "") or rango_edad.get() != "" or partido.get() != "":

            posibilidades_lista = []

            if rango_edad.get() != "":
                posibilidades_lista.append('1')
            else:
                posibilidades_lista.append('0')

            if categoria.get() == "Provincia":
                posibilidades_lista.append('1')
            else:
                posibilidades_lista.append('0')

            if categoria.get() == "Región":
                posibilidades_lista.append('1')
            else:
                posibilidades_lista.append('0')

            if partido.get() != "":
                posibilidades_lista.append('1')
            else:
                posibilidades_lista.append('0')


            if rango_edad.get() != "":
                rango_etario = rango_edad.get()
                if "> 64" in rango_edad.get():
                    edades = ['65', '105']
                else:
                    edades = rango_etario.split("-")
            else:
                edades = ['0', '0']


            if categoria.get() == "Región":
                lista_prov = list(conj_de_prov[prov_o_reg_selec.get()])
            else:
                lista_prov = ["nada"]



            posibilidades_dic = {
                #Posibilidades con un solo filtro
                '1000': (Encuestaa.edad >= edades[0]) & (Encuestaa.edad <= edades[1]),
                '0100': Encuestaa.provincia == prov_o_reg_selec.get(),
                '0010': Encuestaa.provincia << lista_prov,
                '0001': Encuestaa.voto == partido.get(),
                #Posibilidades con 2 Filtros en simultáneo
                '1100': (Encuestaa.provincia == prov_o_reg_selec.get()) & (Encuestaa.edad >= edades[0]) & (Encuestaa.edad <= edades[1]),
                '1010': (Encuestaa.provincia << lista_prov) & (Encuestaa.edad >= edades[0]) & (Encuestaa.edad <= edades[1]),
                '1001': (Encuestaa.voto == partido.get()) & (Encuestaa.edad >= edades[0]) & (Encuestaa.edad <= edades[1]),
                '0101': (Encuestaa.provincia == prov_o_reg_selec.get()) & (Encuestaa.voto == partido.get()),
                '0011': (Encuestaa.provincia << lista_prov) & (Encuestaa.voto == partido.get()),
                #Posibilidades con 2 Filtros en simultáneo
                '1101': (Encuestaa.provincia == prov_o_reg_selec.get()) & (Encuestaa.edad >= edades[0]) & (Encuestaa.edad <= edades[1]) & (Encuestaa.voto == partido.get()),
                '1011': (Encuestaa.edad >= edades[0]) & (Encuestaa.edad <= edades[1]) & (Encuestaa.provincia << lista_prov) & (Encuestaa.voto == partido.get()),
            }

            posibilidades_lista = str(posibilidades_lista[0]) + str(posibilidades_lista[1]) + str(posibilidades_lista[2]) + str(posibilidades_lista[3])
            posibilidades_final = posibilidades_lista.split(" ")

            pos_finaaal= posibilidades_final[0]

            query = Encuestaa.select().where(posibilidades_dic.get(pos_finaaal))

            for encuesta_1 in query:
                voto = encuesta_1.voto
                if voto in conteos_0:
                    conteos_0[voto] += 1
            votos_grafico_2 = list(conteos_0.values())

            print('posibilidades_lista <---> ', posibilidades_lista)
            print("blancos:     ", votos_grafico_2[0])
            print("juntos:      ", votos_grafico_2[1])
            print("izquierda:   ", votos_grafico_2[2])
            print("la libertad: ", votos_grafico_2[3])
            print("union:       ", votos_grafico_2[4])
            print("--------------------------------------\n")


            #limpieza de tabla
            records = my_tree.get_children()
            for element in records:
                my_tree.delete(element)
            #consiguiendo datos:
            for fila in Encuestaa.select().where(posibilidades_dic.get(pos_finaaal)):
                my_tree.insert("", 0, text=fila.id, values=(fila.nombre,
                                                            fila.edad,
                                                            fila.email,
                                                            fila.provincia,
                                                            fila.voto)
                               )

            return votos_grafico_2

        else:
            print("afueraaa! strike out --- else")

            self.actualizar_treeview(my_tree)

            for encuestas in Encuestaa.select():
                voto = encuestas.voto
                if voto in conteos_0:
                    conteos_0[voto] += 1

            votos_grafico_2 = list(conteos_0.values())
            votos_grafico = list(conteos_0.values())
            print("blancos:     ", votos_grafico[0])
            print("juntos:      ", votos_grafico[1])
            print("siniestra    ", votos_grafico[2])
            print("libertad:    ", votos_grafico[3])
            print("union:       ", votos_grafico[4])
            print("--------------------------------------\n")

            return votos_grafico_2



# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



# ----------------------------------Fun. fecha y hora
def fecha_hora():
    fecha = datetime.today().strftime("%d/%m/%y")
    hora = datetime.now().strftime("%H:%M:%S")
    return (fecha, hora)