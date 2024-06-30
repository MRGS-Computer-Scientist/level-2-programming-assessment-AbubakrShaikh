# Import necessary modules
from tkinter import *
from app_settings import *
from login_page import LoginPage

# Define the instruction page class
class InstructionPage:
    def __init__(self, master):
        self.master = master
        self.intro_frame = Frame(master, bg=bg_color, width=w_width, height=w_height)
        self.intro_frame.pack()

        self.instruct_label = Label(self.intro_frame, bg=bg_color, text="Welcome to Collectiva", font=head_font) # Label for the title of the app
        self.instruct_label.grid(row=0, column=0, pady=20, columnspan=2)

        # Left box for the first message
        left_frame = Frame(self.intro_frame, bg="#EEEEEE", padx=20, pady=20)  # Light grey background
        left_frame.grid(row=2, column=0, padx=50, pady=50)

        text_box1 = Label(left_frame, bg="#EEEEEE", text="If this is your first time using this app, please enter your username and password, then click 'Create Account'. This will save your account details for every time you log in.", font=instruction_font, wraplength=300, justify='left')
        text_box1.pack()

        # Right box for the second message
        right_frame = Frame(self.intro_frame, bg="#EEEEEE", padx=20, pady=20)  # Light grey background
        right_frame.grid(row=2, column=1, padx=50, pady=50)

        text_box2 = Label(right_frame, bg="#EEEEEE", text="After you log in, there will be 8 buttons, each of which will take you to a separate page. Each of these pages can be used to sort different items and can be adjusted to an extent.", font=instruction_font, wraplength=300, justify='left')
        text_box2.pack()

        # Title label
        self.instruct_label = Label(self.intro_frame, bg=bg_color, text="Instructions", font=("Helvetica", "30", "bold"))
        self.instruct_label.grid(row=1, column=0, pady=100, columnspan=2)

        # Continue button
        self.continue_button = Button(self.intro_frame, bg="#eeeeff", text="Continue", font=button_font, width=20, height=2, command=self.open_login_page)
        self.continue_button.grid(row=3, column=0, padx=50, pady=50)

        # Exit button
        self.exit_button = Button(self.intro_frame, bg=button_color, text="Exit", font=button_font, width=20, height=2, command=self.exit_function_wrapper)
        self.exit_button.grid(row=3, column=1, padx=50, pady=50)

    def exit_function_wrapper(self):
        exit_function(self.intro_frame, self.master)

    def open_login_page(self):
        self.intro_frame.destroy()
        login_page = LoginPage(self.master)

