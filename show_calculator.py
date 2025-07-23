import tkinter as tk
from src.view import  Display, Keyboard , ha_sido_pulsado

root=tk.Tk()

show_dsp = Display(root)
show_dsp.pack()

kb = Keyboard(root, lambda click_value: ha_sido_pulsado(click_value, show_dsp))
kb.pack()

root.mainloop()