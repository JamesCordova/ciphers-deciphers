import customtkinter as ctk

from app import config as cf

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("App Cipher")
        self.geometry("800x600")
        self.color_ui = (cf.BG_COLOR_DARK, cf.BG_COLOR_LIGHT)
        self.configure(background = self.color_ui)

        # Create a label
        self.label = ctk.CTkLabel(self, text="Hello, World!")
        self.label.grid(pady=20)

        # Create a button
        self.button = ctk.CTkButton(self, text="Click Me", command=self.on_button_click)
        self.button.pack(pady=20)

    def on_button_click(self):
        print("Button clicked!")
        self.label.configure(text="Button clicked!")