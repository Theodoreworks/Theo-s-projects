from tkinter import *
import math

window = Tk()
window.title("Theo Calculator")
window.geometry("300x350")

expression = ""
equation = StringVar()

# Display
Entry(window, textvariable=equation, font=("Arial",20), bd=5, relief="ridge", justify="right").grid(row=0,column=0,columnspan=4, ipadx=8, ipady=8)

# Button functions
def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

def clear():
    global expression
    expression = ""
    equation.set("")

def equal():
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        equation.set("error")
        expression = ""

# Trigonometry
def sin_func():
    try:
        value = float(equation.get())
        equation.set(math.sin(math.radians(value)))
    except:
        equation.set("error")

def cos_func():
    try:
        value = float(equation.get())
        equation.set(math.cos(math.radians(value)))
    except:
        equation.set("error")

def tan_func():
    try:
        value = float(equation.get())
        equation.set(math.tan(math.radians(value)))
    except:
        equation.set("error")

# First row
Button(window,text="sin",width=6,height=2,command=sin_func).grid(row=1,column=0)
Button(window,text="cos",width=6,height=2,command=cos_func).grid(row=1,column=1)
Button(window,text="tan",width=6,height=2,command=tan_func).grid(row=1,column=2)
Button(window,text="C",width=6,height=2,command=clear).grid(row=1,column=3)

# Numbers and operators
Button(window,text="7",width=6,height=2,command=lambda:press(7)).grid(row=2,column=0)
Button(window,text="8",width=6,height=2,command=lambda:press(8)).grid(row=2,column=1)
Button(window,text="9",width=6,height=2,command=lambda:press(9)).grid(row=2,column=2)
Button(window,text="×",width=6,height=2,command=lambda:press("*")).grid(row=2,column=3)

Button(window,text="4",width=6,height=2,command=lambda:press(4)).grid(row=3,column=0)
Button(window,text="5",width=6,height=2,command=lambda:press(5)).grid(row=3,column=1)
Button(window,text="6",width=6,height=2,command=lambda:press(6)).grid(row=3,column=2)
Button(window,text="-",width=6,height=2,command=lambda:press("-")).grid(row=3,column=3)

Button(window,text="1",width=6,height=2,command=lambda:press(1)).grid(row=4,column=0)
Button(window,text="2",width=6,height=2,command=lambda:press(2)).grid(row=4,column=1)
Button(window,text="3",width=6,height=2,command=lambda:press(3)).grid(row=4,column=2)
Button(window,text="+",width=6,height=2,command=lambda:press("+")).grid(row=4,column=3)

Button(window,text="0",width=6,height=2,command=lambda:press(0)).grid(row=5,column=0)
Button(window,text=".",width=6,height=2,command=lambda:press(".")).grid(row=5,column=1)
Button(window,text="=",width=14,height=2,command=equal).grid(row=5,column=2,columnspan=2)

window.mainloop()
