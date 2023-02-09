import tkinter

# Creating a window with Tk class
window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack(side="left")  # The packer "packs" the code

# This runs an infinite loop to keep our window running
window.mainloop()
