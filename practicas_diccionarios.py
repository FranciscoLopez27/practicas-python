CATALOGO_ANALISIS = {
    "A01": {"nombre": "Aerobios mesófilos", "unidad": "UFC/g", "dias": 3},
    "A02": {"nombre": "Enterobacterias", "unidad": "UFC/g", "dias": 2},
    "A03": {"nombre": "Coliformes totales", "unidad": "NMP/g", "dias": 2},
    "A04": {"nombre": "Salmonella", "unidad": "Presencia/25g", "dias": 5},
}

MUESTRAS = [
    {"id": "M-0001", "cliente": "0042", "estado": "liberada",
     "analisis": [{"codigo": "A01", "recuento": 150000}, {"codigo": "A02", "recuento": 50}]},
    {"id": "M-0002", "cliente": "1234", "estado": "enviada",
     "analisis": [{"codigo": "A02", "recuento": 900}]},
    {"id": "M-0003", "cliente": "0042", "estado": "confirmada",
     "analisis": [{"codigo": "A01", "recuento": 2000}, {"codigo": "A03", "recuento": 10}]},
]

def nombre_analisis(codigo):
        analisis_asociado = CATALOGO_ANALISIS.get(codigo)
        if analisis_asociado is None:
             return analisis_asociado
        return analisis_asociado.get("nombre")

def codigos_por_unidad(unidad):
    por_unidad = []
    for codigo, datos_analisis in CATALOGO_ANALISIS.items():
        if datos_analisis["unidad"] == unidad:
            por_unidad.append(codigo)
    return por_unidad

def analisis_mas_largo():
    codigo_mas_demoros = []
    for codigo, datos_analisis in CATALOGO_ANALISIS.items():
        if len(codigo_mas_demoros) == 0:
              codigo_mas_demoros.append({codigo: datos_analisis})
        else:
             diccionario_guardado = codigo_mas_demoros[0]
             datos_actual = next(iter(diccionario_guardado.values()))

             if datos_actual["dias"] < datos_analisis["dias"]:
                  codigo_mas_demoros[0] = {codigo: datos_analisis}
    codigo_final = next(iter(codigo_mas_demoros[0].keys()))
    return codigo_final
              
              
assert nombre_analisis("A02") == "Enterobacterias"
assert nombre_analisis("A99") is None
assert codigos_por_unidad("UFC/g") == ["A01", "A02"]
assert codigos_por_unidad("kg") == []
assert analisis_mas_largo() == "A04"