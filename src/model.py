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
            resultado =  num1 * num2    
        elif self == OPERATION.DIV:
            resultado =  num1 / num2
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


    def add_char(self, value: str):

        for operation in OPERATION :
            if value == operation.value:
                self.operation = operation
                self.status = STATUS_CALCULO.WAITING_N1
                return
        try:
            if self.status == STATUS_CALCULO.WAITING_OP:
                self.num1 = self._concatenar(self.num1, value)
            else:
                self.num1 = rn(value)
            self.status = STATUS_CALCULO.WAITING_OP
        except ValueError:
            pass


                

