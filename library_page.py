from tkinter import *
from tkinter import messagebox
from app_settings import *

class LibraryPage(Frame):
    def __init__(self, parent, page_number, main_frame, update_callback=None):
        Frame.__init__(self, parent, bg="#8094dc", width=w_width, height=w_height)  # Brown background
        self.pack()

        self.page_number = page_number
        self.main_frame = main_frame
        self.update_callback = update_callback

        self.load_library_name()

        self.edit_name_entry = Entry(self, font=("Arial", 20))
        self.edit_name_entry.pack()

        # Frame for buttons
        button_frame = Frame(self, bg="#8094dc")  # Brown background
        button_frame.pack(pady=10)

        self.save_name_button = Button(button_frame, text="Save Name", font=button_font, command=self.save_library_name)
        self.save_name_button.pack(side=LEFT, padx=10)

        self.add_data_button = Button(button_frame, text="Add Data", font=button_font, command=self.open_data_entry_window)
        self.add_data_button.pack(side=LEFT, padx=10)

        self.data_entries = []  # To store data entries dynamically

        self.data_frame = Frame(self, bg="#8B4513")  # Brown background
        self.data_frame.pack(pady=20, padx=10)

        self.back_button = Button(self, bg=button_color, text="Home", font=button_font, width=20, height=2, command=self.back_to_main)
        self.back_button.pack(pady=50)

        # Load existing data entries from file
        self.load_data_entries()

    def load_library_name(self):
        try:
            with open("library_names.txt", "r") as file:
                library_names = file.readlines()
                if len(library_names) >= self.page_number:
                    self.page_label = Label(self, bg="#8094dc", fg="white", text=library_names[self.page_number - 1].strip(), font=head_font)  # White text on brown background
                    self.page_label.pack(pady=100)
                else:
                    self.page_label = Label(self, bg="#8094dc", fg="white", text=f"Library Page {self.page_number}", font=head_font)  # White text on brown background
                    self.page_label.pack(pady=100)
        except FileNotFoundError:
            self.page_label = Label(self, bg="#8094dc", fg="white", text=f"Library Page {self.page_number}", font=head_font)  # White text on brown background
            self.page_label.pack(pady=100)

    def save_library_name(self):
        new_name = self.edit_name_entry.get()
        with open("library_names.txt", "r+") as file:
            library_names = file.readlines()
            if len(library_names) >= self.page_number:
                library_names[self.page_number - 1] = f"{new_name}\n"
                file.seek(0)
                file.writelines(library_names)
            else:
                file.write(f"{new_name}\n")
        self.page_label.config(text=new_name)
        if self.update_callback:
            self.update_callback(self.page_number, new_name)

    def open_data_entry_window(self):
        data_entry_window = Toplevel(self)
        data_entry_window.title(f"Add Data - Library Page {self.page_number}")
        data_entry_window.geometry("400x300")

        label_data = Label(data_entry_window, text="Data:", font=("Arial", 14))
        label_data.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        entry_data = Entry(data_entry_window, width=30, font=("Arial", 12))
        entry_data.grid(row=0, column=1, padx=10, pady=10)

        label_note = Label(data_entry_window, text="Note:", font=("Arial", 14))
        label_note.grid(row=1, column=0, padx=10, pady=10, sticky=W)

        entry_note = Entry(data_entry_window, width=30, font=("Arial", 12))
        entry_note.grid(row=1, column=1, padx=10, pady=10)

        save_button = Button(data_entry_window, text="Save", font=button_font,
                             command=lambda: self.save_data_entry(entry_data.get(), entry_note.get(), data_entry_window))
        save_button.grid(row=2, columnspan=2, pady=20)

    def save_data_entry(self, data, note, window):
        if data.strip() != "":
            self.data_entries.append((data, note))
            self.data_entries.sort(key=lambda x: x[0].lower())  # Sort entries alphabetically by data (case insensitive)
            self.update_data_display()
            self.save_data_to_file()
            window.destroy()
        else:
            messagebox.showerror("Error", "Please enter some data.")

    def update_data_display(self):
        # Clear previous display
        for widget in self.data_frame.winfo_children():
            widget.destroy()

        # Display data entries
        for idx, (data, note) in enumerate(self.data_entries, start=1):
            data_label = Label(self.data_frame, text=data, font=("Monotype Corsiva", "25"))  # Brown background by default
            data_label.grid(row=idx, column=0, padx=10, pady=5, sticky=W)

            note_label = Label(self.data_frame, text=note, font=("Monotype Corsiva", "25"))  # Brown background by default
            note_label.grid(row=idx, column=1, padx=10, pady=5, sticky=W)

            delete_button = Button(self.data_frame, text="Delete", font=("Monotype Corsiva", "25"),
                                   command=lambda idx=idx: self.delete_data_entry(idx - 1))
            delete_button.grid(row=idx, column=2, padx=10, pady=5, sticky=W)

    def delete_data_entry(self, index):
        if 0 <= index < len(self.data_entries):
            del self.data_entries[index]
            self.update_data_display()
            self.save_data_to_file()
        else:
            messagebox.showerror("Error", "Invalid index.")

    def save_data_to_file(self):
        with open(f"library_page_{self.page_number}_data.txt", "w") as file:
            for data, note in self.data_entries:
                file.write(f"{data},{note}\n")

    def load_data_entries(self):
        try:
            with open(f"library_page_{self.page_number}_data.txt", "r") as file:
                for line in file:
                    data, note = line.strip().split(",")
                    self.data_entries.append((data, note))
                self.update_data_display()
        except FileNotFoundError:
            pass

    def back_to_main(self):
        self.pack_forget()  # Forget the library frame
        self.main_frame.pack()  # Repack the main_frame
