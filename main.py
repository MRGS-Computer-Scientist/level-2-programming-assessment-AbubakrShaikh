from intro_page import *
from main_page import *


#Main window, all frames are displayed here

window = Tk()

window.geometry(str(w_width)+"x"+str(w_height))
window.title("My App")

#First frame
initial_page = start_page()



window.mainloop()