from tkinter import *
from app_settings import *

#This will be what the user sees when the app opens
class start_page():
    def __init__(self):
        #Create a frame on which the functions will sit
        self.intro_frame = Frame(bg=bg_color, width=w_width, height=w_height)
        self.intro_frame.pack()

        #Label for the title
        self.instruct_label = Label(self.intro_frame, bg=bg_color, text="Some Placeholder Text", font=head_font)
        self.instruct_label.grid(row=0, column=0, pady=220, columnspan=2 )

        #Button to continue onto the program
        self.continue_button = Button(self.intro_frame, bg="#eeeeff", text="Continue", font=button_font, width=20, height=2)
        self.continue_button.grid(row=1, column=0, padx=50, pady=125)

        #Button for exiting the program
        self.exit_button = Button(self.intro_frame, bg="#eeeeff", text = "Exit", font=button_font, width=20, height=2, command=exit_function)
        self.exit_button.grid(row=1, column=1, padx=50, pady=125)

    #This function asks the user to confirm then destroys the initial_frame frame (need to move to app_settings.py)

