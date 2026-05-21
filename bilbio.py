# ==========================================
# Sistema de Biblioteca - Ejemplo práctico
creado por jhon
# ==========================================

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def prestar(self): # Cambia el estado del libro a prestado
        if self.disponible:
            self.disponible = False
            print(f"El libro '{self.titulo}' ha sido.")
        else:
            print(f"El libro '{self.titulo}' no está disponible.")

    def devolver(self):
        self.disponible = True
        print(f"El libro '{self.titulo}' ha sido devuelto.")

    def mostrar_info(self):
        estado = "Disponible" if self.disponible else "Prestado"
        print(f"Titulo: {self.titulo} | Autor: {self.autor} | Estado: {estado}")


class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"Libro '{libro.titulo}' agregado.")

    def mostrar_libros(self):
        if not self.libros:
            print("No hay libros en la biblioteca.")
        else:
            print("\nLista de libros:")
            for libro in self.libros:
                libro.mostrar_info()

    def prestar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                libro.prestar()
                return
        print("Libro no encontrado.")

    def devolver_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                libro.devolver()
                return
        print("Libro no encontrado.")


# =============================
# Programa principal
# =============================

def menu():
    biblioteca = Biblioteca()

    while True:
        print("\n--- MENU BIBLIOTECA ---")
        print("1. Agregar libro")
        print("2. Mostrar libros")
        print("3. Prestar libro")
        print("4. Devolver libro")
        print("5. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            titulo = input("Ingrese el titulo: ")
            autor = input("Ingrese el autor: ")
            libro = Libro(titulo, autor)
            biblioteca.agregar_libro(libro)

        elif opcion == "2":
            biblioteca.mostrar_libros()

        elif opcion == "3":
            titulo = input("Ingrese el titulo del libro a prestar: ")
            biblioteca.prestar_libro(titulo)

        elif opcion == "4":
            titulo = input("Ingrese el titulo del libro a devolver: ")
            biblioteca.devolver_libro(titulo)

        elif opcion == "5":
            print("Saliendo del sistema...")
            break

        else:
            print("Opcion invalida")


# Ejecutar programa
if __name__ == "__main__":
    menu()