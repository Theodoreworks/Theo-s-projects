from tkinter import *
window = Tk()
window.geometry("500x300")
name = input("what is your name")
greeting = Label(window, text ="Hello " + name)
greeting.pack()
window.mainloop()
