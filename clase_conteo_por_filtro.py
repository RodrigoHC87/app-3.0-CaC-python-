"""def conte_de_votos_1(provincia, region, rango_edad):


    conteos = {
        "Voto en Blanco": 0,
        "Juntos sin el cambio": 0,
        "La SINiestra": 0,
        "La libertad no avanza": 0,
        "Por unión la patria": 0
    }

    conj_de_prov = {
        'Noroeste': {"Jujuy", "Salta", "Tucumán", "Santiago del Estero", "Catamarca", "La Rioja"},
        'Nordeste': {"Corrientes", "Misiones", "Chaco", "Formosa"},
        'Cuyo': {"San Luis", "Mendoza", "San Juan"},
        'Pampeana': {"Córdoba", "La Pampa", "Buenos Aires", "CABA", "Santa Fe", "Entre Ríos"},
        'Patagonia': {"Neuquén", "Río Negro", "Chubut", "Santa Cruz", "Tierra del Fuego, Antártida e Islas del Atlántico Sur"},
    }


    rango_etario = rango_edad.get()
    if ">" in rango_edad.get():
        edades = rango_etario.split(">")
    else:
        edades=rango_etario.split("-")

    query_edad = Encuestaa.select().where((Encuestaa.edad >= edades[0]) & (Encuestaa.edad <= edades[1]) )
    for encuesta_1 in query_edad:
        voto = encuesta_1.voto
        if voto in conteos1:
            conteos1[voto] += 1
    votos_grafico_edad = list(conteos1.values())
    print("votos // _rango edad --->", votos_grafico_edad)


    pass"""