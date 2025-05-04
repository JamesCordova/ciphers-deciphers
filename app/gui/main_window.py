import customtkinter as ctk

from app import config as cf
from app.gui import components

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("App Cipher")
        self.geometry("800x600")
        self.color_ui = (cf.BG_COLOR_DARK, cf.BG_COLOR_LIGHT)
        self.configure(background = self.color_ui)
        
        # Not Widegets variables
        self.algorithms = ["Transformación Columnar Simple",
                           "Transformación Columnar Doble",
                           "Rejillas criptográficas",
                           "Transposición de filas",
                           "Permutación por series",
                           "Playfair"]
        self.algorithm_selected = [self.algorithms[0]]
        
        # Create 3 frames with grid layout
        # Frame with header and combobox
        self.title_frame = components.HeaderFrame(self, list_choices=self.algorithms, selected=self.algorithm_selected, corner_radius=0, fg_color=(cf.BG_COLOR_LIGHT, cf.BG_COLOR_DARK))
        self.title_frame.place(relx=0, rely=0, relwidth=1, relheight=0.1, anchor="nw")
        self.input_output_frame = components.InputOutputFrame(self, corner_radius=0, fg_color=(cf.BG_COLOR_LIGHT, cf.BG_COLOR_DARK), border_color=cf.ERROR_COLOR_DARK, border_width=1)
        self.input_output_frame.place(relx=0, rely=0.1, relwidth=1, relheight=0.7, anchor="nw")
        self.alphabet_frame = components.AlphabetFrame(self, corner_radius=0, fg_color=(cf.BG_COLOR_LIGHT, cf.BG_COLOR_DARK), border_color=cf.ERROR_COLOR_DARK, border_width=1)
        self.alphabet_frame.place(relx=0, rely=0.8, relwidth=1, relheight=0.2, anchor="nw") 

