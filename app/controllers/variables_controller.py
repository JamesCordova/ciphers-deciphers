class VariablesController:
    def __init__(self):
        self.algorithms = [
            "Transformación Columnar Simple",
            "Transformación Columnar Doble",
            "Rejillas criptográficas",
            "Transposición de filas",
            "Permutación por series",
            "Playfair"
        ]
        self.algorithm_selected = self.algorithms[0]

        self.alphabets = [
            "Español",
            "Inglés",
            "Francés",
            "Alemán",
            "Italiano",
            "Custom"
        ]
        self.alphabet_selected = self.alphabets[0]
        
        # Diccionario de abecedarios por idioma
        self.alphabet_dict = {
            "Español": "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ",
            "Inglés": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            "Francés": "ABCDEFGHIJKLMNOPQRSTUVWXYZÀÂÆÇÉÈÊËÎÏÔŒÙÛÜŸ",
            "Alemán": "ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜß",
            "Italiano": "ABCDEFGHILMNOPQRSTUVZ",
            "Custom": ""  # El usuario puede definir este
        }
        
        # Abecedario actual (inicializado con el del idioma por defecto)
        self.current_alphabet = self.alphabet_dict[self.alphabet_selected]

    def set_algorithm(self, algorithm):
        if algorithm in self.algorithms:
            self.algorithm_selected = algorithm

    def set_alphabet(self, alphabet):
        if alphabet in self.alphabets:
            self.alphabet_selected = alphabet
            # Actualiza el abecedario actual cuando se cambia el idioma
            self.current_alphabet = self.alphabet_dict[alphabet]

    def set_custom_alphabet(self, custom_alphabet):
        """Establece un abecedario personalizado."""
        self.alphabet_dict["Custom"] = custom_alphabet
        if self.alphabet_selected == "Custom":
            self.current_alphabet = custom_alphabet

    def get_current_alphabet(self):
        """Obtiene el abecedario actual según el idioma seleccionado."""
        return self.current_alphabet

    def get_selected_algorithm(self):
        return self.algorithm_selected

    def get_selected_alphabet(self):
        return self.alphabet_selected
        
    def cipher_text(self, input_text, key):
        """
        Cifra el texto utilizando el algoritmo seleccionado.
        Esta función debe llamar a la implementación correspondiente en la carpeta core.
        """
        # Aquí deberías importar e invocar la función de cifrado adecuada según el algoritmo seleccionado
        # Ejemplo:
        # if self.algorithm_selected == "Transformación Columnar Simple":
        #     from app.core.transformacion_columnar import cifrar_columnar_simple
        #     return cifrar_columnar_simple(input_text, key, self.current_alphabet)
        # ...
        
        print(f"Cifrando texto con algoritmo: {self.algorithm_selected}, clave: {key}")
        # Por ahora, devolvemos un mensaje genérico
        return f"Texto cifrado con {self.algorithm_selected}"
        
    def decipher_text(self, input_text, key):
        """
        Descifra el texto utilizando el algoritmo seleccionado.
        Esta función debe llamar a la implementación correspondiente en la carpeta core.
        """
        # Aquí deberías importar e invocar la función de descifrado adecuada según el algoritmo seleccionado
        # Ejemplo:
        # if self.algorithm_selected == "Transformación Columnar Simple":
        #     from app.core.transformacion_columnar import descifrar_columnar_simple
        #     return descifrar_columnar_simple(input_text, key, self.current_alphabet)
        # ...
        
        print(f"Descifrando texto con algoritmo: {self.algorithm_selected}, clave: {key}")
        # Por ahora, devolvemos un mensaje genérico
        return f"Texto descifrado con {self.algorithm_selected}"