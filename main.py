##from calendar import c
from pomodoro import Pomodoro
from passwordgen import PasswordGen

from tkinter import *

# pomodoro = Pomodoro()

def start_application( application_class ):
        new_window = Toplevel()
        start_app = application_class(new_window)
        new_window.mainloop()


window = Tk()
window.title("Python Utility App")
window.config(padx=50, pady=50)
window.geometry("1000x1000")
window.resizable(True, True)

app_title = Label(text="Python Utility App", font=("Arial", 24, "bold"))
app_title.grid(row=0, column=2, pady=20)

# Pomodoro Timer
pomodoro_label = Button(text="Pomodoro Timer", command=lambda: start_application(Pomodoro), width=20, height=2)
pomodoro_label.grid(row=2, column=0, pady=10)

# Password Generator
password_gen_label = Button(text="Password Generator", command=lambda: start_application(PasswordGen), width=20, height=2)
password_gen_label.grid(row=3, column=0, pady=10)



window.mainloop()
