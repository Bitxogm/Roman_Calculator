# Para hacer , el control visual tenemos que poder en una ventana
# Hacer del texto que tiene que mostrar. Podemos hacer metodo que sea set_text.
# Tendremos que crear un metod que nos diga lo que haye n pantalla

import pytest
import tkinter as tk
from src.view import Display


@pytest.fixture
def root():
  _root = tk.Tk()
  _root.withdraw()
  yield _root # Devuelve los elementos como un generador , uno a uno . Se procesa cada item de uno en uno
  _root.destroy()

def test_Display_set_value(root):
  display = Display(root)
  assert display.get_text() == ''

  display.set_text('Hi, Otaku')
  assert display.get_text ()== 'Hi, Otaku'

