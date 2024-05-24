from tkinter import *
from app_settings import *

#This will be what the user sees when the app opens

class start_page():
    def __init__(self):
        intro_frame = Frame(bg=bg_color, width=w_width, height=w_height)
        intro_frame.pack()

        instruct_label = Label(intro_frame, bg=bg_color, text="Some Placeholder Text That I Use For Convinience")
        instruct_label.grid(row=0, column=1)

        continue_button = Button(intro_frame, bg="#666666", text="Continue", width=30, height=5)
        continue_button.grid(row=1, column=1)