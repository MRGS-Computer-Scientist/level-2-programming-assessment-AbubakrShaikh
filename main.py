from tkinter import *


window = Tk()
window.geometry("500x500")
window.title("My App")

intro_frame = Frame(background="#8094dc", width=500, height=500)
intro_frame.grid()

intro_title = Label(background="#8094dc", text="Welcome to...", font=25)
intro_title.grid(row=0, column=0)

window.mainloop()