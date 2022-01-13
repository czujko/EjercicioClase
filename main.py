lista = []
nombre = input("Introduce un nombre: ").capitalize()
while nombre != "0":
    lista.append(nombre)
    nombre = input("Introduce un nombre: ").capitalize()
print("Lista de nombres:", lista)

nombre = input("Introduce un nombre para eliminar: ").capitalize()
while nombre != '0':
    lista.remove(nombre)
    nombre = input("Introduce un nombre para eliminar: ").capitalize()

print("Lista de nombres:", lista)
