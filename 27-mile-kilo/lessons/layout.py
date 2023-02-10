from tkinter import *

# Creating a new window and configurations
window = Tk()
window.title("Hello from the other side")
window.minsize(width=500, height=500)
window.config(padx=50, pady=50)

# Label
label = Label(text="This is old text")
label.config(text="This is new text")
label.grid(column=0, row=0)
label.config(padx=20, pady=40)


# Buttons
def action():
    print("Do something")


# calls action() when pressed
button = Button(text="Click Me", command=action)
button.grid(column=1, row=1)

button2 = Button(text="New Button!", command=action)
button2.grid(column=2, row=0)

# Entries
entry = Entry(width=30)
# Add some text to begin with
entry.insert(END, string="Some text to begin with.")
# Gets text in entry
print(entry.get())

entry.grid(column=3, row=2)

window.mainloop()
