from tkinter import *
from app_settings import *

#This will be what the user sees when the app opens

class start_page():
    def __init__(self):
        intro_frame = Frame(bg=bg_color, width=w_width, height=w_height)
        intro_frame.grid()
#Chaneg window color
        continue_button = Button(intro_frame, bg=bg_color, text="Continue", width=10, height=5)
        continue_button.grid()