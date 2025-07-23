
from outer_lib.f_romanos import de_arabigo_a_romano, de_romano_a_arabigo 

class RomanNumber:


    def __init__(self, value: str | int):
        if type(value) == str:
            self.cadena = value
            self.numero = de_romano_a_arabigo(value)
        else:
            self.numero = value
            self.cadena = de_arabigo_a_romano(value)

    def __repr__(self):
        return self.cadena
    
    def __str__(self):
        return self.__repr__()
    

    def __eq__(self, other):
        """
        Comparar los valores
        Devolver True si son iguales, False en otro caso
        """
        return self.numero == other.numero
    
    def __hash__(self):
        return hash((self.numero, self.cadena))

    def __add__(self, other):
        """
        1. sumar self y other
           si other es un numero entero (int)

        2. devolver instancia de RomanNumber con valor suma
        """
        if isinstance(other, int):
            valor_de_la_suma = self.numero + other
        elif isinstance(other, RomanNumber):
            valor_de_la_suma = self.numero + other.numero
        else:
            super().__add__(other)

        return RomanNumber(valor_de_la_suma)
    
    def __radd__(self, other):
        return self.__add__(other)
    
    def __sub__(self, other):
        if isinstance(other, int):
            resultado = self.numero - other
        elif isinstance(other, RomanNumber):
            resultado = self.numero - other.numero
        else:
            super().__add__(other)

        return RomanNumber(resultado)
    
    def __rsub__(self, other):
        if isinstance(other, int):
            return RomanNumber(other - self.numero)
        else:
            super().__rsub__(other)

    
    def __mul__(self, other):
        if isinstance(other, int):
            resultado = self.numero * other
        elif isinstance(other, RomanNumber):
            resultado = self.numero * other.numero
        else:
            super().__add__(other)

        return RomanNumber(resultado)
    
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __truediv__(self, other):
        if isinstance(other, int):
            resultado = self.numero // other
        elif isinstance(other, RomanNumber):
            resultado = self.numero // other.numero
        else:
            super().__add__(other)

        return RomanNumber(resultado)
    
    def __rtruediv__(self, other):
        if isinstance(other, int):
            return RomanNumber(other // self.numero)
        else:
            super().__rtruediv__(other)
    
    def __mod__(self, other):
        if isinstance(other, int):
            resultado = self.numero % other
        elif isinstance(other, RomanNumber):
            resultado = self.numero % other.numero
        else:
            super().__add__(other)

        return RomanNumber(resultado)
    
    def __rmod__(self, other):
        if isinstance(other, int):
            return RomanNumber(other % self.numero)
        else:
            super().__rtruediv__(other)
    

    def __pow__(self, other):
        if isinstance(other, int):
            resultado = self.numero ** other
        elif isinstance(other, RomanNumber):
            resultado = self.numero ** other.numero
        else:
            super().__add__(other)

        return RomanNumber(resultado)
    
    def __rpow__(self, other):
        if isinstance(other, int):
            return RomanNumber(other ** self.numero)
        else:
            super().__rtruediv__(other)



