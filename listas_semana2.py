recuentos = [120, 15000, 80, 3000, 450, 80]

# 1. Primero, último, tres primeros y dos últimos
print("Primero: ", recuentos[0])
print("Ultimo: ", recuentos[-1])
print("Tres primeros: ", recuentos[:3])
print("Ultimos dos: ", recuentos[-2:])


# 2. Agregar 900 al final y 10 al comienzo
recuentos.append(900)
recuentos.insert(0, 10)
print("Después de agregar:", recuentos)

# 3. Eliminar el 15000 por valor y el último por posición
recuentos.remove(15000)
recuentos.pop()

print("Después de eliminar:", recuentos)

# 4. Ordenados de mayor a menor sin modificar la original

recuentos_copia = sorted(recuentos, reverse=True)
print("Lista original: ", recuentos )
print("Copia de la original, ordenada al reves: ",recuentos_copia)

# 5. Cuántas veces aparece 80 y posición del 3000

print("Cantidad de veces que aparece 80: ",recuentos.count(80))
print("Indice del numero 3000 en la lista",recuentos.index(3000))

# 6. Copia independiente

copia = recuentos.copy()
copia.append(39000)
print("Copia: ", copia)
print("Original: ", recuentos)