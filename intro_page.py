from tkinter import *
from app_settings import *

#This will be what the user sees when the app opens

class start_page():
    def __init__(self):
        intro_frame = Frame(bg=bg_color, width=w_width, height=w_height)
        intro_frame.pack()

        instruct_label = Label(intro_frame, bg=bg_color, text="Some Placeholder Text", font=head_font)
        instruct_label.grid(row=0, column=0, pady=220, columnspan=2 )

        continue_button = Button(intro_frame, bg="#eeeeff", text="Continue", font=button_font, width=20, height=2)
        continue_button.grid(row=1, column=0, padx=50, pady=125)

        exit_button = Button(intro_frame, bg="#aaaaff", text="Exit", font=button_font, width=20, height=2)
        exit_button.grid(row=1, column=1, padx=50, pady=125)

