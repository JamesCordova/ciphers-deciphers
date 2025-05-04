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
        self.algorithms = ["Option 1", "Option 2", "Option 3"]
        self.algorithm_selected = [self.algorithms[0]]
        
        # Create 3 frames with grid layout
        # Frame with header and combobox
        self.title_frame = components.HeaderFrame(self, list_choices=self.algorithms, selected=self.algorithm_selected, corner_radius=0, fg_color=(cf.BG_COLOR_LIGHT, cf.BG_COLOR_DARK), border_color=cf.ERROR_COLOR_DARK, border_width=1)
        self.title_frame.place(relx=0, rely=0, relwidth=1, relheight=0.1, anchor="nw")
        self.input_output_frame = ctk.CTkFrame(self, corner_radius=0, fg_color=(cf.BG_COLOR_LIGHT, cf.BG_COLOR_DARK), border_color=cf.ERROR_COLOR_DARK, border_width=1)
        self.input_output_frame.place(relx=0, rely=0.1, relwidth=1, relheight=0.8, anchor="nw")
        self.alphabet_frame = ctk.CTkFrame(self, corner_radius=0, fg_color=(cf.BG_COLOR_LIGHT, cf.BG_COLOR_DARK), border_color=cf.ERROR_COLOR_DARK, border_width=1)
        self.alphabet_frame.place(relx=0, rely=0.9, relwidth=1, relheight=0.1, anchor="nw")
        
        # Setting the title frame
        self.button = ctk.CTkButton(self.input_output_frame, text="Click Me", command=self.on_button_click)
        self.button.place(relx=0.5, rely=0.5, anchor="center")
    
        
    def on_button_click(self):
        print("Selected algorithm:", self.algorithm_selected)