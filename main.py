# Métodos estáticos y métodos de clase

# Método estático -> Son métodos que pertenecen a una clase y no a los objetos instanciados de una clase

# Método de clase -> Método que permite realizar operaciones relacionadas con la clase propia
#   - Recibe (cls) como primer parámetro, el cuál representa a la clase

# Comparación
# Métodos de instancia -> operaciones de instancias de clase (objetos)
# Métodos de clase -> Métodos que requieren acceso a la clase
# Métodos estáticos -> Métodos que representan utilidades

from abc import ABC

class GMF:
    gmf = 0.004

    @classmethod
    def calcular_gmf(cls, valor):
        return cls.gmf * valor
    
    @staticmethod
    def nuevo_calc_gmf(valor):
        return 0.004 * valor
    

class Asociado(ABC):
    total_asociados = 0

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        Asociado.total_asociados += 1

    @classmethod
    def crear_asociado_por_edad(cls, nombre, edad, asociado = None):
        if edad >= 18:
            return Dependiente(nombre, edad)
        else:
            return Cooprokids(nombre, edad, asociado)
        
    @classmethod
    def obtener_estadisticas(cls):
        return {
            "total": cls.total_asociados,
            "nombre_clase": cls.__name__
        }
        
    @staticmethod
    def retiro_aportes(valor):
        gmf = GMF.calcular_gmf(valor)
        return valor + gmf
    
    @staticmethod
    def validar_cedula(cedula):
        if not isinstance(cedula, str):
            return False
        if not cedula.isdigit():
            return False
        return 8 <= len(cedula) <= 10


class Dependiente(Asociado):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)

class Cooprokids(Asociado):
    def __init__(self, nombre, edad, asociado):
        super().__init__(nombre, edad)
        self.asociado = asociado


dependiente = Asociado.crear_asociado_por_edad("Karolina", 44)
coop = Asociado.crear_asociado_por_edad("Duber", 15)

print(Asociado.retiro_aportes(200000))

