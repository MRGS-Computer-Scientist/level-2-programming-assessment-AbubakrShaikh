#Import modules
from tkinter import *
from app_settings import *

class start_page():
    def __init__(self, master):
        self.master = master  # Store the master window reference
        self.intro_frame = Frame(master, bg=bg_color, width=w_width, height=w_height) # Frame where everything for the first frame will be placed
        self.intro_frame.pack()

        self.instruct_label = Label(self.intro_frame, bg=bg_color, text="Some Placeholder Text", font=head_font) # Label for the title of the app
        self.instruct_label.grid(row=0, column=0, pady=220, columnspan=2)

        self.continue_button = Button(self.intro_frame, bg="#eeeeff", text="Continue", font=button_font, width=20, height=2) # Button to continue to the next part 
        self.continue_button.grid(row=1, column=0, padx=50, pady=125)

        self.exit_button = Button(self.intro_frame, bg="#eeeeff", text="Exit", font=button_font, width=20, height=2, command=self.exit_function_wrapper) # Button to exit program
        self.exit_button.grid(row=1, column=1, padx=50, pady=125)

    def exit_function_wrapper(self):
        exit_function(self.intro_frame)  # Pass intro_frame to the exit_function
