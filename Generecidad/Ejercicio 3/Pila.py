from typing import Generic, TypeVar

T = TypeVar('T')

class Pila(Generic[T]):
    def __init__(self):
        self.elementos = []
    
    def apilar(self, elemento: T) -> None:
        self.elementos.append(elemento)
    
    def desapilar(self) -> T:
        if not self.elementos:
            print("Vacio.")
            return None
        return self.elementos.pop()
    
    def mostrar(self) -> None:
        if not self.elementos:
            print("Vacio.")
            return
        for i in range(len(self.elementos) - 1, -1, -1):
            print(self.elementos[i])


pilaNum = Pila[int]()
pilaNum.apilar(1)
pilaNum.apilar(2)
pilaNum.apilar(3)
print("Pila 1:")
pilaNum.mostrar()
print("Desapilado:", pilaNum.desapilar())
pilaNum.mostrar()
    
pilaTexto = Pila[str]() 
pilaTexto.apilar("uno")
pilaTexto.apilar("dos")
pilaTexto.apilar("tres")
print("Pila 2:")
pilaTexto.mostrar()
print("Desapilado:", pilaTexto.desapilar())
pilaTexto.mostrar()

