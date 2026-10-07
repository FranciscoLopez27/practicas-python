def ids_fuera_de_norma(muestras, limite_conteo):
    
    return sorted(
        [id_muestras for id_muestras, recuento in muestras if recuento > limite_conteo]
        )

    muestras_fuera_limite = []
    for id_muestras, recuento in muestras:
        if recuento > limite_conteo:
            muestras_fuera_limite.append(id_muestras)
    return sorted(muestras_fuera_limite)

muestras = [("M-03", 15000), ("M-01", 120), ("M-04", 3000), ("M-02", 80)]

assert ids_fuera_de_norma(muestras, 1000) == ["M-03", "M-04"]
assert ids_fuera_de_norma(muestras, 100000) == []
assert ids_fuera_de_norma([("M-01", 1000)], 1000) == []     # igual al límite: no supera
assert ids_fuera_de_norma([], 1000) == []
print("Ejercicio 1: todas las pruebas pasaron")

def muestras_pendientes(recibidas, analizadas):
    set_analizadas = set(analizadas)
    return [muestra for muestra in recibidas if muestra not in set_analizadas]

recibidas = ["M-03", "M-01", "M-02", "M-05", "M-04"]
analizadas = ["M-04", "M-02"]

assert muestras_pendientes(recibidas, analizadas) == ["M-03", "M-01", "M-05"]
assert muestras_pendientes(recibidas, recibidas) == []
assert muestras_pendientes(recibidas, []) == recibidas
print("Ejercicio 2: todas las pruebas pasaron")


