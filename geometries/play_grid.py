import tkinter as tk

root = tk.Tk()
root.title("playing with grid")

root.propagate(False)
ix = 1
for col in range(3):
  for row in range(4):
    lbl = tk.Label(root, text=f'soy la etiqueta {ix}')
    lbl.grid(column=col, row=row )
    ix+=1

root.mainloop()