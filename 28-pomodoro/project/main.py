from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    # Calling the countdown
    count_down(5 * 60)


def reset_timer():
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    # Formatting the time
    count_min = math.floor(count / 60)
    count_sec = count % 60

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #

# Creating the window
window = Tk()
window.title("Pomodoro~")
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas Widget - Allows images to be placed on top of each other
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

# Have to use PhotoImage to use image
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Title Label
label_title = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
label_title.grid(column=1, row=0)

# Buttons
start_btn = Button(text="START", command=start_timer, fg=GREEN, activeforeground=RED, highlightbackground=YELLOW,
                   padx=2, pady=2, font=(FONT_NAME, 16))
start_btn.grid(column=0, row=2)

reset_btn = Button(text="RESET", command=reset_timer, fg=RED, highlightbackground=YELLOW, activeforeground=GREEN,
                   padx=2, pady=2, font=(FONT_NAME, 16))
reset_btn.grid(column=2, row=2)

# Checkmark Label
check_marks = "✔"

check_label = Label(text=check_marks, bg=YELLOW, fg=GREEN)
check_label.grid(column=1, row=3)

# Allows window to run
window.mainloop()
