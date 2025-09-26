"""
Usando la clase Perro, agregue el atributo eda y haga un menu con estas opciones:
1.- Crear 1 perro y agregarlos a uma lista de perros existente
2.- Mostrar los perros de la lista
3.- Fin
"""

class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

lista_perros = []
while True:
    print("1.- Crear 1 perro")
    print("2.- Mostrar los perros de la lista")
    print("3.- Fin")
    opcion = input("Seleccione una opcion: ")
    if opcion == "1":
        nombre = input("Ingrese el nombre del perro: ")
        edad = input("Ingrese la edad del perro: ")
        perro = Perro(nombre, edad)
        lista_perros.append(perro)
    elif opcion == "2":
        if not lista_perros:
            print("No hay perros en la lista.")
        else:
            print("Lista de perros: ")
            for i, perro in enumerate(lista_perros):
                print(f"{i+1}. Nombre: {perro.nombre}, Edad: {perro.edad}")
    elif opcion == "3":
        print ("Fin")
        break