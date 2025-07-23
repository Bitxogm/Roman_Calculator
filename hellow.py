import tkinter as tk

root = tk.Tk()

root.title("Hellow")
root.geometry("800x600")
lbl = tk.Label( root, text='hola bitxo')
lbl.place(x=380, y=290 )

btn = tk.Button(root, text='Click here', command=lambda : lbl.config(text='Clickado'))
btn.place(x=380, y=135)
root.mainloop()

