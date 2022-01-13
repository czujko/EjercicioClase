nombre = input("Introduce un nombre: ")
if (nombre == "0"):
    print("No has introducido ningún nombre")
else:
    lista = []
    lista.append(nombre)
    nombre = input("Introduce un nombre: ")
    while nombre != "":
        lista.append(nombre)
        nombre = input("Introduce un nombre: ")
    print("Lista de nombres:", lista)

nombre = input("Introduce un nombre para eliminar: ")
if (nombre == 0):
    print("No has introducido ningún nombre")
else:
    lista.remove(nombre)
    print("Lista de nombres:", lista)
