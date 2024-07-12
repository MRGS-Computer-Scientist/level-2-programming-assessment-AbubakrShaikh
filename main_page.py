from tkinter import *
from app_settings import *
from library_page import LibraryPage

class MainPage(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg=bg_color, width=w_width, height=w_height)
        self.pack_propagate(False)  # Prevent frame from resizing to fit content
        self.pack()

        self.library_names = self.load_library_names()

        self.title_label = Label(self, text="Library Pages", font=head_font, bg=bg_color)
        self.title_label.grid(row=0, column=0, columnspan=4, pady=20)

        self.create_buttons()

    def load_library_names(self):
        try:
            with open("library_names.txt", "r") as file:
                library_names = file.readlines()
                return [name.strip() for name in library_names]
        except FileNotFoundError:
            return []

    def create_buttons(self):
        self.buttons = []
        for i in range(1, 9):  # Create 8 buttons
            button_text = self.get_library_name(i)
            button = Button(self, text=button_text, font=plus_font, width=12, height=4,
                            command=lambda num=i: self.open_library_page(num))
            row = 1 if i <= 4 else 2
            column = i - 1 if i <= 4 else i - 5
            button.grid(row=row, column=column, padx=20, pady=20)
            self.buttons.append(button)

    def get_library_name(self, page_number):
        if page_number <= len(self.library_names):
            return self.library_names[page_number - 1]
        else:
            return f"Library Page {page_number}"

    def open_library_page(self, page_number):
        self.pack_forget()  # Hides the main frame
        self.library_page = LibraryPage(self.master, page_number, self, self.update_button_text)  # Pass callback function

    def update_button_text(self, page_number, new_name):
        self.library_names[page_number - 1] = new_name
        self.buttons[page_number - 1].config(text=new_name)

    def show(self):
        self.pack()