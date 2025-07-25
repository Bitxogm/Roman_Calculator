# Para hacer , el control visual tenemos que poder en una ventana
# Hacer del texto que tiene que mostrar. Podemos hacer metodo que sea set_text.
# Tendremos que crear un metod que nos diga lo que haye n pantalla

import pytest
import tkinter as tk
from random import randint
from src.view import Display, Calculator, CalcButton, Keyboard


@pytest.fixture
def root():
  _root = tk.Tk()
  _root.withdraw()
  yield _root # Devuelve los elementos como un generador , uno a uno . Se procesa cada item de uno en uno
  _root.destroy()

def test_Display_set_value(root):
  display = Display(root)
  assert display.get_text() == ""

  display.set_text('Hi, Otaku')
  assert display.get_text () == 'Hi, Otaku'


def test_create_calculator(root):
  calculator = Calculator(root)
  assert hasattr(calculator, "set_text")
  assert hasattr(calculator, "set_clicked")

  assert callable(getattr(calculator, "set_text"))
  assert callable(getattr(calculator, "set_clicked"))

def test_calculator_show_test(root):
  calculator = Calculator(root)
  assert calculator.display.get_text() == ""
  calculator.set_text("Hi, Otaku&Obama")
  assert calculator.display.get_text() == "Hi, Otaku&Obama"


def test_calculator_click(root):
  clicks = []
  calculator = Calculator(root)
  calculator.set_clicked(lambda x: clicks.append(x))
  calculator._clicked("I")
  calculator._clicked("V")

  assert clicks == ["I", "V"]
  
def test_click_CalButton(root):
  clicks = []

  cButton = CalcButton(root, "?", lambda x: clicks.append(x))
  nclicks = randint(3, 12)
  for i in range(nclicks):
    cButton._click()

  assert clicks == nclicks * ["?"]


def test_click_Keyboard(root):
  clicks = []
  kb  = Keyboard(root, lambda x: clicks.append(x), rows=2, cols=2, labels = [ "a", "d", "b,", "c"] )
  kb._click("a")
  kb._click("d")
  kb._click("b")
  kb._click("c")

  assert clicks ==  ["a", "d", "b", "c"]