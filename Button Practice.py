from tkinter import *

count = 1

def click():
    global count
    count += count*2
    print("Deedee has pressed the button " + str(count) + " times.")

window = Tk()

image = PhotoImage(file="deedee.png")
window.iconphoto(True, image)
window.title("Deedee don't touch that!")
window.geometry("500x200")
window.config(bg="pink")

button = Button(window,
                text="OoOoO What does this button do?",
                font=("Ariel",20,"bold"),
                image=image,
                compound="top",
                command=click,
                fg="red",
                bg="pink",
                activeforeground="red",
                activebackground="pink")
button.pack()

window.mainloop()