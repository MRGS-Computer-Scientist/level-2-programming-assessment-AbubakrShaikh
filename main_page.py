from app_settings import *




#This will be the second page after the intro page where the user will see the main content

class MainPage():
    def __init__(self, master):
        self.master = master
        self.main_frame = Frame(background="#8094dc", width=500, height=500)
        self.main_frame.grid()

        self.main_title = Label(self.main_frame, bg=bg_color, text="Some Placeholder Text", font=head_font)
        self.main_title.grid(row=1, column=0, pady=50, columnspan=4)

        