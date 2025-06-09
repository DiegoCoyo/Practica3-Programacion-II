import json
from typing import Optional, List

class Medicamento:
    def __init__(self, nombre: str, codMedicamento: int, tipo: str, precio: float):
        self.nombre = nombre
        self.codMedicamento = codMedicamento
        self.tipo = tipo
        self.precio = precio
    
    def to_dict(self):
        return {
            "nombre": self.nombre,
            "codMedicamento": self.codMedicamento,
            "tipo": self.tipo,
            "precio": self.precio
        }

class Farmacia:
    def __init__(self, nombreFarmacia: str, sucursal: int, direccion: str):
        self.nombreFarmacia = nombreFarmacia
        self.sucursal = sucursal
        self.direccion = direccion
        self.medicamentos = []  
    
    def agregarMedicamento(self, medicamento: Medicamento):
        self.medicamentos.append(medicamento)
    
    def to_dict(self):
        return {
            "nombreFarmacia": self.nombreFarmacia,
            "sucursal": self.sucursal,
            "direccion": self.direccion,
            "medicamentos": [m.to_dict() for m in self.medicamentos]
        }

class ArchFarmacia:
    def __init__(self, na: str):
        self.na = na
    
    def crearArchivo(self):
        try:
            with open(self.na, 'w') as f:
                json.dump([], f)
        except IOError:
            print("Error, no se creo archivo.")
    
    def adicionar(self, farmacia: Farmacia):
        try:
            with open(self.na, 'r') as f:
                farmacias = json.load(f)
        except (IOError, json.JSONDecodeError):
            farmacias = []
        farmacias.append(farmacia.to_dict())
        try:
            with open(self.na, 'w') as f:
                json.dump(farmacias, f, indent=4)
        except IOError:
            print("Error, no se adiciono farmacia.")
    
    def listar(self):
        try:
            with open(self.na, 'r') as f:
                farmacias = json.load(f)
                for f in farmacias:
                    print(f"Nombre: {f['nombreFarmacia']}, Sucursal: {f['sucursal']}, Direccion: {f['direccion']}")
                    for m in f['medicamentos']:
                        print(f"  - Medicamento: {m['nombre']}, Codigo: {m['codMedicamento']}, Tipo: {m['tipo']}, Precio: {m['precio']}")
        except (IOError, json.JSONDecodeError):
            print("Error, no se listo la farmacia.")
    
    def mostrarMedicamentosResfrios(self):
        try:
            with open(self.na, 'r') as f:
                farmacias = json.load(f)
                for f in farmacias:
                    print(f"Nombre: {f['nombreFarmacia']}, Sucursal: {f['sucursal']}")
                    for m in f['medicamentos']:
                        if m['tipo'].lower() == 'resfriado':
                            print(f"  - Medicamento: {m['nombre']}, Precio: {m['precio']}")
        except (IOError, json.JSONDecodeError):
            print("Error, no se mostro medicamentos para resfriados")
    
    def mostrarMedicamentosMenorTos(self, precio: float):
        try:
            with open(self.na, 'r') as f:
                farmacias = json.load(f)
                for f in farmacias:
                    print(f"Nombre: {f['nombreFarmacia']}, Sucursal: {f['sucursal']}")
                    for m in f['medicamentos']:
                        if m['tipo'].lower() == 'tos' and m['precio'] < precio:
                            print(f"  - Medicamento: {m['nombre']}, Precio: {m['precio']}")
        except (IOError, json.JSONDecodeError):
            print("Error, no se mostro medicamentos para tos menores a", precio)
    
    def mostrarMedicamentosX(self, sucursal: int):
        try:
            with open(self.na, 'r') as f:
                farmacias = json.load(f)
                for f in farmacias:
                    if f['sucursal'] == sucursal:
                        print(f"Nombre: {f['nombreFarmacia']}, Sucursal: {f['sucursal']}, Dirección: {f['direccion']}")
                        for m in f['medicamentos']:
                            print(f"  - Medicamento: {m['nombre']}, Código: {m['codMedicamento']}, Tipo: {m['tipo']}, Precio: {m['precio']}")
        except (IOError, json.JSONDecodeError):
            print(f"Error, no se mostro medicamentos para sucursal {sucursal}")
    
    def buscaMedicamento(self, nombre: str):
        try:
            with open(self.na, 'r') as f:
                farmacias = json.load(f)
                for f in farmacias:
                    for m in f['medicamentos']:
                        if m['nombre'].lower() == nombre.lower():
                            return f["sucursal"], f["direccion"]
                return None
        except (IOError, json.JSONDecodeError):
            print(f"Error, no se busco el medicamento {nombre}.")
            return None


archivo = ArchFarmacia("farmacias.json")
archivo.crearArchivo()
    
farm1 = Farmacia("Farmacia San Pedro", 1, "Calle Pedregal")
farm1.agregarMedicamento(Medicamento("Golpex", 11, "Dolor", 3.50))
farm1.agregarMedicamento(Medicamento("Inyeccion", 12, "Resfrio", 5.60))
farm1.agregarMedicamento(Medicamento("Antigripal", 13, "Resfrio", 2.00))
    
farm2 = Farmacia("Farmacia UMSA", 2, "Calle Hernan Siles")
farm2.agregarMedicamento(Medicamento("Golpex", 14, "Dolor", 3.50))
farm2.agregarMedicamento(Medicamento("Paracetamol", 17, "Dolor", 2.00))
    
archivo.adicionar(farm1)
archivo.adicionar(farm2)
    
print("Lista de Farmacias:")
archivo.listar()
    
print("\nMedicamentos para sucursal 1:")
archivo.mostrarMedicamentosX(1)
    
print("\nSucursales con Golpex:")
resultado = archivo.buscaMedicamento("Golpex")
if resultado:
    sucursal, direccion = resultado
    print(f"Sucursal: {sucursal}, Dirección: {direccion}")
else:
    print("No se encontró Golpex.")
