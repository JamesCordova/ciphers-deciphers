
def cifrar_playfair(texto, clave, alphabet=None):
    """
    Cifra un texto utilizando el método de Playfair.
    
    :param texto: Texto a cifrar.
    :param clave: Clave de cifrado.
    :return: Texto cifrado.
    """
    # Crear la matriz de Playfair
    matriz = crear_matriz_playfair(clave)
    
    # Preparar el texto
    texto = preparar_texto(texto)
    
    # Cifrar el texto
    texto_cifrado = ''
    for i in range(0, len(texto), 2):
        par = texto[i:i+2]
        if len(par) == 1:
            par += 'X'  # Agregar 'X' si el par es impar
        texto_cifrado += cifrar_par(par, matriz)
    
    return texto_cifrado

def descifrar_playfair(texto_cifrado, clave, alphabet=None):
    """
    Descifra un texto cifrado utilizando el método de Playfair.
    
    :param texto_cifrado: Texto cifrado.
    :param clave: Clave de cifrado.
    :return: Texto descifrado.
    """
    # Crear la matriz de Playfair
    matriz = crear_matriz_playfair(clave)
    
    # Preparar el texto cifrado
    texto_cifrado = preparar_texto(texto_cifrado)
    
    # Descifrar el texto
    texto_descifrado = ''
    for i in range(0, len(texto_cifrado), 2):
        par = texto_cifrado[i:i+2]
        if len(par) == 1:
            par += 'X'  # Agregar 'X' si el par es impar
        texto_descifrado += descifrar_par(par, matriz)
    
    return texto_descifrado

def crear_matriz_playfair(clave):
    """
    Crea la matriz de Playfair a partir de la clave.
    
    :param clave: Clave de cifrado.
    :return: Matriz de Playfair.
    """
    # Eliminar duplicados y espacios en blanco de la clave
    clave = ''.join(sorted(set(clave), key=lambda x: clave.index(x))).replace(' ', '')
    
    # Crear la matriz de Playfair
    alfabeto = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'  # 'J' se combina con 'I'
    matriz = []
    
    for letra in clave:
        if letra not in matriz and letra in alfabeto:
            matriz.append(letra)
    
    for letra in alfabeto:
        if letra not in matriz:
            matriz.append(letra)
    
    return [matriz[i:i+5] for i in range(0, 25, 5)]  # Matriz de 5x5

def preparar_texto(texto):
    """
    Prepara el texto para el cifrado o descifrado.
    
    :param texto: Texto a preparar.
    :return: Texto preparado.
    """
    # Eliminar espacios en blanco y convertir a mayúsculas
    texto = texto.replace(' ', '').upper()
    
    # Reemplazar 'J' por 'I'
    texto = texto.replace('J', 'I')
    
    return texto

def cifrar_par(par, matriz):
    """
    Cifra un par de letras utilizando la matriz de Playfair.
    
    :param par: Par de letras a cifrar.
    :param matriz: Matriz de Playfair.
    :return: Par cifrado.
    """
    fila1, col1 = encontrar_posicion(par[0], matriz)
    fila2, col2 = encontrar_posicion(par[1], matriz)
    
    if fila1 == fila2:
        # Mismo fila
        return matriz[fila1][(col1 + 1) % 5] + matriz[fila2][(col2 + 1) % 5]
    elif col1 == col2:
        # Misma columna
        return matriz[(fila1 + 1) % 5][col1] + matriz[(fila2 + 1) % 5][col2]
    else:
        # Diferente fila y columna
        return matriz[fila1][col2] + matriz[fila2][col1]

def descifrar_par(par, matriz):
    """
    Descifra un par de letras utilizando la matriz de Playfair.
    
    :param par: Par de letras a descifrar.
    :param matriz: Matriz de Playfair.
    :return: Par descifrado.
    """
    fila1, col1 = encontrar_posicion(par[0], matriz)
    fila2, col2 = encontrar_posicion(par[1], matriz)
    
    if fila1 == fila2:
        # Mismo fila
        return matriz[fila1][(col1 - 1) % 5] + matriz[fila2][(col2 - 1) % 5]
    elif col1 == col2:
        # Misma columna
        return matriz[(fila1 - 1) % 5][col1] + matriz[(fila2 - 1) % 5][col2]
    else:
        # Diferente fila y columna
        return matriz[fila1][col2] + matriz[fila2][col1]
    
def encontrar_posicion(letra, matriz):
    """
    Encuentra la posición de una letra en la matriz de Playfair.
    
    :param letra: Letra a buscar.
    :param matriz: Matriz de Playfair.
    :return: Fila y columna de la letra en la matriz.
    """
    for i in range(5):
        for j in range(5):
            if matriz[i][j] == letra:
                return i, j
    return None, None  # Si no se encuentra la letra