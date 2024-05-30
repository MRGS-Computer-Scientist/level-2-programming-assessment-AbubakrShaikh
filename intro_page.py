from tkinter import *
from app_settings import *

#This will be what the user sees when the app opens




class start_page():
    def __init__(self):
        self.intro_frame = Frame(bg=bg_color, width=w_width, height=w_height)
        self.intro_frame.pack()

        self.instruct_label = Label(self.intro_frame, bg=bg_color, text="Some Placeholder Text", font=head_font)
        self.instruct_label.grid(row=0, column=0, pady=220, columnspan=2 )

        continue_button = Button(self.intro_frame, bg="#eeeeff", text="Continue", font=button_font, width=20, height=2)
        continue_button.grid(row=1, column=0, padx=50, pady=125)

        self.exit_button = Button(self.intro_frame, bg="#eeeeff", text = "Exit", font=button_font, width=20, height=2, command=self.collect_name)
        self.exit_button.grid(row=1, column=1, padx=50, pady=125)

    #This function collects the user's name then destroys the initial_frame frame
    def collect_name(self):
        self.confirm_window = Tk()

        self.yes_no = IntVar()

        self.confirm_question = Label(self.confirm_window, text="Are you sure you want to exit?")
        self.confirm_question.grid(row=0, column=0, columnspan=2)

        self.confirm_yes = Button(self.confirm_window, text="Yes", command=lambda:[self.confirm_window.destroy(), self.intro_frame.destroy()])
        self.confirm_yes.grid(row=1, column=0)

        

        self.confirm_no = Button(self.confirm_window, text="No", command=self.confirm_window.destroy())
        self.confirm_no.grid(row=1, column=1)

        self.confirm_window.mainloop()


