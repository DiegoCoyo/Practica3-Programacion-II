from typing import Generic, TypeVar
T = TypeVar('T')

class Caja(Generic[T]):
    def __init__(self):
        self.contenido = None
    
    def guardar(self, valor: T) -> None:
        self.contenido = valor
    
    def obtener(self) -> T:
        return self.contenido
    
texto = Caja()
texto.guardar("Buen dia ")

numero = Caja()
numero.guardar(78)

print(texto.obtener())    
print(numero.obtener())


