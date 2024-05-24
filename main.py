from intro_page import *
from main_page import *


#Main window, all frames are displayed here

from tkinter import *

if __name__ == "__main__":
    window = Tk()
    window.configure(bg=bg_color)
    window.geometry(str(w_width)+"x"+str(w_height))
    window.title("My App")

    #Initial Frame
    start_frame = start_page()


    window.mainloop()