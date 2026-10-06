
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