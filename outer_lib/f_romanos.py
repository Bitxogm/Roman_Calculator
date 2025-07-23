diccionario = {
    "I": 1,
    "II": 2,
    "III": 3,
    "IV": 4,
    "V": 5,
    "VI": 6, 
    "VII": 7,
    "VIII": 8,
    "IX": 9,
    'X': 10,
    'XX': 20,
    "XXX": 30,
    "XL": 40,
    "L": 50,
    "LX": 60,
    "LXX": 70,
    "LXXX": 80,
    "XC" : 90,
    "C": 100,
    "CC": 200,
    "CCC": 300,
    "CD": 400,
    "D": 500,
    "DC": 600,
    "DCC": 700,
    "DCCC": 800,
    "CM": 900,
    "M": 1000,
    "MM": 2000,
    "MMM": 3000
}

THOUSAND_IND = "•"

def a_romano_menor_4000(n: int) -> str:
    componentes = descomponer(n) # [1000, 900, 70, 6]

    resultado = ""
    for n in componentes:
        for clave, valor in diccionario.items():
            if valor == n:
                resultado += clave
    
    return resultado

def de_arabigo_a_romano(n: int) -> str:
    if n < 0:
        raise ValueError("Solo enteros no negativos")
    groups = to_groups(n)

    result = ""
    for ix, group in enumerate(groups):
        if group == 0:
            continue    

        rvalue = a_romano_menor_4000(group)
        level_suffix = THOUSAND_IND * (len(groups) - ix - 1)
        result += rvalue + level_suffix

    return result

def descomponer(n: int) -> list:
    resultado = []
    for i in (1000, 100, 10):
        if n >= i:
            n_pos = n // i
            resultado.append(n_pos * i)
            n = n % i

    resultado.append(n)

    return resultado

def resta_permitida(valor, anterior):
    return (anterior == 100 and valor in (500, 1000)) or \
            (anterior == 10 and valor in (50, 100)) or \
            (anterior == 1 and valor in (5, 10))

def check_resta(anterior, valor, num_repes, resultado):
    es_resta = False
    if anterior > 0 and valor > anterior: # procesamos la resta si la hay
        order = get_order(resultado - anterior)

        if order and order < get_order(valor):
            raise ValueError("Ya no se puede restar")

        if num_repes == 1 and resta_permitida(valor, anterior):
            resultado = resultado - 2 * anterior
            es_resta = True
        else:
            raise ValueError("Orden incorrecto")
        
    return resultado, es_resta

def check_repes(valor, anterior, num_repes, letra):
    if valor == anterior: # comprobar si hay repeticion y la contamos
        num_repes += 1
    else:
        num_repes = 1

    if letra in ('V', 'L', 'D') and num_repes > 1 or num_repes > 3: # validamos el nuimero de repeticions
        raise ValueError(f"Demasiadas repeticiones de {letra}")
    
    return num_repes

def a_arabigo_menor_4000(romano: str) -> int:
    resultado = 0
    anterior = 0
    num_repes = 1
    es_resta = False
    
    for letra in romano:
        if letra in diccionario:
            valor = diccionario[letra] # obtenemos el valor de la letra

            if es_resta and get_order(resultado) <= get_order(valor):
                raise ValueError("Restas no permitidas")
         
            resultado, es_resta = check_resta(anterior, valor, num_repes, resultado)

            num_repes = check_repes(valor, anterior, num_repes, letra)
            
            resultado += valor # incrementar el valor
            
            anterior = valor # recordar el digito anterior
        else:
            raise ValueError("Simbolo no permitido")
        

    return resultado        

def de_romano_a_arabigo(romano: str) -> int:
    groups = to_roman_tuples(romano)

    result = 0

    for roman_number, num_miles in groups:
        # transformar roman_number en arabigo
        # obtener los miles como 1000 ** num_miles
        # Multiplicar miles por arabigo
        # sumar a result
        arabic = a_arabigo_menor_4000(roman_number)
        miles = 1000 ** num_miles
        result += arabic * miles

    return result
   
def get_order(numero: int) -> int:
    if numero == 0:
        return 0
    cadena = str(numero)
    orden = 1
    for num in cadena[::-1]:
        if num != "0":
            break
        orden = orden * 10

    return orden

def to_groups(number: int) -> list:
    result = []

    while number > 0:
        resto = number % 1000
        result.append(resto)
        number = number // 1000

    if not result:
        result = [0] 
    elif result[-1] < 4 and len(result) > 1:
        result[-2] = result[-1] * 1000 + result[-2]
        result.pop()

    return result[::-1]

def to_roman_tuples(roman_number: str) -> list:
    groups = roman_number.split(THOUSAND_IND)
    result = []
    for group in groups:
        if group:
            t = [group, 1]
            result.append(t)
        else:
            t[1] += 1
    
    result[-1][1] -= 1

    result = list(map(lambda x: tuple(x), result))

    return result