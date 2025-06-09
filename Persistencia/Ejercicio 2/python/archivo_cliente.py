import json
from typing import Optional

class Cliente:
    def __init__(self, id: int, nombre: str, telefono: int):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono
    
    def to_dict(self):
        return {"id": self.id, "nombre": self.nombre, "telefono": self.telefono}

class ArchivoCliente:
    def __init__(self, nomA: str):
        self.nomA = nomA
    
    def crearArchivo(self) -> None:
        try:
            with open(self.nomA, 'w') as f:
                json.dump([], f)
        except IOError:
            print("Error, no se creo archivo.")
    
    def guardaCliente(self, c: Cliente) -> None:
        try:
            with open(self.nomA, 'r') as f:
                clientes = json.load(f)
        except (IOError, json.JSONDecodeError):
            clientes = []
        clientes.append(c.to_dict())
        try:
            with open(self.nomA, 'w') as f:
                json.dump(clientes, f, indent=4)
        except IOError:
            print("Error, no se guardo cliente.")
    
    def buscarCliente(self, c: int) -> Optional[Cliente]:
        try:
            with open(self.nomA, 'r') as f:
                clientes = json.load(f)
                for cl in clientes:
                    if cl["id"] == c:
                        return Cliente(cl["id"], cl["nombre"], cl["telefono"])
        except (IOError, json.JSONDecodeError):
            print("Error, no se busco cliente.")
        return None
    
    def buscarCelularCliente(self, c: int) -> Optional[Cliente]:
        try:
            with open(self.nomA, 'r') as f:
                clientes = json.load(f)
                for cl in clientes:
                    if cl["telefono"] == c:
                        return Cliente(cl["id"], cl["nombre"], cl["telefono"])
        except (IOError, json.JSONDecodeError):
            print("Error, no se busco por celular.")
        return None

archivo = ArchivoCliente("clientes.json")
archivo.crearArchivo()
archivo.guardaCliente(Cliente(1, "Miguel", 78321269))
archivo.guardaCliente(Cliente(2, "Joana", 65329670))
encontradoID = archivo.buscarCliente(1)
if encontradoID: print("Encontrado por ID:", encontradoID.id, encontradoID.nombre, encontradoID.telefono)
encontradoCelular = archivo.buscarCelularCliente(65329670)
if encontradoCelular: print("Encontrado por Celular:", encontradoCelular.id, encontradoCelular.nombre, encontradoCelular.telefono)
