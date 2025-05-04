import customtkinter as ctk

class HeaderFrame(ctk.CTkFrame):
    def __init__(self, master=None, list_choices=None, selected:str=None, **kwargs):
        super().__init__(master, **kwargs)
        self.list = list_choices
        self.selected = selected
        # Create a title_label
        self.title_label = ctk.CTkLabel(self, text=self.selected[0], wraplength=570, anchor="w")
        self.title_label.place(relx=0.02, rely=0.5, relwidth=0.75, anchor="w")
        # Create a Combobox
        self.combobox = ctk.CTkComboBox(self, values=list_choices, command=self.on_combobox_change, variable=self.selected, state="readonly")
        self.combobox.set(self.selected[0])
        self.combobox.place(relx=0.78, rely=0.5, relwidth=0.21, anchor="w")
        
    def on_combobox_change(self, choice):
        # Update the title_label text with the selected choice
        print(f"Combobox changed to: {choice}")
        self.selected[0] = choice
        self.title_label.configure(text=choice)