CLIENTES = {"0042": "Lácteos del Sur", "1234": "Quesos Andinos", "5678": "Frutas del Valle"}

def nombre_cliente(codigo):
    return CLIENTES.get(codigo, "Cliente desconocido")

def codigo_cliente(nombre):
    return(next((codigo for codigo, nombre_cliente in CLIENTES.items() if nombre == nombre_cliente), None))
    
    for codigo, cliente in CLIENTES.items():
        if nombre == cliente:
            return codigo
    return None

def contar_por_cliente(codigos):
    diccionario_clientes = {}
    for codigo in codigos:
        diccionario_clientes[codigo] = diccionario_clientes.get(codigo, 0) + 1
    return diccionario_clientes


assert nombre_cliente("0042") == "Lácteos del Sur"
assert nombre_cliente("9999") == "Cliente desconocido"

assert codigo_cliente("Quesos Andinos") == "1234"
assert codigo_cliente("No existe") is None

assert contar_por_cliente(["0042", "1234", "0042", "0042"]) == {"0042": 3, "1234": 1}
assert contar_por_cliente([]) == {}
print("Todas las pruebas pasaron")