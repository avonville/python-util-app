from tkinter import *

class Pomodoro:
    """
    A class to manage a Pomodoro timer application.
    """

    def __init__(self, master):
        """
        Initializes the Pomodoro object with the main window and sets up the UI.

        Args:
            master: The root window (Tk object).
        """
        self.reps = 0
        self.timer = None
        self.WORK_MIN = 25
        self.SHORT_BREAK_MIN = 5
        self.LONG_BREAK_MIN = 20
        self.PINK = "#e2979c"
        self.RED = "#e7305b"
        self.GREEN = "#9bdeac"
        self.YELLOW = "#f7f5dd"
        self.FONT_NAME = "Courier"
        
        self.master = master
        master.title("Pomodoro")
        master.config(padx=100, pady=50, bg=self.YELLOW)

        

        self.tomato_img = PhotoImage(file="tomato.png")

        self.canvas = Canvas(master, width=200, height=224, bg=self.YELLOW, highlightthickness=0)
        self.canvas.create_image(103, 112, image=self.tomato_img)
        self.timer_text = self.canvas.create_text(100, 130, text="00:00", fill="white", font=(self.FONT_NAME, 35, "bold"))
        self.canvas.grid(column=1, row=1)

        self.title_label = Label(master, text="Timer", fg=self.GREEN, bg=self.YELLOW, font=(self.FONT_NAME, 50, "bold"))
        self.title_label.grid(column=1, row=0)

        self.start_button = Button(master, text="Start", highlightthickness=0, command=self.start_timer)
        self.start_button.grid(column=0, row=2)

        self.reset_button = Button(master, text="Reset", highlightthickness=0, command=self.reset_timer)
        self.reset_button.grid(column=2, row=2)

        self.check_marks = Label(master, fg=self.GREEN, bg=self.YELLOW, font=(self.FONT_NAME, 20, "bold"))
        self.check_marks.grid(column=1, row=3)

        self.master.mainloop()  # Start the Tkinter event loop here

    def reset_timer(self):
        """Resets the timer to its initial state."""
        self.reps = 0
        if self.timer:  # Check if timer is not None
            self.master.after_cancel(self.timer)
        self.canvas.itemconfig(self.timer_text, text="00:00")
        self.title_label.config(text="Timer", fg=self.GREEN)
        self.check_marks.config(text="")

    def start_timer(self):
        """Starts the Pomodoro timer mechanism."""
        self.reps += 1
        work_sec = self.WORK_MIN * 60
        short_break_sec = self.SHORT_BREAK_MIN * 60
        long_break_sec = self.LONG_BREAK_MIN * 60

        if self.reps % 8 == 0:
            self.count_down(long_break_sec)
            self.title_label.config(text="Long Break", fg=self.RED)
        elif self.reps % 2 == 0:
            self.count_down(short_break_sec)
            self.title_label.config(text="Break", fg=self.PINK)
        else:
            self.count_down(work_sec)
            self.title_label.config(text="Work", fg=self.GREEN)

    def count_down(self, count):
        """
        Counts down the time and updates the timer display.

        Args:
            count: The time in seconds to count down from.
        """
        count_min = count // 60
        count_sec = count % 60
        if count_sec < 10:
            count_sec = f"0{count_sec}"
        self.canvas.itemconfig(self.timer_text, text=f"{count_min}:{count_sec}")
        if count > 0:
            self.timer = self.master.after(1000, self.count_down, count - 1)
        else:
            self.start_timer()
            if self.reps % 2 == 0:
                marks = ""
                work_sessions = self.reps // 2
                for _ in range(work_sessions):
                    marks += "✔"
                self.check_marks.config(text=marks)
