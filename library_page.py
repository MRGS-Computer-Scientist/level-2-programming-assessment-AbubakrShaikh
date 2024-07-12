from tkinter import *
from app_settings import *

class LibraryPage(Frame):
    def __init__(self, parent, page_number, main_frame, update_callback=None):
        Frame.__init__(self, parent, bg=bg_color, width=w_width, height=w_height)
        self.pack()

        self.page_number = page_number
        self.main_frame = main_frame
        self.update_callback = update_callback

        self.load_library_name()

        self.edit_name_entry = Entry(self, font=("Arial", 20))
        self.edit_name_entry.pack()

        self.save_name_button = Button(self, text="Save Name", font=button_font, command=self.save_library_name)
        self.save_name_button.pack()

        self.back_button = Button(self, bg=button_color, text="Home", font=button_font, width=20, height=2, command=self.back_to_main)
        self.back_button.pack(pady=50)

    def load_library_name(self):
        try:
            with open("library_names.txt", "r") as file:
                library_names = file.readlines()
                if len(library_names) >= self.page_number:
                    self.page_label = Label(self, bg=bg_color, text=library_names[self.page_number - 1].strip(), font=head_font)
                    self.page_label.pack(pady=100)
                else:
                    self.page_label = Label(self, bg=bg_color, text=f"Library Page {self.page_number}", font=head_font)
                    self.page_label.pack(pady=100)
        except FileNotFoundError:
            self.page_label = Label(self, bg=bg_color, text=f"Library Page {self.page_number}", font=head_font)
            self.page_label.pack(pady=100)

    def save_library_name(self):
        new_name = self.edit_name_entry.get()
        with open("library_names.txt", "r+") as file:
            library_names = file.readlines()
            if len(library_names) >= self.page_number:
                library_names[self.page_number - 1] = f"{new_name}\n"
                file.seek(0)
                file.writelines(library_names)
            else:
                file.write(f"{new_name}\n")
        self.page_label.config(text=new_name)
        if self.update_callback:
            self.update_callback(self.page_number, new_name)

    def back_to_main(self):
        self.pack_forget()  # Forget the library frame
        self.main_frame.pack()  # Repack the main_frame
