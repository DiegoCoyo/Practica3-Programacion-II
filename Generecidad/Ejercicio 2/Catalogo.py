from typing import Generic, TypeVar

T = TypeVar('T')

class Libro:
    def __init__(self, titulo: str, autor: str):
        self.titulo = titulo
        self.autor = autor
    
    def __str__(self) -> str:
        return f"{self.titulo} - {self.autor}"

class Producto:
    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        self.precio = precio
    
    def __str__(self) -> str:
        return f"{self.nombre} - {self.precio} Bs"

class Catalogo(Generic[T]):
    def __init__(self):
        self.elementos = []
    
    def agregar(self, elemento: T) -> None:
        self.elementos.append(elemento)
    
    def buscar(self, indice: int) -> T:
        if indice < 0 or indice >= len(self.elementos):
            print("no permitido.")
            return None
        return self.elementos[indice]


libros = Catalogo[Libro]()
libros.agregar(Libro("Mañana llovera", "San DIego"))
libros.agregar(Libro("Vivir o Morir", "Dante Miguel"))
print(libros.buscar(0))
print(libros.buscar(1))
    
productos = Catalogo[Producto]()
productos.agregar(Producto("Tablet", 2100.0))
productos.agregar(Producto("Television", 5700.0))
print(productos.buscar(0))
print(productos.buscar(1))

