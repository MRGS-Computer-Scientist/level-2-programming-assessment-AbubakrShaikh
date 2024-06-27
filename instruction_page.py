#Import modules
from app_settings import *
from login_page import LoginPage

class instruction_page():
    def __init__(self, master):
        self.master = master  # Store the master window reference
        self.intro_frame = Frame(master, bg=bg_color, width=w_width, height=w_height) # Frame where everything for the first frame will be placed
        self.intro_frame.pack()

        self.instruct_label = Label(self.intro_frame, bg=bg_color, text="Instructions/Guide", font=head_font) # Label for the title of the app
        self.instruct_label.grid(row=0, column=0, pady=220, columnspan=2)

        self.continue_button = Button(self.intro_frame, bg="#eeeeff", text="Continue", font=button_font, width=20, height=2, command=self.open_login_page) # Button to continue to the next part 
        self.continue_button.grid(row=1, column=0, padx=50, pady=125)

        self.exit_button = Button(self.intro_frame, bg=button_color, text="Exit", font=button_font, width=20, height=2, command=self.exit_function_wrapper) # Button to exit program
        self.exit_button.grid(row=1, column=1, padx=50, pady=125)

    def exit_function_wrapper(self):
        exit_function(self.intro_frame, self.master)  # Pass intro_frame to the exit_function

    def open_login_page(self):
        self.intro_frame.destroy()  # Destroy the intro frame
        login_page = LoginPage(self.master)  # Create an instance of the login page
