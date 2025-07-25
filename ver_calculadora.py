import tkinter as tk
from src.view import Display, Keyboard, Calculator

root = tk.Tk()
calc = Calculator(root)
calc.pack()

root.mainloop()