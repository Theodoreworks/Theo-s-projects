from tkinter import *
window = Tk()
window.geometry("500x300")
Label(window, text= "Builders club Registration form", font= "ar 15 bold").grid(row =0,column=3)

name = Label(window,text="name")
gender = Label(window,text="gender")
phone = Label(window,text="phone")
email = Label(window,text="email")
city = Label(window,text="city")
interest = Label(window,text="interest")

name.grid(row= 1, column = 2)
gender.grid(row= 2, column = 2)
phone.grid(row= 3, column = 2)
email.grid(row= 4, column = 2)
city.grid(row= 5, column = 2)
interest.grid(row= 6, column = 2)

namevalue = StringVar
gendervalue = StringVar
phonevalue = StringVar
emailvalue = StringVar
cityvalue = StringVar
interestvalue = StringVar
checkvalue = IntVar

nameentry = Entry(window, textvariable = namevalue)
genderentry = Entry(window, textvariable = gendervalue)
phoneentry = Entry(window, textvariable = phonevalue)
emailentry = Entry(window, textvariable = emailvalue)
cityentry = Entry(window, textvariable = cityvalue)
interestentry= Entry(window, textvariable = interestvalue)


nameentry.grid(row=1,column = 3 )
genderentry.grid(row=2,column = 3 )
phoneentry.grid(row=3,column = 3 )
emailentry.grid(row=4,column = 3 )
cityentry.grid(row=5,column = 3 )
interestentry.grid(row=6,column = 3 )

window.mainloop()




#greeting = Label(window, text ="Hello " + name)
#greeting.pack()
window.mainloop()
import random

##print("hie",chob)
#print(chob,"welcome to math game!")
#num1 = random.randint(1,100)
#num2 = random.randint(48,500)
#ans = int(input(f"what is , {num1} + {num2}? " ))
#stuff = num1 + num2
#if stuff != ans:
    #print(chob,"vele udull wena mfana!")
#elif stuff == ans:
    #print(chob, " that is the correct answer")

#print("welcome to calculator")
#a = int(input("enter your first number "))
#b = int(input("enter your second number "))

#def calc():
    #return int(a) * int(b)

#calc()

#print("hey welcome to age genie")
#name = input("what is your name ")
#brthyear = int(input("What year where you born? "))
#currentyr = 2026
#def calc():
    #ans = int(currentyr - brthyear)
    #print(f"{name} you are",ans, "years old. ")
#calc()
#for r in range(0,4):
#    print(r)
#a = input("what is your year? \n")
#print("you are",int(2026) - int(a), "years old")

#a = input("what is your year? \n")
#print("you are",str(2026 - int(a)), "years old")



