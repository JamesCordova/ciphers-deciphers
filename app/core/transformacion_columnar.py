# from enum import Enum
import math

class Alfabetos():
    ALFABETO_INGLES = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ALFABETO_ESPANOL = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    ALFABETO_NUMERICO = "0123456789"
    ALFABETO_ALFANUMERICO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

class CifradoColumnarSimple:
    """
    Implementación del cifrado por transposición columnar simple.
    Este cifrado reorganiza los caracteres de un mensaje según el orden derivado de una clave.
    """
    def __init__(self, clave: str, alfabeto: str = Alfabetos.ALFABETO_INGLES):
        """
        Inicializa el cifrador con una clave y un alfabeto específico.

        Args:
            clave: Palabra clave que determina el orden de las columnas.
            alfabeto: Conjunto de caracteres permitidos (por defecto, alfabeto inglés en mayúsculas).

        Raises:
            ValueError: Si la clave está vacía o contiene caracteres fuera del alfabeto.
        """
        # Validación inicial de parámetros
        if not clave:
            raise ValueError("La clave no puede estar vacía")

        # Normalización a mayúsculas para consistencia
        self.alfabeto = alfabeto.upper()
        self.clave = clave.upper()

        # Verificar que todos los caracteres de la clave estén en el alfabeto
        caracteres_invalidos = [c for c in self.clave if c not in self.alfabeto]
        if caracteres_invalidos:
            raise ValueError(f"La clave contiene caracteres fuera del alfabeto: {caracteres_invalidos}")

        # Calcular el orden de las columnas basado en la clave
        self.indices_columnas = self._calcular_orden_columnas()

    def _calcular_orden_columnas(self):
        """
        Calcula el orden numérico de cada columna basado en el orden alfabético de la clave.

        Returns:
            Lista donde cada posición contiene el índice de columna después de ordenar.
        """
        # Crear pares (caracter, índice_original) y ordenarlos alfabéticamente
        pares_ordenados = sorted([(caracter, indice) for indice, caracter in enumerate(self.clave)])

        # Crear una lista para convertir índices originales a nuevos índices ordenados
        mapa_indices = [0] * len(self.clave)

        # Asignar a cada posición original su nuevo índice ordenado
        for nuevo_indice, (_, indice_original) in enumerate(pares_ordenados):
            mapa_indices[indice_original] = nuevo_indice

        return mapa_indices

    def cifrar(self, mensaje: str, rellenar: bool = False):
        """
        Cifra un mensaje usando el método de transposición columnar.

        Args:
            mensaje: Texto a cifrar.
            rellenar: Si es True, rellena los espacios vacíos con 'X'.

        Returns:
            Mensaje cifrado.

        Raises:
            ValueError: Si el mensaje contiene caracteres fuera del alfabeto.
        """
        # Normalización y limpieza del mensaje
        mensaje_procesado = mensaje.upper().replace(" ", "")

        # Validación de caracteres del mensaje
        caracteres_invalidos = [c for c in mensaje_procesado if c not in self.alfabeto]
        if caracteres_invalidos:
            raise ValueError(f"El mensaje contiene caracteres fuera del alfabeto: {caracteres_invalidos}")

        # Cálculo de dimensiones para la matriz
        num_columnas = len(self.clave)
        num_filas = math.ceil(len(mensaje_procesado) / num_columnas)
        total_celdas = num_filas * num_columnas

        # Rellenar mensaje si es necesario
        if rellenar:
            # Agregar 'X' al final para completar la matriz
            caracteres_faltantes = total_celdas - len(mensaje_procesado)
            mensaje_completo = mensaje_procesado + 'X' * caracteres_faltantes
        else:
            mensaje_completo = mensaje_procesado

        # Construcción de la matriz por filas
        matriz_mensaje = []
        indice_caracter = 0

        for fila in range(num_filas):
            # Extraer caracteres para esta fila
            fila_actual = []
            for columna in range(num_columnas):
                if indice_caracter < len(mensaje_completo):
                    fila_actual.append(mensaje_completo[indice_caracter])
                    indice_caracter += 1
                else:
                    # Si no hay más caracteres y no rellenamos, dejar vacío
                    fila_actual.append('')
            matriz_mensaje.append(fila_actual)

        # Leer columnas según el orden determinado por la clave
        texto_cifrado = ''
        for indice_columna in range(len(self.indices_columnas)):
            # Encontrar qué columna va en esta posición
            columna_a_leer = self.indices_columnas.index(indice_columna)

            # Extraer caracteres de esta columna en todas las filas
            for fila in matriz_mensaje:
                if columna_a_leer < len(fila) and fila[columna_a_leer] != '':
                    texto_cifrado += fila[columna_a_leer]

        return texto_cifrado

    def descifrar(self, mensaje_cifrado: str):
        """
        Descifra un mensaje cifrado por transposición columnar.

        Args:
            mensaje_cifrado: Texto cifrado a descifrar.

        Returns:
            Mensaje descifrado.

        Raises:
            ValueError: Si el mensaje cifrado contiene caracteres fuera del alfabeto.
        """
        # Validación de caracteres del mensaje cifrado
        caracteres_invalidos = [c for c in mensaje_cifrado if c not in self.alfabeto]
        if caracteres_invalidos:
            raise ValueError(f"El mensaje cifrado contiene caracteres fuera del alfabeto: {caracteres_invalidos}")

        # PASO 1: Calcular las dimensiones de la matriz
        num_columnas = len(self.clave)
        longitud_mensaje = len(mensaje_cifrado)

        # Calcular el número de filas (redondeando hacia arriba)
        num_filas = math.ceil(longitud_mensaje / num_columnas)

        # Calcular celdas totales y celdas vacías
        total_celdas = num_filas * num_columnas
        celdas_vacias = total_celdas - longitud_mensaje

        # PASO 2: Determinar la longitud de cada columna
        # Inicialmente, asumimos que todas las columnas tienen el mismo número de filas
        longitudes_columnas = [num_filas] * num_columnas

        # Si hay celdas vacías, algunas columnas tendrán una fila menos
        if celdas_vacias > 0:
            # Identificar qué columnas originales tendrán una fila menos
            # Las columnas que aparecen últimas en el orden de lectura tienen menos filas
            # Esto corresponde a las columnas con índices más altos en la matriz original
            columnas_cortas = []

            # Obtener las posiciones ordenadas según la clave
            posiciones_ordenadas = []
            for i in range(len(self.indices_columnas)):
                posiciones_ordenadas.append(self.indices_columnas.index(i))

            # Las últimas columnas en ser leídas (según el orden de la clave) tienen una fila menos
            for i in sorted(posiciones_ordenadas)[-celdas_vacias:]:
                columnas_cortas.append(i)
                longitudes_columnas[i] -= 1

        # PASO 3: Reconstruir las columnas a partir del mensaje cifrado
        columnas_reconstruidas = {}
        indice_actual = 0

        # Recorrer las columnas en el orden en que aparecen en el texto cifrado
        for orden_columna in range(num_columnas):
            # Encontrar qué columna original corresponde a esta posición en el orden
            columna_original = self.indices_columnas.index(orden_columna)

            # Obtener la longitud de esta columna
            longitud_columna = longitudes_columnas[columna_original]

            # Extraer los caracteres correspondientes a esta columna
            fin_columna = indice_actual + longitud_columna
            caracteres_columna = mensaje_cifrado[indice_actual:fin_columna]

            # Guardar la columna reconstruida
            columnas_reconstruidas[columna_original] = list(caracteres_columna)

            # Actualizar el índice para la siguiente columna
            indice_actual = fin_columna

        # PASO 4: Reconstruir la matriz original leyendo por filas
        matriz_reconstruida = []

        for fila in range(num_filas):
            fila_actual = []

            for columna in range(num_columnas):
                # Verificar si esta posición tiene un carácter
                if fila < len(columnas_reconstruidas.get(columna, [])):
                    fila_actual.append(columnas_reconstruidas[columna][fila])
                else:
                    # Esta posición está vacía (corresponde a una celda vacía)
                    fila_actual.append('')

            matriz_reconstruida.append(fila_actual)

        # PASO 5: Leer la matriz por filas para obtener el mensaje original
        texto_descifrado = ''
        for fila in matriz_reconstruida:
            for caracter in fila:
                if caracter:  # Ignorar celdas vacías
                    texto_descifrado += caracter

        return texto_descifrado


class CifradoColumnarDoble:
    """
    Implementación del cifrado por transposición columnar doble.
    Aplica dos veces el cifrado columnar simple con claves diferentes.
    """
    def __init__(self, clave1: str, clave2: str, alfabeto: str = Alfabetos.ALFABETO_INGLES):
        """
        Inicializa el cifrador doble con dos claves y un alfabeto específico.

        Args:
            clave1: Primera clave para la primera pasada de cifrado.
            clave2: Segunda clave para la segunda pasada de cifrado.
            alfabeto: Conjunto de caracteres permitidos.

        Raises:
            ValueError: Si alguna clave está vacía.
        """
        # Validar que ambas claves no estén vacías
        if not clave1 or not clave2:
            raise ValueError("Ambas claves deben contener al menos un carácter")

        # Crear dos instancias de cifrado simple, una para cada clave
        self.cifrador_primera_pasada = CifradoColumnarSimple(clave1, alfabeto)
        self.cifrador_segunda_pasada = CifradoColumnarSimple(clave2, alfabeto)

    def cifrar(self, mensaje: str, rellenar: bool = False):
        """
        Cifra un mensaje aplicando dos pasadas de cifrado columnar.

        Args:
            mensaje: Texto a cifrar.
            rellenar: Si es True, rellena espacios vacíos con 'X'.

        Returns:
            Mensaje cifrado con doble transposición.
        """
        # Aplicar el primer cifrador
        resultado_intermedio = self.cifrador_primera_pasada.cifrar(mensaje, rellenar=rellenar)

        # Aplicar el segundo cifrador al resultado de la primera pasada
        resultado_final = self.cifrador_segunda_pasada.cifrar(resultado_intermedio, rellenar=rellenar)

        return resultado_final

    def descifrar(self, mensaje_cifrado: str, rellenar: bool = False):
        """
        Descifra un mensaje cifrado con doble transposición columnar.

        Args:
            mensaje_cifrado: Texto cifrado a descifrar.

        Returns:
            Mensaje descifrado.
        """
        # Primero descifrar con el segundo cifrador (orden inverso)
        resultado_intermedio = self.cifrador_segunda_pasada.descifrar(mensaje_cifrado)

        if rellenar:  # Si se usó relleno, ajustar el resultado intermedio, ya que puede tener 'X' al final
            # Ajustar el resultado intermedio eliminando caracteres extra al final
            exceso = len(resultado_intermedio) % len(self.cifrador_primera_pasada.clave)

            if exceso != 0:
                resultado_intermedio = resultado_intermedio[:-exceso]

        # Luego descifrar con el primer cifrador
        resultado_final = self.cifrador_primera_pasada.descifrar(resultado_intermedio)

        return resultado_final

# Funciones de adaptación para el controlador
def cifrar_transformacion_columnar_simple(mensaje: str, clave: str, alfabeto: str = Alfabetos.ALFABETO_INGLES, rellenar: bool = True):
    """
    Función de adaptación para el controlador que utiliza la clase CifradoColumnarSimple.
    
    Args:
        mensaje: Texto a cifrar
        clave: Clave de cifrado
        alfabeto: Alfabeto a utilizar
        rellenar: Si se debe rellenar con 'X' las celdas vacías
        
    Returns:
        Texto cifrado
        
    Raises:
        ValueError: Si hay errores en los parámetros
    """
    try:
        cifrador = CifradoColumnarSimple(clave, alfabeto)
        return cifrador.cifrar(mensaje, rellenar)
    except Exception as e:
        return str(e)

def descifrar_transformacion_columnar_simple(mensaje: str, clave: str, alfabeto: str = Alfabetos.ALFABETO_INGLES):
    """
    Función de adaptación para el controlador que utiliza la clase CifradoColumnarSimple.
    
    Args:
        mensaje: Texto cifrado a descifrar
        clave: Clave de cifrado
        alfabeto: Alfabeto a utilizar
        
    Returns:
        Texto descifrado
        
    Raises:
        ValueError: Si hay errores en los parámetros
    """
    try:
        cifrador = CifradoColumnarSimple(clave, alfabeto)
        return cifrador.descifrar(mensaje)
    except Exception as e:
        return str(e)

def cifrar_transformacion_columnar_doble(mensaje: str, clave: str, alfabeto: str = Alfabetos.ALFABETO_INGLES, rellenar: bool = True):
    """
    Función de adaptación para el controlador que utiliza la clase CifradoColumnarDoble.
    La clave debe contener dos palabras separadas por un espacio.
    
    Args:
        mensaje: Texto a cifrar
        clave: Dos claves separadas por espacio (ej: "CLAVE1 CLAVE2")
        alfabeto: Alfabeto a utilizar
        rellenar: Si se debe rellenar con 'X' las celdas vacías
        
    Returns:
        Texto cifrado
        
    Raises:
        ValueError: Si hay errores en los parámetros
    """
    try:
        # Dividir la clave en dos partes
        partes_clave = clave.split()
        if len(partes_clave) != 2:
            raise ValueError("La clave para cifrado columnar doble debe contener dos palabras separadas por un espacio")
            
        clave1, clave2 = partes_clave
        cifrador = CifradoColumnarDoble(clave1, clave2, alfabeto)
        return cifrador.cifrar(mensaje, rellenar)
    except Exception as e:
        return str(e)

def descifrar_transformacion_columnar_doble(mensaje: str, clave: str, alfabeto: str = Alfabetos.ALFABETO_INGLES, rellenar: bool = True):
    """
    Función de adaptación para el controlador que utiliza la clase CifradoColumnarDoble.
    La clave debe contener dos palabras separadas por un espacio.
    
    Args:
        mensaje: Texto cifrado a descifrar
        clave: Dos claves separadas por espacio (ej: "CLAVE1 CLAVE2")
        alfabeto: Alfabeto a utilizar
        rellenar: Si se usó relleno durante el cifrado
        
    Returns:
        Texto descifrado
        
    Raises:
        ValueError: Si hay errores en los parámetros
    """
    try:
        # Dividir la clave en dos partes
        partes_clave = clave.split()
        if len(partes_clave) != 2:
            raise ValueError("La clave para cifrado columnar doble debe contener dos palabras separadas por un espacio")
            
        clave1, clave2 = partes_clave
        cifrador = CifradoColumnarDoble(clave1, clave2, alfabeto)
        return cifrador.descifrar(mensaje, rellenar)
    except Exception as e:
        return str(e)
