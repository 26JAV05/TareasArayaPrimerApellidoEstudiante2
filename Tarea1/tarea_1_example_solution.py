def filtrar_vocales(cadena, bandera):
    # Filtra las vocales o consonantes de un texto.
    # Entradas:
    # cadena: texto a evaluar.
    # bandera: valor True o False.
    # Salidas:
    # Retorna el codigo de estado y el texto resultante.

    res = ""  # Variable para guardar el resultado

    # Error si no es un string
    if not isinstance(cadena, str):
        return -100, None

    # Error si bandera no es un booleano
    if not isinstance(bandera, bool):
        return -500, None

    vocales = "aeiouAEIOU"  # Lista de vocales
    longitud = len(cadena)  # Se cuenta la cantidad de caracteres

    # Error si el texto esta vacio
    if longitud == 0:
        return -300, None

    # Error si contiene caracteres que no son letras
    if not cadena.isalpha():
        return -200, None

    # Error si excede los 30 caracteres
    if longitud > 30:
        return -400, None

    if bandera:
        # Se buscan vocales y se agregan al resultado
        for char in cadena:
            if char in vocales:
                res += char
    else:
        # Se buscan consonantes y se agregan al resultado
        for char in cadena:
            if char not in vocales:
                res += char

    return 0, res  # Retorno código de exitoo


def encontrar_extremos(lista_numeros):

    # Busca el valor minimo y el valor maximo en una lista.
    # Entradas: lista_numeros
    # Salidas: retorna el codigo de estado, el valor minimo y el maximo.

    # Error si no es una lista
    if not isinstance(lista_numeros, list):
        return -600, None, None

    # Se revisa que todos los elementos sean numeros
    for i in lista_numeros:
        if type(i) is not int and type(i) is not float:
            return -700, None, None

    longitud = len(lista_numeros)  # Se cuenta la cantidad de elementos

    # Error si la lista esta vacia
    if longitud == 0:
        return -800, None, None

    # Error si la lista tiene mas de 15 elementos
    if longitud > 15:
        return -900, None, None

    # Se obtiene el mínimo y el máximo
    minimo = min(lista_numeros)
    maximo = max(lista_numeros)

    return 0, minimo, maximo  # Retorno c+odigo exito
