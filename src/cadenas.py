def invierte_cadena(texto: str) -> str:
    '''
    Invierte el texto que recibe los parametros

    Parametros
    -texto (str): El texto a invertir

    Devuelve:
    (str) El texto recibido al revés.
    '''

    res =""
    for c in texto:
        res = c + res
    return res

def es_palindromo(texto: str, ignora_espacios: bool = False, ignora_mayusculas: bool = False) -> bool:
    '''
    Devuelve True si el texto recibido es un palíndromo

    Parámetros:
    texto(str): el texto que queremos testear si es palindromo
    ignora_espacio
    ignora_mayuscula
    '''
    if ignora_espacios:
        texto = texto.replace(" ", "")
    if ignora_mayusculas:
        texto = texto.lower()

    return texto == invierte_cadena(texto)

def estiliza_mensaje(texto:str, alterna_may_min: bool = True, sustituye_espavios: str = " ") -> str:
    res = ""
    toca_mayusculas = True
    for c in texto:
        if alterna_may_min and c.isalpha():
            if toca_mayusculas:
                c =c.upper()
            else:
                c= c.lower()
            toca_mayusculas = not toca_mayusculas

    if c == " ":
        
        res += c