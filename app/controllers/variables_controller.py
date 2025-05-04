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
            "Transformación Columnar Doble": tc.cifrar_transformacion_columnar_doble,
            "Rejillas criptográficas": None,  # Placeholder for future implementation
            "Transposición de filas": None,  # Placeholder for future implementation
            "Permutación por series": None,  # Placeholder for future implementation
            "Playfair": pf.cifrar_playfair
        }
        
        self.decipher_dict = {
            "Transformación Columnar Simple": tc.descifrar_transformacion_columnar_simple,
            "Transformación Columnar Doble": tc.descifrar_transformacion_columnar_doble,
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

        # Para gestionar los mensajes de notificación
        self.last_notification = ""
        self.notification_type = "success"  # "success", "error", "info"

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
    
    def set_notification(self, message, type="success"):
        """Establece un mensaje de notificación y su tipo (éxito, error o información)."""
        self.last_notification = message
        self.notification_type = type
        return message
    
    def get_last_notification(self):
        """Retorna el último mensaje de notificación y su tipo."""
        return self.last_notification, self.notification_type
    
    def clear_notification(self):
        """Limpia el mensaje de notificación."""
        self.last_notification = ""
        self.notification_type = "success"
    
    def algorithm_not_defined(self, input_text, key):
        """Método para manejar el caso en que el algoritmo no está definido."""
        message = f'El algoritmo {self.algorithm_selected} no está implementado todavía.'
        return self.set_notification(message, "error")
        
    def cipher_text(self, input_text, key):
        """Cifra el texto utilizando el algoritmo seleccionado"""
        print(f"Cifrando texto con algoritmo: {self.algorithm_selected}, clave: {key}")
        
        # Validar parámetros básicos
        if not input_text:
            return self.set_notification("El texto de entrada no puede estar vacío.", "error")
        
        if not key:
            return self.set_notification("La clave no puede estar vacía.", "error")

        if self.algorithm_selected == "Transformación Columnar Doble" and " " not in key:
            return self.set_notification("Para cifrado columnar doble, la clave debe ser dos palabras separadas por espacio.", "error")
        
        try:
            # Intentar cifrar el texto
            cipher_function = self.cipher_dict.get(self.algorithm_selected)
            if cipher_function is None:
                return self.algorithm_not_defined(input_text, key)
                
            result = cipher_function(input_text, key, self.current_alphabet)
            
            # Verificar si el resultado es un mensaje de error
            if result and isinstance(result, str) and ("error" in result.lower() or "excepción" in result.lower() or "inválid" in result.lower()):
                return self.set_notification(result, "error")
            else:
                self.set_notification(f"Cifrado {self.algorithm_selected} completado.", "success")
                return result
                
        except Exception as e:
            return self.set_notification(f"Error al cifrar: {str(e)}", "error")
        
    def decipher_text(self, input_text, key):
        """Descifra el texto utilizando el algoritmo seleccionado"""
        print(f"Descifrando texto con algoritmo: {self.algorithm_selected}, clave: {key}")
        
        # Validar parámetros básicos
        if not input_text:
            return self.set_notification("El texto cifrado no puede estar vacío.", "error")
        
        if not key:
            return self.set_notification("La clave no puede estar vacía.", "error")
            
        if self.algorithm_selected == "Transformación Columnar Doble" and " " not in key:
            return self.set_notification("Para cifrado columnar doble, la clave debe ser dos palabras separadas por espacio.", "error")

        try:
            # Intentar descifrar el texto
            decipher_function = self.decipher_dict.get(self.algorithm_selected)
            if decipher_function is None:
                return self.algorithm_not_defined(input_text, key)
                
            result = decipher_function(input_text, key, self.current_alphabet)
            
            # Verificar si el resultado es un mensaje de error
            if result and isinstance(result, str) and ("error" in result.lower() or "excepción" in result.lower() or "inválid" in result.lower()):
                return self.set_notification(result, "error")
            else:
                self.set_notification(f"Descifrado completado con éxito usando {self.algorithm_selected}.", "success")
                return result
                
        except Exception as e:
            return self.set_notification(f"Error al descifrar: {str(e)}", "error")