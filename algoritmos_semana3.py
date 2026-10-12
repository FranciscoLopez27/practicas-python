MUESTRAS = [
    {"id": "M-0001", "cliente": "0042", "estado": "enviada"},
    {"id": "M-0002", "cliente": "1234", "estado": "liberada"},
    {"id": "M-0003", "cliente": "0042", "estado": "confirmada"},
    {"id": "M-0004", "cliente": "0042", "estado": "enviada"},
    {"id": "M-0005", "cliente": "5678", "estado": "liberada"},
]

RESULTADOS = [
    {"id": "M-0001", "analisis": "A01", "recuento": 150000},
    {"id": "M-0001", "analisis": "A02", "recuento": 50},
    {"id": "M-0002", "analisis": "A02", "recuento": 900},
    {"id": "M-0003", "analisis": "A01", "recuento": 2000},
    {"id": "M-0004", "analisis": "A03", "recuento": 10},
]

LIMITES = {"A01": 100000, "A02": 100, "A03": 10}
ESTADOS_POSIBLES_MUESTRAS = ("enviada", "confirmada", "liberada")

def agrupar_por_estado(muestras):
    por_estado = {}
    for muestra in muestras:
        if muestra["estado"] not in ESTADOS_POSIBLES_MUESTRAS:
            por_estado.setdefault("invalido", []).append(muestra["id"])
        else:
            por_estado.setdefault(muestra["estado"], []).append(muestra["id"])
    return por_estado

assert agrupar_por_estado(MUESTRAS) == {
    "enviada": ["M-0001", "M-0004"],
    "liberada": ["M-0002", "M-0005"],
    "confirmada": ["M-0003"],
}

def fuera_de_norma_por_analisis(resultados, limites):
    resultados_fuera_norma = {}
    for resultado in resultados:
        codigo = resultado["analisis"]
        limite_analisis = limites.get(codigo)
        #Si hay un analisis que no tiene limite se toma como correcto independientemente del resultado de conteo
        if limite_analisis is None:
            continue
        elif limite_analisis < resultado["recuento"]:
            resultados_fuera_norma[codigo] = resultados_fuera_norma.get(codigo, 0) + 1
    return resultados_fuera_norma

MUESTRAS_PRUEBA_MAL = [
    {"id": "M-0001", "cliente": "0042", "estado": "enviada"},
    {"id": "M-0002", "cliente": "1234", "estado": "liberada"},
    {"id": "M-0003", "cliente": "0042", "estado": "rechazada"},
    {"id": "M-0004", "cliente": "0056", "estado": "rechazada"},
]

assert agrupar_por_estado([]) == {}
assert agrupar_por_estado(MUESTRAS_PRUEBA_MAL) == {
    "enviada": ["M-0001"],
    "liberada": ["M-0002"],
    "invalido": ["M-0003", "M-0004"]
}


RESULTADOS_2 = [
    {"id": "M-0001", "analisis": "A01", "recuento": 150000},
    {"id": "M-0001", "analisis": "A02", "recuento": 50},
    {"id": "M-0002", "analisis": "A02", "recuento": 900},
    {"id": "M-0003", "analisis": "A01", "recuento": 2000},
    {"id": "M-0004", "analisis": "A03", "recuento": 10},
    {"id": "M-0005", "analisis": "A01", "recuento": 1000000},
    {"id": "M-0006", "analisis": "A03", "recuento": 1000000},
]

RESULTADOS_3 = [
    {"id": "M-0001", "analisis": "A01", "recuento": 150000},
    {"id": "M-0001", "analisis": "A02", "recuento": 50},
    {"id": "M-0002", "analisis": "A02", "recuento": 900},
    {"id": "M-0003", "analisis": "A01", "recuento": 2000},
    {"id": "M-0004", "analisis": "A03", "recuento": 10},
    {"id": "M-0005", "analisis": "A06", "recuento": 1000000},
    {"id": "M-0006", "analisis": "A01", "recuento": 150000},
    {"id": "M-0007", "analisis": "A02", "recuento": 1000},
]


assert fuera_de_norma_por_analisis(RESULTADOS, LIMITES) == {"A01": 1, "A02": 1}
assert fuera_de_norma_por_analisis(RESULTADOS_2, LIMITES) == {"A01": 2, "A02": 1, "A03": 1}
assert fuera_de_norma_por_analisis(RESULTADOS_3, LIMITES) == {"A01": 2, "A02": 2}
assert fuera_de_norma_por_analisis([], LIMITES) == {}

from collections import Counter
def cliente_con_mas_muestras(muestras):
    if not muestras:
        return []
    contador_codigos = Counter([muestra["cliente"] for muestra in muestras])
    maximas_repeticiones = contador_codigos.most_common(1)[0][1]
    clientes_mas_frecuentes = [cliente for cliente, conteo in contador_codigos.items() if conteo == maximas_repeticiones]
    return clientes_mas_frecuentes


MUESTRAS_1 = []
MUESTRAS_2 = [
    {"id": "M-0001", "cliente": "0042", "estado": "enviada"},
    {"id": "M-0002", "cliente": "1234", "estado": "liberada"},
    {"id": "M-0003", "cliente": "0042", "estado": "confirmada"},
    {"id": "M-0004", "cliente": "0042", "estado": "enviada"},
    {"id": "M-0005", "cliente": "5678", "estado": "liberada"},
    {"id": "M-0006", "cliente": "5678", "estado": "liberada"},
    {"id": "M-0005", "cliente": "5678", "estado": "liberada"},
]

assert cliente_con_mas_muestras(MUESTRAS) == ["0042"]
assert cliente_con_mas_muestras(MUESTRAS_1) == []
assert cliente_con_mas_muestras(MUESTRAS_2) == ["0042", "5678"]