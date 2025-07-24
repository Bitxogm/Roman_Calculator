from outer_lib.roman_number import RomanNumber as rn
from enum import Enum, auto


class OPERATION(Enum):
    ADD = "+"
    SUB = "-"
    MUL = "x"
    DIV = "/"
    MOD = "%"

    def calcular(self, num1, num2):
        if self == OPERATION.ADD:
            resultado = num1 + num2
        elif self == OPERATION.SUB:
            resultado = num1 - num2
        elif self == OPERATION.MUL:
            resultado = num1 * num2
        elif self == OPERATION.DIV:
            resultado = num1 / num2
        elif self == OPERATION.MOD:
            resultado = num1 % num2
        return resultado


"""Clase Calculo

    Atrivbutos
    n1: RomanNumber
    n2: RomanNumber
    op: OPERATION
    resultado : RomanNuber
    estado : STATUS_CALCULO --> Enum

    metodos:
    add_char(label:str)
    acumular_n1(RomanNumber | str)
    acumular_n2(RomanNumber | str)
    guardar_operation(value: OPERATION | str)
    hacer_calculo()
"""


class STATUS_CALCULO(Enum):
    WAITING_N1 = auto()
    WAITING_OP = auto()
    WAITING_N2 = auto()
    WAITING_SOLUTION = auto()


class Calculo:
    @staticmethod
    def _concatenar(num: rn, cad: str):
        '''
        1. extraer cadena de num1
        2. concatenar con cadena value
        3. asignar a num1 como rn
        '''
        rom_cadena = num.cadena
        tot_cadena = rom_cadena + cad
        result = rn(tot_cadena)
        return result

    def __init__(self):
        self.num1 = None
        self.num2 = None
        self.operation = None
        self.status = STATUS_CALCULO.WAITING_N1
        self.resultado = None

    def _select_operation(self, operation: OPERATION | None) -> None:
        if self.num1 is not None and self.num2 is None:
            self.operation = operation
            self.status = STATUS_CALCULO.WAITING_N2
        elif self.num2 is not None:
            self.num1 = self.operation.calcular(self.num1, self.num2)
            self.operation = operation
            self.num2 = None
            self.status = STATUS_CALCULO.WAITING_N2


    def add_char(self, value: str):
        try:
            if value in [op.value for op in OPERATION]:
                self._select_operation(OPERATION(value))
                
        
            elif value == "=" and self.num1 and self.num2 and self.operation:
                self.num1 = self.operation.calcular(self.num1, self.num2)
                self.num2 = None
                self.operation = None
                self.status = STATUS_CALCULO.WAITING_OP
            elif value == "clear":
                self.num1 = self.num2 = self.operation = self.resultado = None
                self.status = STATUS_CALCULO.WAITING_N1
            
            elif self.status == STATUS_CALCULO.WAITING_OP:
                self.num1 = self._concatenar(self.num1, value)
            elif self.status == STATUS_CALCULO.WAITING_N1:
                self.num1 = rn(value)
                self.status = STATUS_CALCULO.WAITING_OP
            elif self.status == STATUS_CALCULO.WAITING_N2:
                self.num2 = rn(value)
                self.status = STATUS_CALCULO.WAITING_SOLUTION
            else:
                self.num2 = self._concatenar(self.num2, value)


        except ValueError:
            pass
        