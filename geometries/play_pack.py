import tkinter as tk

root = tk.Tk()
root.title("playing with pack")
root.pack_propagate(False)

for n in range(1, 5):
  lbl = tk.Label(root, text=f'Soy la etiqueta {n}', relief=tk.GROOVE)
  lbl.pack(side=tk.TOP, expand=True, fill=tk.X )

root.mainloop()


