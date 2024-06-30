#Import Modules
from tkinter import *
from login_page import LoginPage
from instruction_page import InstructionPage
from app_settings import *

if __name__ == "__main__":
    window = Tk()
    window.configure(bg=bg_color)
    window.geometry(str(w_width)+"x"+str(w_height))
    window.title("My App")

    with open("list_data.txt", "r") as user_file: # Open the file in read mode
        user_list = [line.strip() for line in user_file] # Read each line and convert it back to the original data type
    if not user_list:
        start_frame = InstructionPage(window)  # Start the initial frame and pass window as the master.
    else:
        start_frame = LoginPage(window)

    window.mainloop()
