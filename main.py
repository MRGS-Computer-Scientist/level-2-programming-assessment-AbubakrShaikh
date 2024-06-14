#Import modules
from intro_page import *
from tkinter import *

if __name__ == "__main__": # Run main window
    # Define window and its properties
    window = Tk()
    window.configure(bg=bg_color)
    window.geometry(str(w_width)+"x"+str(w_height))
    window.title("My App")

    #Create instance of StartPage
    start_frame = start_page(window)  # Start the initial frame and pass window as the master.

    window.mainloop()
