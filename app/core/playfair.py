def cifrar_playfair(texto, clave, alphabet=None):
    """
    Cifra un texto utilizando el método de Playfair.
    Función adaptadora para integrarse con el controlador de variables.
    
    :param texto: Texto a cifrar.
    :param clave: Clave de cifrado.
    :param alphabet: Alfabeto a utilizar (no se usa en este algoritmo pero se incluye para compatibilidad).
    :return: Texto cifrado.
    """
    try:
        # Normalizar entrada
        texto = texto.strip()
        clave = clave.strip()
        
        if not texto:
            return "El texto a cifrar no puede estar vacío."
            
        if not clave:
            return "La clave no puede estar vacía."
        
        # Normalizar el texto y la clave usando la misma función que el descifrado
        texto_norm = normalizar_palabra(texto)
        clave_norm = normalizar_palabra(clave)
        
        if len(texto_norm) < 1:
            raise ValueError("El texto a cifrar es demasiado corto o contiene caracteres no válidos.")
        
        # Preparar el texto para que tenga longitud par
        # Si dos letras iguales están juntas, insertar 'x' entre ellas
        texto_preparado = []
        i = 0
        while i < len(texto_norm):
            if i+1 < len(texto_norm):
                if texto_norm[i] == texto_norm[i+1]:
                    texto_preparado.append(texto_norm[i])
                    texto_preparado.append('x')
                    i += 1
                else:
                    texto_preparado.append(texto_norm[i])
                    texto_preparado.append(texto_norm[i+1])
                    i += 2
            else:
                texto_preparado.append(texto_norm[i])
                texto_preparado.append('x')  # Agregar 'x' si queda una letra sola
                i += 1
        
        texto_norm = ''.join(texto_preparado)
        
        # Generar matriz usando la función existente
        matriz = []
        generar_matriz(clave_norm, matriz)
        
        # Cifrar el texto usando una versión adaptada de la lógica de cifrado
        texto_cifrado = []
        posiciones = [0] * 4
        for i in range(0, len(texto_norm), 2):
            buscar_posiciones(matriz, texto_norm[i], texto_norm[i+1], posiciones)
            if posiciones[0] == posiciones[2]:  # Misma fila
                texto_cifrado.append(matriz[posiciones[0]][(posiciones[1] + 1) % 5])
                texto_cifrado.append(matriz[posiciones[2]][(posiciones[3] + 1) % 5])
            elif posiciones[1] == posiciones[3]:  # Misma columna
                texto_cifrado.append(matriz[(posiciones[0] + 1) % 5][posiciones[1]])
                texto_cifrado.append(matriz[(posiciones[2] + 1) % 5][posiciones[3]])
            else:  # Forma un rectángulo
                texto_cifrado.append(matriz[posiciones[0]][posiciones[3]])
                texto_cifrado.append(matriz[posiciones[2]][posiciones[1]])
        
        return ''.join(texto_cifrado).upper()  # Convertir a mayúsculas para consistencia
    except Exception as e:
        return e

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

# Función para convertir mayúsculas en minúsculas y eliminar otros caracteres
def normalizar_palabra(palabra):
    palabra = palabra.replace(' ', '')
    palabra = list(palabra)
    for i in range(len(palabra)):
        if ord(palabra[i]) > 64 and ord(palabra[i]) < 91:
            palabra[i] = chr(ord(palabra[i]) + 32)
        elif ord(palabra[i]) < 97 or ord(palabra[i]) > 122:
            palabra[i] = ''
    return ''.join(palabra)

# Función para generar la matriz de caracteres
def generar_matriz(clave, matriz):
    n = len(clave)
    
    matriz.clear()
    for i in range(5):
        matriz.append([0]*5)

    abecedario = [0]*26

    for i in range(n):
        if clave[i] != 'j':
            abecedario[ord(clave[i]) - 97] = 2

    abecedario[ord('j') - 97] = 1

    i = 0
    j = 0

    for k in range(n):
        if abecedario[ord(clave[k]) - 97] == 2:
            abecedario[ord(clave[k]) - 97] = 1
            matriz[i][j] = clave[k]
            j += 1
            if j == 5:
                i += 1
                j = 0

    for k in range(26):
        if abecedario[k] == 0:
            matriz[i][j] = chr(k + 97)
            j += 1
            if j == 5:
                i += 1
                j = 0

# Función para retornar la posición de las letras del digrafo en la matriz
def buscar_posiciones(matriz, a, b, posiciones):
    if a == 'j':
        a = 'i'
    elif b == 'j':
        b = 'i'
    for i in range(5):
        for j in range(5):
            if matriz[i][j] == a:
                posiciones[0] = i
                posiciones[1] = j
            elif matriz[i][j] == b:
                posiciones[2] = i
                posiciones[3] = j

# Función para descifrar
def descifrar(palabra, matriz):
    n = len(palabra)
    palabra = list(palabra)
    posiciones = [0] * 4
    for i in range(0, n, 2):
        buscar_posiciones(matriz, palabra[i], palabra[i + 1], posiciones)
        if posiciones[0] == posiciones[2]:
            palabra[i] = matriz[posiciones[0]][(posiciones[1] + 4) % 5]
            palabra[i + 1] = matriz[posiciones[2]][(posiciones[3] + 4) % 5]
        elif posiciones[1] == posiciones[3]:
            palabra[i] = matriz[(posiciones[0] + 4) % 5][posiciones[1]]
            palabra[i + 1] = matriz[(posiciones[2] + 4) % 5][posiciones[3]]
        else:
            palabra[i] = matriz[posiciones[0]][posiciones[3]]
            palabra[i + 1] = matriz[posiciones[2]][posiciones[1]]
    return ''.join(palabra)

# Descifrado mediante Playfair
def descifrar_playfair_console(palabra, clave):
    matriz = []
    clave = normalizar_palabra(clave)
    palabra = normalizar_palabra(palabra)
    generar_matriz(clave, matriz)
    return descifrar(palabra, matriz)

# Función adaptadora para integrar con el controlador de variables
def descifrar_playfair(texto, clave, alphabet=None):
    """
    Descifra un texto cifrado utilizando el método de Playfair.
    Función adaptadora para integrarse con el controlador de variables.
    
    :param texto: Texto cifrado a descifrar.
    :param clave: Clave de descifrado.
    :param alphabet: Alfabeto a utilizar (no se usa en este algoritmo pero se incluye para compatibilidad).
    :return: Texto descifrado.
    """
    try:
        # Normalizar entrada
        texto = texto.strip()
        clave = clave.strip()
        
        if not texto:
            return "El texto cifrado no puede estar vacío."
            
        if not clave:
            return "La clave no puede estar vacía."
            
        # Usar la función de descifrado existente
        matriz = []
        texto_norm = normalizar_palabra(texto)
        clave_norm = normalizar_palabra(clave)
        
        if len(texto_norm) < 2:
            raise ValueError("El texto cifrado es demasiado corto para Playfair.")
            
        if len(texto_norm) % 2 != 0:
            texto_norm += 'x'  # Asegurar que el texto tenga longitud par
            
        generar_matriz(clave_norm, matriz)
        resultado = descifrar(texto_norm, matriz)
        
        return resultado.upper()  # Convertir a mayúsculas para consistencia
    except Exception as e:
        return e

if __name__ == "__main__":
    clave = "unsa"
    palabra = "nshwfqnkfngw"
    print("Clave:", clave)
    print("Palabra cifrada:", palabra)
    palabra = descifrar_playfair_console(palabra, clave)
    print("Palabra descifrada:", palabra)