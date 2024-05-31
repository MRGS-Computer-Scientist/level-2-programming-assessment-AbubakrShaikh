from tkinter import *

#Function to exit the app
def exit_function():
    confirm_window = Tk()
    
    def pressed_yes():
        confirm_window.destroy()
        intro_frame.destroy()

    def pressed_no():
        confirm_window.destroy()

    confirm_question = Label(confirm_window, text="Are you sure you want to exit?")
    confirm_question.grid(row=0, column=0, columnspan=2)

    confirm_yes = Button(confirm_window, text="Yes", command=pressed_yes)
    confirm_yes.grid(row=1, column=0)

    confirm_no = Button(confirm_window, text="No", command=pressed_no)
    confirm_no.grid(row=1, column=1)

    confirm_window.mainloop()




#Variables to be used in code
w_width = 1600
w_height = 900

app_title = "AppTITLE"

bg_color = "#8094dc"

head_font = ("Forte", "40")
button_font = ("Freestyle Script", "20", "bold")

