import pytest
from src.model import OPERATION, STATUS_CALCULO, Calculo, rn

@pytest.mark.parametrize(
    "op1, op2, operation, resultado",
    [
        (1, 1, OPERATION.ADD, 2),
        (1, 1, OPERATION.SUB, 0),
        (1, 1, OPERATION.MUL, 1),
        (1, 2, OPERATION.DIV, 0.5),
        (10, 3, OPERATION.MOD, 1)
    ]
)
def test_operations(op1, op2, operation, resultado):
    assert operation.calcular(op1, op2) == resultado


def test_crear_calculo():
    calc = Calculo()
    assert calc.num1 is None
    assert calc.num2 is None
    assert calc.operation is None
    assert calc.status == STATUS_CALCULO.WAITING_N1
    assert calc.resultado is None
    
@pytest.mark.parametrize(
        "char, num1, num2, operation, status, resultado",
        [
            ("V", rn(5), None, None, STATUS_CALCULO.WAITING_OP, None),
            ("+", None, None, None, STATUS_CALCULO.WAITING_N1, None),
            ("=", None, None, None, STATUS_CALCULO.WAITING_N1, None),
        ]
)
def test_add_char(char, num1, num2, operation, status, resultado):
    calc = Calculo()
    calc.add_char(char)

    assert calc.num1 == num1
    assert calc.num2 == num2
    assert calc.operation == operation
    assert calc.status == status
    assert calc.resultado == resultado


@pytest.mark.parametrize(
    "ini, cadena, num1, num2, operation, resultado, status",
    [
        ("V", "I", rn(6), None, None, None, STATUS_CALCULO.WAITING_OP),
        ("I", "V", rn(4), None, None, None, STATUS_CALCULO.WAITING_OP),
        ("V", "+", rn(5), None, OPERATION.ADD, None, STATUS_CALCULO.WAITING_N2),
        ("V", "=", rn(5), None, None, None, STATUS_CALCULO.WAITING_OP)
    ]
)
def test_add_char_en_estado_EOP(ini, cadena, num1, num2, operation, resultado, status):
    # preparacion del test
    calc = Calculo()
    calc.add_char(ini)

    # realizar el test
    calc.add_char(cadena)

    # revisamos resultados (asserts)
    assert calc.num1 == num1
    assert calc.num2 == num2
    assert calc.operation == operation
    assert calc.status == status
    assert calc.resultado == resultado

@pytest.mark.parametrize(
    "chars, cadena,num1, num2, operation, resultado, status",
    [
        ("VI+", "I", rn(6), rn(1), OPERATION.ADD, None, STATUS_CALCULO.WAITING_SOLUTION),
        ("VI+", "-", rn(6), None, OPERATION.SUB, None, STATUS_CALCULO.WAITING_N2),
        ("VI+", "=", rn(6), None, OPERATION.ADD, None, STATUS_CALCULO.WAITING_N2),
    ]
)
def test_add_char_en_estado_EN2(chars, cadena, num1, num2, operation, resultado, status):
    calc = Calculo()
    for char in chars:
        calc.add_char(char)

    # realizo el test
    calc.add_char(cadena)

    # verifico
    assert calc.num1 == num1
    assert calc.num2 == num2
    assert calc.operation == operation
    assert calc.status == status
    assert calc.resultado == resultado

@pytest.mark.parametrize(
    "chars, cadena, num1, num2, operation, resultado, status",
    [
        ("VI+I", "I", rn(6), rn(2), OPERATION.ADD, None, STATUS_CALCULO.WAITING_SOLUTION),
        ("VI+I", "-", rn(7), None, OPERATION.SUB, None, STATUS_CALCULO.WAITING_N2),
        ("VI+I", "=", rn(7), None, None, None, STATUS_CALCULO.WAITING_OP),
    ]
)
def test_add_char_en_estado_ESO(chars, cadena, num1, num2, operation, resultado, status):
    calc = Calculo()
    for char in chars:
        calc.add_char(char)

    # realizo el test
    calc.add_char(cadena)

    # verifico
    assert calc.num1 == num1
    assert calc.num2 == num2
    assert calc.operation == operation
    assert calc.status == status
    assert calc.resultado == resultado


def test_concatenar_IV():
    num1 = rn(1)

    assert Calculo._concatenar(num1, "V") == rn(4)

def test_atomic_bomb():
    calc = Calculo()
    calc.add_char("I")
    calc.add_char("+")
    calc.add_char("V")
    calc.add_char("clear")

    assert calc.num1 == None
    assert calc.num2 == None
    assert calc.operation == None
    assert calc.status == STATUS_CALCULO.WAITING_N1
    assert calc.resultado == None



    