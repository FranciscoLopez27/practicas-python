
def hay_ids_repetidos(lista_ids):
    set_de_ids = set()
    for id_muestra in lista_ids:
        if id_muestra in set_de_ids:
            return True
        else:
            set_de_ids.add(id_muestra)
    return False

assert hay_ids_repetidos(["M-01", "M-02", "M-03"]) is False
assert hay_ids_repetidos(["M-01", "M-02", "M-01"]) is True
assert hay_ids_repetidos(["M-01", "M-02", "M-03", "M-03"]) is True   # repetido al final
assert hay_ids_repetidos([]) is False                                # lista vacía
assert hay_ids_repetidos(["M-01"]) is False                          # un solo elemento


def hay_ids_repetidos_una_linea(lista_ids):
    return len(lista_ids) != len(set(lista_ids))

###Codigo para el proyecto
UNIDADES_VALIDAS = {"UFC/g", "UFC/ml", "UFC/swab", "NMP/g", "NMP/ml"}
CLIENTES_REGISTRADOS = {"0042", "1234", "5678"}
UNIDADES_VALIDAS_MINUSCULAS = set()

for unidad in UNIDADES_VALIDAS:
    UNIDADES_VALIDAS_MINUSCULAS.add(unidad.lower())


def es_unidad_valida(unidad):
    return unidad.lower() in UNIDADES_VALIDAS_MINUSCULAS


def es_cliente_valido(cliente):
    return len(cliente) == 4 and cliente.isdigit() and cliente in CLIENTES_REGISTRADOS 

# Unidades
assert es_unidad_valida("UFC/g") is True
assert es_unidad_valida("NMP/ml") is True
assert es_unidad_valida("mg/kg") is False      # unidad no permitida
assert es_unidad_valida("") is False           # vacía
print("es_unidad_valida: todas las pruebas pasaron")

# Clientes
assert es_cliente_valido("0042") is True       # registrado, con ceros a la izquierda
assert es_cliente_valido("1234") is True
assert es_cliente_valido("9999") is False      # formato correcto, pero no registrado
assert es_cliente_valido("42") is False        # muy corto
assert es_cliente_valido("12345") is False     # muy largo
assert es_cliente_valido("12a4") is False      # contiene una letra
assert es_cliente_valido("") is False          # vacío
print("es_cliente_valido: todas las pruebas pasaron")