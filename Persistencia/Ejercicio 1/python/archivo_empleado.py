import json
from typing import Optional, List

class Empleado:
    def __init__(self, nombre: str, edad: int, salario: float):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario
    
    def to_dict(self):
        return {"nombre": self.nombre, "edad": self.edad, "salario": self.salario}

class ArchivoEmpleado:
    def __init__(self, nombre: str):
        self.nombre = nombre
    
    def crearArchivo(self) -> None:
        try:
            with open(self.nombre, 'w') as f:
                json.dump([], f)
        except IOError:
            print("Error, el archivo no fue creadod.")
    
    def guardarEmpleado(self, e: Empleado) -> None:
        try:
            with open(self.nombre, 'r') as f:
                empleados = json.load(f)
        except (IOError, json.JSONDecodeError):
            empleados = []
        empleados.append(e.to_dict())
        try:
            with open(self.nombre, 'w') as f:
                json.dump(empleados, f, indent=4)
        except IOError:
            print("Error, no se guardo el empleado.")
    
    def buscaEmpleado(self, n: str) -> Optional[Empleado]:
        try:
            with open(self.nombre, 'r') as f:
                empleados = json.load(f)
                for e in empleados:
                    if e["nombre"] == n:
                        return Empleado(e["nombre"], e["edad"], e["salario"])
        except (IOError, json.JSONDecodeError):
            print("Error, no se busco el empleado.")
        return None
    
    def mayorSalario(self, sueldo: float) -> Optional[Empleado]:
        try:
            with open(self.nombre, 'r') as f:
                empleados = json.load(f)
                mayor = None
                for e in empleados:
                    if e["salario"] > sueldo:
                        if mayor is None or e["salario"] > mayor.salario:
                            mayor = Empleado(e["nombre"], e["edad"], e["salario"])
                return mayor
        except (IOError, json.JSONDecodeError):
            print("Error, no se busco al mayor salario.")
        return None


archivo = ArchivoEmpleado("empleados.json")
archivo.crearArchivo()
archivo.guardarEmpleado(Empleado("Diego", 20, 4000.0))
archivo.guardarEmpleado(Empleado("Antonio", 35, 6000.0))
encontrado = archivo.buscaEmpleado("Diego")
if encontrado: print("Encontrado:", encontrado.nombre, encontrado.edad, encontrado.salario)
mayor = archivo.mayorSalario(5000.0)
if mayor: print("Mayor salario:", mayor.nombre, mayor.edad, mayor.salario)
