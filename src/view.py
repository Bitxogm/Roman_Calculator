import tkinter as tk
# --- Jerarquía de widgets ---
# -root --> ventana que contiene la aplicación
  #Calculator : control de la calculadora
    #Display : Pantalla
#   -Keyboard: Teclado con n teclas
#     -[CalcButtons]



WIDTH_BUTTON = 90
HEIGHT_BUTTON = 50
# Clase CalcButton 
class CalcButton(tk.Frame):
    def __init__(self, parent, text : str, clicked):
        super().__init__(parent, width=WIDTH_BUTTON, height=HEIGHT_BUTTON) 
        self.pack_propagate(False) 
        self.btn = tk.Button(self, text=text,  command= lambda: clicked(text) )
        self.btn.pack(fill=tk.BOTH, expand=True) 
        self.text = text

    def _click(self):
        self.btn.invoke()



# Clase Keyboard 
class Keyboard(tk.Frame):
    def __init__(self, parent, clicked_button, rows=5, cols=3, labels = None):
        super().__init__(parent, width= cols * WIDTH_BUTTON, height= rows * HEIGHT_BUTTON) 
        if labels :
            self.labels = labels

        self.buttons = [
            ('Clear', 0, 0), ('I', 1, 0), ('X', 2, 0), ('c', 3, 0), ('M', 4, 0), # Columna 0
            ('%', 0, 1), ('V', 1, 1), ('L', 2, 1), ('D', 3, 1), ('·', 4, 1), # Columna 1
            ('/', 0, 2), ('*', 1, 2), ('-', 2, 2), ('+', 3, 2), ('=', 4, 2)  # Columna 2
        ]

        self.clicked_buttons = clicked_button
      
        for i in range(3): # Para las 3 columnas de botones
            self.grid_columnconfigure(i, weight=1)
        for i in range(5): # Para las 5 filas de botones
            self.grid_rowconfigure(i, weight=1)

        # Crear y colocar cada CalcButton dentro del grid de este Keyboard
        for text, row, column in self.buttons:
            # Creamos una instancia  CalcButton, siendo 'self' su padre
            button = CalcButton(self, text=text, clicked=clicked_button)
            # Colocamos el botón en el grid de este Keyboard
            button.grid(row=row, column=column, sticky='nsew', padx=3, pady=3)

    def _click(self, label: str):
        self.clicked_buttons(label)
   


            



#Class Display
class Display(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, width=WIDTH_BUTTON*3, height=HEIGHT_BUTTON*2)
        self.pack_propagate(False)
        self.label = tk.Label(self, text="", bg='black', fg='white', anchor=tk.E, font=("Arial", 24, "bold"))
        self.label.pack(fill=tk.BOTH, expand=True)

    def get_text(self):
        return self.label.cget("text")

    def set_text(self, value : str):
        self.label["text"] = value

class Calculator(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.display = Display(self)
        self.display.pack()
        self._clicked = None
        self.keywoard = Keyboard(self, self.__on_click)
        self.keywoard.pack()

    def set_text(self, text: str ):
        self.display.set_text(text)

    def __on_click(self, text: str):
        # self._clicked(text)
        if text == 'Clear':
            self.display.set_text("")
        else:
            current = self.display.get_text()
            self.display.set_text(current + text)

    def set_clicked(self, clicked: callable):
        self._clicked = clicked

        

# Funciones de manejo de eventos  
def get_value(value: str , display_instance: Display):
    print(f'get_value recibe el valor de "{value}"')

    if value == 'Clear':
        display_instance.set_text("")
    else:
        text = display_instance.get_text()
        display_instance.set_text(text + value)

def ha_sido_pulsado( label:str, display_instance):
    print(f'**** {label} ***')
    get_value(label, display_instance)







# Configuración de la aplicación principal
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Roman Calculator") 
    root.geometry("480x280") 

# Configuracion de columns y rows
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)


#Crear instacia del Display y colocar en root 
    show_display = Display(root)
    show_display.grid(row=0, column=0, sticky="nsew", padx=5, pady=5) 

# Creamo sinstancia del teclado y colocarla en la ventana principal
# 'root' es el padre del 'keyboard', y le pasamos la función que manejará los clics
    keyboard = Keyboard(root, lambda click_value: ha_sido_pulsado(click_value, show_display))
# Colocamos el 'keyboard' en la fila 0, columna 0 del grid de 'root'
    keyboard.grid(row=1, column=0, sticky="nsew", padx=3, pady=3) 
    root.mainloop()


