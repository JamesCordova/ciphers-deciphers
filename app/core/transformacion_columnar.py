
def cifrar_transformacion_columnar_simple(texto, clave):
    """
    Cifra un texto utilizando el método de transformación columnar simple.
    
    :param texto: Texto a cifrar.
    :param clave: Clave de cifrado.
    :return: Texto cifrado.
    """
    # Eliminar espacios en blanco del texto
    texto = texto.replace(" ", "")
    
    # Calcular el número de filas necesarias
    num_filas = len(texto) // len(clave) + (len(texto) % len(clave) > 0)
    
    # Crear una lista para almacenar las filas
    filas = [''] * num_filas
    
    # Llenar las filas con el texto
    for i in range(len(texto)):
        fila = i // len(clave)
        col = i % len(clave)
        filas[fila] += texto[i]
    
    # Ordenar la clave y obtener el orden de las columnas
    orden_clave = sorted(range(len(clave)), key=lambda k: clave[k])
    
    # Cifrar el texto reordenando las columnas
    texto_cifrado = ''
    for col in orden_clave:
        for fila in filas:
            if col < len(fila):
                texto_cifrado += fila[col]
    
    return texto_cifrado

def descifrar_transformacion_columnar_simple(texto_cifrado, clave):
    """
    Descifra un texto cifrado utilizando el método de transformación columnar simple.
    
    :param texto_cifrado: Texto cifrado.
    :param clave: Clave de cifrado.
    :return: Texto descifrado.
    """
    # Calcular el número de filas necesarias
    num_filas = len(texto_cifrado) // len(clave) + (len(texto_cifrado) % len(clave) > 0)
    
    # Crear una lista para almacenar las filas
    filas = [''] * num_filas
    
    # Ordenar la clave y obtener el orden de las columnas
    orden_clave = sorted(range(len(clave)), key=lambda k: clave[k])
    
    # Llenar las filas con el texto cifrado reordenando las columnas
    for col in range(len(clave)):
        for fila in range(num_filas):
            if col < len(filas[fila]):
                filas[fila] += texto_cifrado[col * num_filas + fila]
    
    # Descifrar el texto concatenando las filas
    texto_descifrado = ''.join(filas)
    
    return texto_descifrado
