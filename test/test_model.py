import pytest

from src.model import OPERATION , STATUS_CALCULO, Calculo , rn

@pytest.mark.parametrize(
  "op1, op2,  operation, result", [

    (1, 1, OPERATION.ADD, 2 ),
    (1, 1, OPERATION.SUB, 0 ),
    (1, 1, OPERATION.MUL,  1),
    (1, 2, OPERATION.DIV, 0.5 ),
    (10, 3, OPERATION.MOD, 1  ),
  ]
)

def test_operations(op1, op2, operation, result):
  assert operation.calcular(op1, op2 )  == result

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
            ("+", None, None, OPERATION.ADD, STATUS_CALCULO.WAITING_N1, None),
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
        ("V", "+", rn(5), None, OPERATION.ADD, None, STATUS_CALCULO.WAITING_N1),
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


def test_concatenar_IV():
    num1 = rn(1)
    assert Calculo._concatenar(num1, "V") == rn(4)

#Test para estado esperando n2 :
# @pytest.mark.parametrize(
#    "ini, cadena, segundo_numero, num1, num2, operation, resultado, status",
#    [
#       ("V", "+", "I", rn(5), rn(1), OPERATION.ADD, None, STATUS_CALCULO.WAITING_SOLUTION),
#    ]
# )


# def test_add_char_en_estado_EN2(ini, cadena, segundo_numero, num1, num2,operation, resultado, status):
   
#    # preparacion del test
#     calc = Calculo()
#     calc.add_char(ini)

#     # realizar el test
#     calc.add_char(cadena)

#     calc.add_char(segundo_numero)
#     assert calc.num1 == num1
#     assert calc.num2 == num2
#     assert calc.operation == operation
#     assert calc.resultado == resultado
#     assert calc.status == status