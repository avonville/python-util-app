from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

class PasswordGen:
    """
    A class to manage passwords, providing functionalities to generate, save,
    and search for passwords, with a graphical user interface.
    """
    def __init__(self, master):
        """
        Initializes the PasswordGen object with the main window and sets up the UI.

        Args:
            master: The root window (Tk object).
        """
        self.master = master
        master.title("Password Manager")
        master.config(padx=50, pady=50)
        
        self.logo = PhotoImage(file="logo.png")
        self.canvas = Canvas(master, width=200, height=200)
        self.canvas.create_image(100, 100, image=self.logo)
        self.canvas.grid(row=0, column=1)

        self.website_label = Label(master, text="Website:")
        self.website_label.grid(row=1, column=0)
        self.website_input = Entry(master, width=34)
        self.website_input.focus()
        self.website_input.grid(row=1, column=1)

        self.search_button = Button(master, text="Search", command=self.search)
        self.search_button.grid(row=1, column=2)

        self.user_label = Label(master, text="Email/Username:")
        self.user_label.grid(row=2, column=0)
        self.user_input = Entry(master, width=52)
        self.user_input.insert(END, "austinv@email.com")
        self.user_input.grid(row=2, column=1, columnspan=2)

        self.password_label = Label(master, text="Password:")
        self.password_label.grid(row=3, column=0)
        self.password_input = Entry(master, width=34)
        self.password_input.grid(row=3, column=1)
        self.password_gen = Button(master, text="Generate Password", command=self.gen_pass)
        self.password_gen.grid(row=3, column=2)

        self.add_button = Button(master, text="Add", width=44, command=self.save_pass)
        self.add_button.grid(row=4, column=1, columnspan=2)

    def search(self):
        """
        Searches for a website in the data.json file and displays the corresponding
        email and password if found.  Displays error messages using messagebox
        if the file is not found, or the website is not found.
        """
        website = self.website_input.get()
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            messagebox.showinfo(title="Error Loading File", message="No Data File Found")
        else:
            if website in data:
                messagebox.showinfo(title=website, message=f" Email: {data[website]['email']}\n Password: {data[website]['password']}")
            else:
                messagebox.showinfo(title="Error", message="Website not found")

    def gen_pass(self):
        """
        Generates a random password, inserts it into the password input field,
        and copies it to the clipboard.
        """
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        rand_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
        rand_sym = [random.choice(symbols) for _ in range(random.randint(2, 4))]
        rand_num = [random.choice(numbers) for _ in range(random.randint(2, 4))]

        password_list = rand_letters + rand_sym + rand_num
        random.shuffle(password_list)
        password = "".join(password_list)

        self.password_input.delete(0, END)  # Corrected line
        self.password_input.insert(0, password)
        pyperclip.copy(password)

    def save_pass(self):
        """
        Saves the website, email, and password to a JSON file (data.json).
        Displays an error message if any of the fields are empty.
        """
        website = self.website_input.get()
        user = self.user_input.get()
        password = self.password_input.get()
        new_data = {
            website: {
                "email": user,
                "password": password,
            }
        }
        if not website or not password:
            messagebox.showinfo(title="Missing Information", message="Cannot Leave Blank Entries")
            return
        else:
            try:
                with open("data.json", "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                self.website_input.delete(0, END)
                self.password_input.delete(0, END)

