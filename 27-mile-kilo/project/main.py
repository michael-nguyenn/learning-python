from tkinter import *

# Create a new window and it's configs
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=200)
window.config(padx=50, pady=20)

# Blank label for grid setup
label = Label(text="")
label.grid(column=0, row=0)

# Input field to convert
entry = Entry(width=5)
entry.insert(END, string="0")
entry.grid(column=1, row=0)

# Labels
label1 = Label(text="Miles")
label1.grid(column=2, row=0)

label2 = Label(text="is equal to")
label2.grid(column=0, row=2)

label3 = Label(text="0")
label3.grid(column=1, row=2)

label4 = Label(text="Km")
label4.grid(column=2, row=2)


# Button
def convert_temp():
    usr_input = int(entry.get())

    label3.config(text=round(float(usr_input * 1.609), 2))


button = Button(text="Calculate", command=convert_temp)
button.grid(column=1, row=3)
window.mainloop()
