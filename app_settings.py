#Import modules
from tkinter import *

# Variables to be used in code
w_width = 1600 # Width of window and frames
w_height = 900 # Height of window and frames

app_title = "AppTITLE" # Title of window

bg_color = "#8094dc" # Default background of window and frames

head_font = ("Forte", "40") # Font for the main header
button_font = ("Freestyle Script", "20", "bold") # Font for buttons


def exit_function(intro_frame, window):  # Pass intro_frame as an argument
    confirm_window = Tk() # Seperate window for exit confirmation
    confirm_window.geometry("175x50")
    confirm_window.configure(bg=bg_color)
    
    def pressed_yes(): # Function to run if "yes" button is pressed
        confirm_window.destroy()
        intro_frame.destroy()
        window.destroy()

    def pressed_no(): # Function to run if "no" button is pressed
        confirm_window.destroy()

    confirm_question = Label(confirm_window, bg=bg_color, text="Are you sure you want to exit?") # Question to confirm program exit
    confirm_question.grid(row=0, column=0, columnspan=2)

    confirm_yes = Button(confirm_window, text="Yes", command=pressed_yes) # Button to confirm exit program
    confirm_yes.grid(row=1, column=0)

    confirm_no = Button(confirm_window, text="No", command=pressed_no) # Button to cancel program exit
    confirm_no.grid(row=1, column=1)

    confirm_window.mainloop()