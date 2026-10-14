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
    codigo_mas_demoroso = None
    dias_mas_demorosos = 0
    for codigo, datos in CATALOGO_ANALISIS.items():
         if datos["dias"] > dias_mas_demorosos:
              codigo_mas_demoroso = codigo
              dias_mas_demorosos = datos["dias"]
    return codigo_mas_demoroso
              
              
assert nombre_analisis("A02") == "Enterobacterias"
assert nombre_analisis("A99") is None
assert codigos_por_unidad("UFC/g") == ["A01", "A02"]
assert codigos_por_unidad("kg") == []
assert analisis_mas_largo() == "A04"

def buscar_muestra(muestras, id_muestra):
    return next((muestra for muestra in muestras if id_muestra == muestra.get("id")), None)

def ids_por_cliente(muestras,cliente):
    return [muestra.get("id") for muestra in muestras if muestra.get("cliente") == cliente]

def contar_por_estado(muestras):
    diccionario_muestras_por_estado = {}
    for muestra in muestras:
         estado_muestra = muestra.get("estado")
         diccionario_muestras_por_estado[estado_muestra] = diccionario_muestras_por_estado.get(estado_muestra,0) + 1
    return diccionario_muestras_por_estado
    
assert buscar_muestra(MUESTRAS, "M-0002")["cliente"] == "1234"
assert buscar_muestra(MUESTRAS, "M-9999") is None
assert ids_por_cliente(MUESTRAS, "0042") == ["M-0001", "M-0003"]
assert ids_por_cliente(MUESTRAS, "5678") == []
assert contar_por_estado(MUESTRAS) == {"liberada": 1, "enviada": 1, "confirmada": 1}
assert contar_por_estado([]) == {}


def codigos_de_muestra(muestras, id_muestra):
    muestra = buscar_muestra(muestras, id_muestra)
    lista_analisis = []
    if muestra is None:
         return lista_analisis
    analisis_de_muestra = muestra.get("analisis")
    for analisis in analisis_de_muestra:
        lista_analisis.append(analisis.get("codigo"))
    return lista_analisis

def total_analisis(muestras):
    suma_total_analisis = 0
    for muestra in muestras:
        suma_total_analisis +=len(muestra.get("analisis"))
    return suma_total_analisis

def veces_por_analisis(muestras):
    dicc_cantidad_veces_analisis = {}
    for muestra in muestras:
        analisis_muestra = muestra.get("analisis")
        for analisis in analisis_muestra:
            codigo_analisis = analisis.get("codigo")
            dicc_cantidad_veces_analisis[codigo_analisis] = dicc_cantidad_veces_analisis.get(codigo_analisis,0)+1
    return dicc_cantidad_veces_analisis

def reporte_muestra(muestra, catalogo):
    lista_reporte = []
    analisis_de_muestra = muestra.get("analisis")
    for analisis in analisis_de_muestra:
        codigo_analisis = analisis.get("codigo")
        recuento_analisis = analisis.get("recuento")
        analisis_en_catalogo = catalogo.get(codigo_analisis)
        if analisis_en_catalogo is None:
            lista_reporte.append(f"El codigo: {codigo_analisis} no se encuentra asociado a ningun analisis en el sistema, recuento: {recuento_analisis}")
            continue
        nombre_analisis_catalogo = analisis_en_catalogo.get("nombre")
        unidades_analisis_catalogo = analisis_en_catalogo.get("unidad")
        lista_reporte.append(f"{nombre_analisis_catalogo}: {recuento_analisis} {unidades_analisis_catalogo}")
    return lista_reporte

assert codigos_de_muestra(MUESTRAS, "M-0003") == ["A01", "A03"]
assert codigos_de_muestra(MUESTRAS, "M-9999") == []
assert total_analisis(MUESTRAS) == 5
assert total_analisis([]) == 0
assert veces_por_analisis(MUESTRAS) == {"A01": 2, "A02": 2, "A03": 1}
assert reporte_muestra(MUESTRAS[0], CATALOGO_ANALISIS) == [
    "Aerobios mesófilos: 150000 UFC/g",
    "Enterobacterias: 50 UFC/g",
]

muestra_con_codigo_desconocido = {
    "id": "M-0004", "cliente": "1234", "estado": "enviada",
    "analisis": [{"codigo": "A01", "recuento": 500}, {"codigo": "A99", "recuento": 30}],
}

assert reporte_muestra(muestra_con_codigo_desconocido, CATALOGO_ANALISIS) == [
    "Aerobios mesófilos: 500 UFC/g",
    "El codigo: A99 no se encuentra asociado a ningun analisis en el sistema, recuento: 30",
]

print("Todas las pruebas pasaron")

