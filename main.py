lista = []
nombre = input("Introduce un nombre: ").lower()
while nombre != "0":
    lista.append(nombre)
    nombre = input("Introduce un nombre: ").lower()
print("Lista de nombres:", lista)

nombre = input("Introduce un nombre para eliminar: ").lower()
while nombre != '0':
    lista.remove(nombre)
    nombre = input("Introduce un nombre para eliminar: ").lower()

print("Lista de nombres:", lista)
