from app_settings import *




#This will be the second page after the intro page where the user will see the main content

class MainPage():
    def __init__(self, master):
        self.master = master
        self.main_frame = Frame(background="#8094dc", width=500, height=500)
        self.main_frame.grid()

        self.button_one = Button(self.main_frame, text="Some Placeholder Text")
        self.button_one.grid(row=0, column=0, padx=125, pady=30)

        self.button_two = Button(self.main_frame, text="Some Placeholder Text")
        self.button_two.grid(row=0, column=1, padx=125, pady=30)
        
        self.button_three = Button(self.main_frame, text="Some Placeholder Text")
        self.button_three.grid(row=0, column=2, padx=125, pady=30)

        self.button_four = Button(self.main_frame, text="Some Placeholder Text", width=30, height=15)
        self.button_four.grid(row=0, column=3, padx=125, pady=30)


        self.main_title = Label(self.main_frame, bg=bg_color, text="Some Placeholder Text", font=head_font)
        self.main_title.grid(row=1, column=0, pady=50, columnspan=4)
        
        self.button_five = Button(self.main_frame, text="Some Placeholder Text")
        self.button_five.grid(row=2, column=0, padx=125, pady=30)

        self.button_six = Button(self.main_frame, text="Some Placeholder Text")
        self.button_six.grid(row=2, column=1, padx=125, pady=30)

        self.button_seven = Button(self.main_frame, text="Some Placeholder Text")
        self.button_seven.grid(row=2, column=2, padx=125, pady=30)

        self.button_eight = Button(self.main_frame, text="Some Placeholder Text")
        self.button_eight.grid(row=2, column=3, padx=125, pady=30)