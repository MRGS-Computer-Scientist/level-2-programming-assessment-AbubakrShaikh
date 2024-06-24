#Import Modules
from tkinter import *
from intro_page import *
from app_settings import *

if __name__ == "__main__":
    window = Tk()
    window.configure(bg=bg_color)
    window.geometry(str(w_width)+"x"+str(w_height))
    window.title("My App")

    start_frame = start_page(window)  # Start the initial frame and pass window as the master.

    window.mainloop()
