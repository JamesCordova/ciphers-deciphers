import customtkinter as ctk
import app.config as cf

class HeaderFrame(ctk.CTkFrame):
    def __init__(self, master=None, controller=None, **kwargs):
        super().__init__(master, **kwargs)
        # Controller instance
        if controller is None:
            raise ValueError("Controller needed")
        self.controller = controller
        # Create a title_label
        self.title_label = ctk.CTkLabel(self, text=self.controller.get_selected_algorithm, wraplength=650, anchor="w", font=("Arial", 25))
        self.title_label.place(relx=0.02, rely=0.5, relwidth=0.75, anchor="w")
        # Create a Combobox
        self.combobox = ctk.CTkComboBox(self, 
                                        values=self.controller.algorithms, 
                                        corner_radius=15,
                                        border_color=(cf.MESSAGE_COLOR_LIGHT,cf.MESSAGE_COLOR_DARK),
                                        command=self.on_combobox_change,
                                        state="readonly")
        self.combobox.set(self.controller.get_selected_algorithm())
        self.combobox.place(relx=0.78, rely=0.5, relwidth=0.21, anchor="w")
        
    def on_combobox_change(self, choice):
        # Update the title_label text with the selected choice
        print(f"Combobox changed to: {choice}")
        self.controller.set_algorithm(choice)
        self.title_label.configure(text=choice)

class InputOutputFrame(ctk.CTkFrame):
    def __init__(self, master=None, controller=None, **kwargs):
        super().__init__(master, **kwargs)
        # Controller instance
        if controller is None:
            raise ValueError("Controller needed")
        self.controller = controller
        
        # First the 3 frames with grid layout
        # the input side of the mid frame
        self.input_side = ctk.CTkFrame(self, fg_color=(cf.BG_COLOR_LIGHT, cf.BG_COLOR_DARK))
        self.input_side.grid(row=0, column=0, sticky="nsew")
        
        # the frame of buttons and KEY entry box
        self.operation_side = ctk.CTkFrame(self, fg_color=(cf.BG_COLOR_LIGHT, cf.BG_COLOR_DARK))
        self.operation_side.grid(row=0, column=1, sticky="ew")
        
        # the output side of the mid frame
        self.output_side = ctk.CTkFrame(self, fg_color=(cf.BG_COLOR_LIGHT, cf.BG_COLOR_DARK))
        self.output_side.grid(row=0, column=2, sticky="nsew")
        
        
        # Input side: the label and the textbox for the input text
        self.input_label = ctk.CTkLabel(self.input_side, text="Insert the input text", fg_color=(cf.BG_COLOR_LIGHT, cf.BG_COLOR_DARK))
        self.input_label.pack(side="top", fill="x")
        self.input_textbox = ctk.CTkTextbox(self.input_side, 
                                            wrap="word", 
                                            corner_radius=20,
                                            fg_color=(cf.ACCENT_COLOR_LIGHT, cf.ACCENT_COLOR_DARK))
        self.input_textbox.pack(side="top", fill="both", expand=True, padx=20, pady=10)
        
        
        # Operation side: the frame will have a button and a entry box for the key
        self.key_entry = ctk.CTkEntry(self.operation_side,placeholder_text="Clave", corner_radius=20, fg_color=(cf.BG_COLOR_LIGHT, cf.BG_COLOR_DARK))
        self.key_entry.pack(side="top", fill="x", anchor="center", expand=True, padx=15, pady=10)
        # two buttons for the cypher and decypher
        self.cypher_button = ctk.CTkButton(self.operation_side, 
                                           text="Cypher >", 
                                           corner_radius = 15,
                                            fg_color = (cf.MESSAGE_COLOR_LIGHT, cf.MESSAGE_COLOR_DARK),
                                            hover_color = (cf.SUCCESS_COLOR_LIGHT, cf.SUCCESS_COLOR_DARK), command=self.cypher_content)
        self.cypher_button.pack(side="top", fill="x", anchor="center", expand=True, padx=15, pady=10)
        self.decypher_button = ctk.CTkButton(self.operation_side, 
                                             text="< Decypher", 
                                             corner_radius = 15,
                                             fg_color = (cf.MESSAGE_COLOR_LIGHT, cf.MESSAGE_COLOR_DARK),
                                             hover_color = (cf.SUCCESS_COLOR_LIGHT, cf.SUCCESS_COLOR_DARK), command=self.decypher_content)
        self.decypher_button.pack(side="top", fill="x", anchor="center", expand=True, padx=15, pady=10)
        
    
        # Output side: the label and the textbox for the input text
        self.output_label = ctk.CTkLabel(self.output_side, text="Insert the output text", fg_color=(cf.BG_COLOR_LIGHT, cf.BG_COLOR_DARK))
        self.output_label.pack(side="top", fill="x")
        self.output_textbox = ctk.CTkTextbox(self.output_side, 
                                            wrap="word", 
                                            corner_radius=20,
                                            fg_color=(cf.ACCENT_COLOR_LIGHT, cf.ACCENT_COLOR_DARK))
        self.output_textbox.pack(side="top", fill="both", expand=True, padx=20, pady=10)
        
        # Configure the grid layout
        self.grid_columnconfigure(0, weight=5)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=5)
        self.grid_rowconfigure(0, weight=1)
        
    def cypher_content(self):
        print("Cypher button clicked")
        input_text = self.input_textbox.get("1.0", "end-1c")
        key = self.key_entry.get()
        
        if not input_text:
            print("No input text provided")
            return
            
        # Usar el controlador para cifrar el texto
        result = self.controller.cipher_text(input_text, key)
        
        # Mostrar el resultado en el cuadro de texto de salida
        self.output_textbox.delete("1.0", "end")
        self.output_textbox.insert("1.0", result)
    
    def decypher_content(self):
        print("Decypher button clicked")
        input_text = self.output_textbox.get("1.0", "end-1c")
        key = self.key_entry.get()
        
        if not input_text:
            print("No input text provided")
            return
            
        # Usar el controlador para descifrar el texto
        result = self.controller.decipher_text(input_text, key)
        
        # Mostrar el resultado en el cuadro de texto de entrada
        self.input_textbox.delete("1.0", "end")
        self.input_textbox.insert("1.0", result)
    
class AlphabetFrame(ctk.CTkFrame):
    def __init__(self, master=None, controller=None, **kwargs):
        super().__init__(master, **kwargs)
        # Controller instance
        if controller is None:
            raise ValueError("Controller needed")
        self.controller = controller
        
        # Create a label for the alphabet
        self.alphabet_label = ctk.CTkLabel(self, text="Alphabet", anchor="center", fg_color=(cf.BG_COLOR_LIGHT, cf.BG_COLOR_DARK))
        self.alphabet_label.pack(side="top", fill="x", padx=20, pady=2)
        
        # Create a segmented button for the alphabet options
        self.alphabet_options = ctk.CTkSegmentedButton(self, 
                                                       values=self.controller.alphabets, 
                                                       corner_radius=20,
                                                       bg_color=(cf.BG_COLOR_LIGHT, cf.BG_COLOR_DARK),
                                                       fg_color=(cf.BG_COLOR_LIGHT, cf.BG_COLOR_DARK),
                                                       selected_color=(cf.SUCCESS_COLOR_LIGHT, cf.SUCCESS_COLOR_DARK),
                                                       selected_hover_color=(cf.SUCCESS_COLOR_LIGHT, cf.SUCCESS_COLOR_DARK),
                                                       command=self.on_segmented_button_change)
        self.alphabet_options.set(self.controller.get_selected_alphabet())
        self.alphabet_options.pack(side="top", fill="x", padx=20, pady=2)
        
        # Create an entry for the current alphabet
        self.current_alphabet_entry = ctk.CTkEntry(self, placeholder_text="Current Alphabet", corner_radius=20, fg_color=(cf.BG_COLOR_LIGHT, cf.BG_COLOR_DARK))
        self.current_alphabet_entry.insert(0, self.controller.get_current_alphabet())
        self.current_alphabet_entry.pack(side="top", fill="x", anchor="n", expand=True, padx=20, pady=2)
        
    def on_segmented_button_change(self, value):
        print("Segmented button changed to:", value)
        # Actualizar el alfabeto seleccionado en el controlador
        self.controller.set_alphabet(value)
        
        # Si se selecciona Custom, permitir editar el abecedario
        if value == "Custom":
            self.current_alphabet_entry.configure(state="normal")
            self.current_alphabet_entry.delete(0, ctk.END)
            self.current_alphabet_entry.insert(0, self.controller.get_current_alphabet())
            self.current_alphabet_entry.bind("<FocusOut>", self.update_custom_alphabet)
        else:
            # Si no es Custom, mostrar el abecedario predefinido
            self.current_alphabet_entry.configure(state="readonly")
            self.current_alphabet_entry.delete(0, ctk.END)
            self.current_alphabet_entry.insert(0, self.controller.get_current_alphabet())
    
    def update_custom_alphabet(self, event=None):
        """Actualiza el abecedario personalizado en el controlador cuando el usuario termina de editarlo"""
        custom_alphabet = self.current_alphabet_entry.get()
        self.controller.set_custom_alphabet(custom_alphabet)