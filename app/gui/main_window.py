import customtkinter as ctk

from app import config as cf
from app.gui import components
from app.controllers.variables_controller import VariablesController 

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        # Controller instance
        self.controller = VariablesController()
        
        # Set the appearance mode and color theme
        # ctk.set_appearance_mode(cf.APPEARANCE_MODE)
        self.title("App Cipher")
        self.geometry("800x600")
        self.color_ui = (cf.BG_COLOR_DARK, cf.BG_COLOR_LIGHT)
        self.configure(background=self.color_ui)


        # Create 3 frames with grid layout
        # Frame with header and combobox
        self.title_frame = components.HeaderFrame(
            self,
            controller=self.controller,
            corner_radius=0,
            fg_color=(cf.BG_COLOR_LIGHT, cf.BG_COLOR_DARK)
        )
        self.title_frame.place(relx=0, rely=0, relwidth=1, relheight=0.1, anchor="nw")

        self.input_output_frame = components.InputOutputFrame(
            self,
            controller=self.controller,  # Pasamos el controlador a InputOutputFrame
            corner_radius=0,
            fg_color=(cf.BG_COLOR_LIGHT, cf.BG_COLOR_DARK)
        )
        self.input_output_frame.place(relx=0, rely=0.1, relwidth=1, relheight=0.7, anchor="nw")

        self.alphabet_frame = components.AlphabetFrame(
            self,
            controller=self.controller,
            corner_radius=0,
            fg_color=(cf.BG_COLOR_LIGHT, cf.BG_COLOR_DARK)
        )
        self.alphabet_frame.place(relx=0, rely=0.8, relwidth=1, relheight=0.2, anchor="nw")

