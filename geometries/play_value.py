import tkinter as tk

root = tk.Tk()
root.title("playing with Value")

for ix1 in range(4):
  lbl = tk.Label(root, text=f'Soy la label {ix1 + 1}')
  lbl.place(x=ix1 * 10, y=ix1  *20)

  root.mainloop()
