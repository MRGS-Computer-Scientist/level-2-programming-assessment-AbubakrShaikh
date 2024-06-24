from tkinter import *
from app_settings import *
from library_page import *

class MainPage:
    def __init__(self, master):
        self.master = master
        self.main_frame = Frame(background="#8094dc", width=w_width, height=w_height)
        self.main_frame.pack_propagate(False)  # Prevent frame from resizing to fit content
        self.main_frame.pack()

        # Top row buttons
        self.top_buttons = []
        for i in range(4):
            button = Button(self.main_frame, text=f"Library {i+1}", font=plus_font, width=12, height=4,
                            command=lambda num=i+1: self.open_library_page(num))
            button.grid(row=0, column=i, padx=20, pady=20)
            self.top_buttons.append(button)

        # Middle row placeholder text
        self.main_title = Label(self.main_frame, bg=bg_color, text="Some Placeholder Text", font=head_font)
        self.main_title.grid(row=1, column=0, columnspan=4, pady=50)

        # Bottom row buttons
        self.bottom_buttons = []
        for i in range(4):
            button = Button(self.main_frame, text=f"Library {i+5}", font=plus_font, width=12, height=4,
                            command=lambda num=i+5: self.open_library_page(num))
            button.grid(row=2, column=i, padx=20, pady=20)
            self.bottom_buttons.append(button)

    def open_library_page(self, page_number):
        self.main_frame.pack_forget()  # Hides the main frame
        self.library_page = LibraryPage(self.master, page_number, self.main_frame)  # Create an instance of the respective library page
