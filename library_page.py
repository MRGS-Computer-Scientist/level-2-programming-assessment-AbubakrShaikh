from tkinter import *
from app_settings import *
from main_page import *

class LibraryPage:
    def __init__(self, master, page_number, main_frame):
        self.master = master
        self.main_frame = main_frame
        self.library_frame = Frame(master, bg=bg_color, width=w_width, height=w_height)
        self.library_frame.pack()

        self.page_number = page_number  # Store the page number to differentiate pages

        # Example label to show the page number (you can customize this as needed)
        self.page_label = Label(self.library_frame, bg=bg_color, text=f"Library Page {page_number}", font=head_font)
        self.page_label.pack(pady=100)

        # Example back button to return to main page
        self.back_button = Button(self.library_frame, bg=button_color, text="Home", font=button_font, width=20, height=2, command=self.back_to_main)
        self.back_button.pack(pady=50)

    def back_to_main(self):
        self.library_frame.pack_forget()  # Forget the library frame
        self.main_frame.pack() # Repack the main_frame
