from tkinter import *

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

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

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
canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"))
canvas.pack()

# Allows window to run
window.mainloop()
