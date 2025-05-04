import app.core.transformacion_columnar as tc
import app.core.playfair as pf

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
        
        self.cipher_dict = {
            "Transformación Columnar Simple": tc.cifrar_transformacion_columnar_simple,
            "Transformación Columnar Doble": None, # Placeholder for future implementation
            "Rejillas criptográficas": None,  # Placeholder for future implementation
            "Transposición de filas": None,  # Placeholder for future implementation
            "Permutación por series": None,  # Placeholder for future implementation
            "Playfair": pf.cifrar_playfair
        }
        
        self.decipher_dict = {
            "Transformación Columnar Simple": tc.descifrar_transformacion_columnar_simple,
            "Transformación Columnar Doble": None,  # Placeholder for future implementation
            "Rejillas criptográficas": None,  # Placeholder for future implementation
            "Transposición de filas": None,  # Placeholder for future implementation
            "Permutación por series": None,  # Placeholder for future implementation
            "Playfair": pf.descifrar_playfair
        }
        
        self.alphabets = [
            "Español",
            "Inglés",
            "Francés",
            "Alemán",
            "Custom"
        ]
        self.alphabet_selected = self.alphabets[0]
        
        # Diccionario de abecedarios por idioma
        self.alphabet_dict = {
            "Español": "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ",
            "Inglés": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            "Francés": "ABCDEFGHIJKLMNOPQRSTUVWXYZÀÂÆÇÉÈÊËÎÏÔŒÙÛÜŸ",
            "Alemán": "ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜß",
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
            self.current_alphabet = self.alphabet_dict.get(alphabet)

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
    
    def algorithm_not_defined(self, input_text, key):
        """Método para manejar el caso en que el algoritmo no está definido."""
        return f'El algoritmo {self.algorithm_selected} no está definido.'
        
    def cipher_text(self, input_text, key):
        print(f"Cifrando texto con algoritmo: {self.algorithm_selected}, clave: {key}")

        try:
            result = self.cipher_dict.get(self.algorithm_selected)(input_text, key, self.current_alphabet)
        except TypeError:
            return self.algorithm_not_defined(input_text, key)
        return result
        
    def decipher_text(self, input_text, key):
        print(f"Cifrando texto con algoritmo: {self.algorithm_selected}, clave: {key}")

        try:
            result = self.decipher_dict.get(self.algorithm_selected)(input_text, key, self.current_alphabet)
        except TypeError:
            return self.algorithm_not_defined(input_text, key)
        return result