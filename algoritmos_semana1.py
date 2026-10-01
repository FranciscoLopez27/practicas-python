def contar_fuera_limite(recuentos, limite):
    total_fuera_limite=0
    for recuento in recuentos:
        if recuento > limite:
            total_fuera_limite += 1
    return total_fuera_limite

assert contar_fuera_limite([120, 15000, 80, 3000], 1000) == 2
assert contar_fuera_limite([], 1000) == 0
assert contar_fuera_limite([1000], 1000) == 0
print("Ejercicio 1: todas las pruebas pasaron")

def promedio_recuentos(recuentos):
    contador=0
    suma_conteos=0
    for recuento in recuentos:
        if recuento >= 0:
            contador += 1
            suma_conteos += recuento
    if contador == 0:
        print("Sin datos validos")
        return None
    else:
        return suma_conteos/contador

assert promedio_recuentos([120, -5, 80]) == 100
assert promedio_recuentos([10, 200, 300, -400, -400, 200, 350, 3, 0, -600]) == 1063 / 7
assert promedio_recuentos([0, 0]) == 0              # ceros válidos: promedio 0, no None
assert promedio_recuentos([-5, -10]) is None        # sin datos válidos
assert promedio_recuentos([]) is None               # lista vacía
print("Ejercicio 2: todas las pruebas pasaron")

def hay_ids_repetidos(lista_ids):
    i=0
    repeticion_encontrada=False
    while i<=len(lista_ids)-1:
        j=i+1
        while j<= len(lista_ids)-1:
            if lista_ids[i]==lista_ids[j]:
                repeticion_encontrada=True
                return repeticion_encontrada
            j+=1
        i+=1
    return repeticion_encontrada

assert hay_ids_repetidos(["M-01", "M-02", "M-03"]) is False
assert hay_ids_repetidos(["M-01", "M-02", "M-01"]) is True
assert hay_ids_repetidos(["M-01", "M-02", "M-03", "M-03"]) is True   # repetido al final
assert hay_ids_repetidos([]) is False                                # lista vacía
assert hay_ids_repetidos(["M-01"]) is False                          # un solo elemento
print("Ejercicio 3: todas las pruebas pasaron")

def racha_fuera_de_rango(lista_temperaturas):
    i=0
    racha_maxima=0
    racha=0
    while i<= len(lista_temperaturas)-1:
        if lista_temperaturas[i]<35 or lista_temperaturas[i]>37:
            racha +=1
            if racha>racha_maxima:
                racha_maxima=racha
        else:
            racha=0
        i+=1
    return racha_maxima

assert racha_fuera_de_rango([36, 38, 39, 36, 34, 33, 32, 36]) == 3
assert racha_fuera_de_rango([36, 36, 37]) == 0       # todo dentro de rango
assert racha_fuera_de_rango([36, 38, 39, 40]) == 3   # racha al final
assert racha_fuera_de_rango([35, 37]) == 0           # en los bordes del rango: dentro
assert racha_fuera_de_rango([34, 38]) == 2           # bajo y sobre el rango cuentan igual
assert racha_fuera_de_rango([]) == 0                 # lista vacía
print("Ejercicio 4: todas las pruebas pasaron")

