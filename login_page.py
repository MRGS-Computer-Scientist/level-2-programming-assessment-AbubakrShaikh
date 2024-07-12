from tkinter import *
from app_settings import *
from main_page import MainPage
import re  # Import regular expression module for validation

# Function to validate if a string is alphanumeric
def is_alphanumeric(s):
    return bool(re.match('^[a-zA-Z0-9]*$', s))

with open("list_data.txt", "r") as user_file: # Open the file in read mode
    user_list = [line.strip() for line in user_file] # Read each line and convert it back to the original data type

with open("password.txt", "r") as pass_file: # Open the file in read mode
    pass_list = [line.strip() for line in pass_file] # Read each line and convert it back to the original data type

all_passwords = []

class LoginPage:
    def __init__(self, master):
        self.master = master
        self.login_frame = Frame(master, bg=bg_color, width=w_width, height=w_height) # Set frame for LoginPage
        self.login_frame.pack()

        self.title_label = Label(self.login_frame, bg=bg_color, text="Some Placeholder Text", font=head_font) # Label for the title of the app
        self.title_label.grid(row=0, column=0, pady=50, columnspan=2)

        self.username_label = Label(self.login_frame, bg=bg_color, text="Username:", font=("Arial", 20)) # Label for username entry
        self.username_label.grid(row=1, column=0, pady=20, columnspan=2)

        self.password_label = Label(self.login_frame, bg=bg_color, text="Password:", font=("Arial", 20)) # Label for password entry
        self.password_label.grid(row=3, column=0, pady=20, columnspan=2)

        self.username_entry = Entry(self.login_frame, font=("Arial", 20))
        self.username_entry.grid(row=2, column=0, pady=20, columnspan=2)

        self.password_entry = Entry(self.login_frame, show="*", font=("Arial", 20))
        self.password_entry.grid(row=4, column=0, pady=20, columnspan=2)

        if not user_list:
            print(user_list)
            self.create_button = Button(self.login_frame, bg="#eeeeff", text="Create Account", font=button_font, width=20, height=2, command=self.create_account)
            self.create_button.grid(row=5, column=0, padx=5, pady=25)

        else:
            self.login_button = Button(self.login_frame, bg="#eeeeff", text="Login", font=button_font, width=20, height=2, command=self.login)
            self.login_button.grid(row=5, column=0, padx=5, pady=25)

        self.exit_button = Button(self.login_frame, bg=button_color, text="Exit", font=button_font, width=20, height=2, command=self.exit_function_wrapper)
        self.exit_button.grid(row=5, column=1,padx=5, pady=25, columnspan=2)


    def error_function_wrapper(self):
        error_function(self.login_frame, self.master)  # Pass intro_frame to the exit_function

    def create_account(self):
        create_username = self.username_entry.get().strip()
        create_password = self.password_entry.get().strip()

        # Validate username and password
        if not (1 <= len(create_username) <= 16 and is_alphanumeric(create_username)):
            error_function()
            return
        if not (1 <= len(create_password) <= 16 and is_alphanumeric(create_password)):
            error_function()
            return

        # Check for existing username
        if create_username in user_list:
            exist_error()
        else:
            # Valid username and password, proceed to save
            user_list.append(create_username)
            with open("list_data.txt", "w") as user_file:
                for item in user_list:
                    user_file.write(str(item) + "\n")

            pass_list.append(create_password)
            with open("password.txt", "w") as pass_file:
                for item in pass_list:
                    pass_file.write(str(item) + "\n")

            # Inform user about successful account creation
            account_window = Tk()
            account_window.geometry("160x50")
            account_window.configure(bg=bg_color)
            account_window.title("Account Info")
            create_message = Label(account_window, bg=bg_color, text="Account successfully created")
            create_message.grid(row=0, column=0)
            exit_account = Button(account_window, text="Close", command=account_window.destroy)
            exit_account.grid(row=1, column=0)

            self.login_frame.destroy()  # Destroy the login frame
            main_page = MainPage(self.master)  # Create an instance of the main page

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Check if username and password match stored credentials (mock implementation)
        if username == "":
            error_function()

        else:
            if username in user_list:
                pass_check = user_list.index(username)
                
                if pass_list[pass_check] == password:

                    self.login_frame.destroy()  # Destroy the login frame
                    main_page = MainPage(self.master)  # Create an instance of the main page

                    
                else:
                    match_error()
            else:
                match_error()
            

            

    def exit_function_wrapper(self):
        exit_function(self.login_frame, self.master)  # Pass intro_frame to the exit_function


