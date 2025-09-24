from abc import ABC
import datetime
from decimal import Decimal


class Cuenta(ABC):
    # Variable de clase para numeración secuencial
    siguiente_numero_cuenta = 100001
    
    def __init__(self, id_propietario, saldo_inicial=0):
        self.numero_cuenta = Cuenta.siguiente_numero_cuenta
        Cuenta.siguiente_numero_cuenta += 1
        self.id_propietario = id_propietario
        self.saldo = Decimal(str(saldo_inicial))
        self.fecha_creacion = datetime.now()
    
    # MÉTODO DE CLASE 1: Método fábrica para crear cuentas por tipo
    @classmethod
    def crear_cuenta_por_tipo(cls, tipo_cuenta, id_propietario, saldo_inicial=0):
        """Método fábrica para crear diferentes tipos de cuenta"""
        if tipo_cuenta.upper() == 'AHORROS':
            return CuentaAhorros(id_propietario, saldo_inicial)
        elif tipo_cuenta.upper() == 'CREDITO':
            return CuentaCredito(id_propietario, saldo_inicial)
        else:
            raise ValueError(f"Tipo de cuenta no válido: {tipo_cuenta}")
    
    # MÉTODO DE CLASE 2: Generar reporte de cuentas existentes
    @classmethod
    def obtener_reporte_cuentas(cls):
        """Retorna información sobre las cuentas creadas"""
        return {
            'siguiente_numero_cuenta': cls.siguiente_numero_cuenta,
            'total_cuentas_creadas': cls.siguiente_numero_cuenta - 100001
        }
    
    # MÉTODO DE CLASE 3: Configurar parámetros globales de cuenta
    @classmethod
    def configurar_parametros_cuenta(cls, tarifa_mantenimiento, saldo_minimo):
        """Configura tarifas y montos mínimos para todas las cuentas"""
        cls.tarifa_mantenimiento = tarifa_mantenimiento
        cls.saldo_minimo = saldo_minimo
        return f"Configuración actualizada para {cls.__name__}"
    
    # MÉTODO DE CLASE 4: Obtener siguiente número disponible sin crear cuenta
    @classmethod
    def previsualizar_siguiente_numero_cuenta(cls):
        """Retorna el próximo número de cuenta sin incrementar el contador"""
        return cls.siguiente_numero_cuenta
    
    # MÉTODO ESTÁTICO 1: Validar número de cuenta bancaria colombiana
    @staticmethod
    def validar_formato_cuenta(numero_cuenta):
        """Valida formato de cuenta bancaria (10-20 dígitos)"""
        if not isinstance(numero_cuenta, (str, int)):
            return False
        cuenta_str = str(numero_cuenta)
        if not cuenta_str.isdigit():
            return False
        return 10 <= len(cuenta_str) <= 20
    
    # MÉTODO ESTÁTICO 2: Convertir pesos colombianos a salarios mínimos
    @staticmethod
    def pesos_a_salarios_minimos(cantidad, salario_minimo_actual=1300000):
        """Convierte cantidad en pesos a salarios mínimos colombianos"""
        return Decimal(str(cantidad)) / Decimal(str(salario_minimo_actual))


class CuentaAhorros(Cuenta):
    # Variables de clase específicas
    tasa_interes = 0.02
    max_retiros_mensuales = 6
    
    # MÉTODO DE CLASE específico: Actualizar tasa de interés
    @classmethod
    def actualizar_tasa_interes(cls, nueva_tasa):
        """Actualiza la tasa de interés para todas las cuentas de ahorro"""
        tasa_anterior = cls.tasa_interes
        cls.tasa_interes = nueva_tasa
        return f"Tasa actualizada de {tasa_anterior:.2%} a {nueva_tasa:.2%}"
    
    # MÉTODO DE CLASE específico: Configurar políticas de retiro
    @classmethod
    def configurar_politica_retiro(cls, max_retiros):
        """Configura límite de retiros mensuales para cuentas de ahorro"""
        cls.max_retiros_mensuales = max_retiros
        return f"Límite de retiros configurado: {max_retiros} por mes"
    
    # MÉTODO ESTÁTICO específico: Calcular rendimiento cuenta de ahorros
    @staticmethod
    def calcular_interes_mensual(saldo, tasa_anual=0.02):
        """Calcula interés mensual para cuenta de ahorros (EA típica 2%)"""
        tasa_mensual = Decimal(str(tasa_anual)) / 12
        return saldo * tasa_mensual


class CuentaCredito(Cuenta):
    # Variables de clase para políticas de crédito
    tasa_credito_predeterminada = 0.24
    limite_credito_maximo = 50000000  # 50 millones COP
    
    def __init__(self, id_propietario, limite_credito):
        super().__init__(id_propietario, 0)
        self.limite_credito = Decimal(str(limite_credito))
        self.credito_usado = Decimal('0')
    
    # MÉTODO DE CLASE específico: Actualizar tasa de crédito
    @classmethod
    def actualizar_tasa_credito(cls, nueva_tasa):
        """Actualiza tasa de interés para créditos nuevos"""
        tasa_anterior = cls.tasa_credito_predeterminada
        cls.tasa_credito_predeterminada = nueva_tasa
        return f"Tasa de crédito actualizada de {tasa_anterior:.1%} a {nueva_tasa:.1%}"
    
    # MÉTODO DE CLASE específico: Configurar límite máximo
    @classmethod
    def configurar_limite_credito_maximo(cls, nuevo_limite):
        """Establece límite máximo de crédito institucional"""
        cls.limite_credito_maximo = nuevo_limite
        return f"Límite máximo de crédito: ${nuevo_limite:,} COP"
    
    # MÉTODO ESTÁTICO específico: Calcular cuota de crédito
    @staticmethod
    def calcular_cuota_mensual(principal, tasa_anual, meses):
        """Calcula cuota mensual de crédito usando fórmula francesa"""
        tasa_mensual = Decimal(str(tasa_anual)) / 12
        if tasa_mensual == 0:
            return principal / meses
        
        numerador = principal * tasa_mensual * ((1 + tasa_mensual) ** meses)
        denominador = ((1 + tasa_mensual) ** meses) - 1
        return numerador / denominador
    
interes_mensual = CuentaAhorros.calcular_interes_mensual(Decimal('1000000'))
cuota_credito = CuentaCredito.calcular_cuota_mensual(
    Decimal('5000000'), 0.24, 36  # 5M pesos, 24% EA, 36 meses
)

