from tkinter import *
from app_settings import *

class LoginPage:
    def __init__(self, master):
        self.master = master
        self.login_frame = Frame(master, bg=bg_color, width=w_width, height=w_height)
        self.login_frame.pack()

        self.username_label = Label(self.login_frame, bg=bg_color, text="Username:", font=("Arial", 20))
        self.username_label.grid(row=0, column=0, pady=30, columnspan=2)

        self.password_label = Label(self.login_frame, bg=bg_color, text="Password:", font=("Arial", 20))
        self.password_label.grid(row=2, column=0, pady=30, columnspan=2)

        self.username_entry = Entry(self.login_frame, font=("Arial", 20))
        self.username_entry.grid(row=1, column=0, pady=20, columnspan=2)

        self.password_entry = Entry(self.login_frame, show="*", font=("Arial", 20))
        self.password_entry.grid(row=3, column=0, pady=20, columnspan=2)

        self.login_button = Button(self.login_frame, bg="#eeeeff", text="Login", font=button_font, width=20, height=2, command=self.login)
        self.login_button.grid(row=4, column=0, padx=50, pady=125)

        self.exit_button = Button(self.login_frame, bg="#eeeeff", text="Exit", font=button_font, width=20, height=2, command=self.exit_function_wrapper)
        self.exit_button.grid(row=4, column=1,padx=50, pady=125)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Check if username and password match stored credentials (mock implementation)
        if username == "admin" and password == "password":
            self.login_frame.destroy()  # Destroy the intro frame
            main_page = MainPage(self.master)  # Create an instance of the login page

    def exit_function_wrapper(self):
        exit_function(self.intro_frame, self.master)  # Pass intro_frame to the exit_function