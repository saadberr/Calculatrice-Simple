from tkinter import *
import tkinter.font as font


# Calculator window
calculator = Tk()
calculator.geometry("400x400")
calculator.title("SaadCalculator")
calculator.iconbitmap("icone.ico")
calculator.configure(bg='skyblue')
calculator.resizable(False, False)

# Buttons actions
def actionzero():
	screen.insert(len(str(screen.get())), 0)
def actionone():
	screen.insert(len(str(screen.get())), 1)
def actiontwo():
	screen.insert(len(str(screen.get())), 2)
def actionthree():
	screen.insert(len(str(screen.get())), 3)
def actionfour():
	screen.insert(len(str(screen.get())), 4)
def actionfive():
	screen.insert(len(str(screen.get())), 5)
def actionsix():
	screen.insert(len(str(screen.get())), 6)
def actionseven():
	screen.insert(len(str(screen.get())), 7)
def actioneight():
	screen.insert(len(str(screen.get())), 8)
def actionnine():
	screen.insert(len(str(screen.get())), 9)
def actionplus():
	screen.insert(len(str(screen.get())), "+")
def actionminus():
	screen.insert(len(str(screen.get())), "-")
def actionmult():
	screen.insert(len(str(screen.get())), "*")
def actiondiv():
	screen.insert(len(str(screen.get())), "/")
def actionleft():
	screen.insert(len(str(screen.get())), "(")
def actionright():
	screen.insert(len(str(screen.get())), ")")
def actionclear():
	screen.delete(0, END)
def actionequal():
	resultat = screen.get()
	###
	resultat = str(resultat)
	resultat = resultat.replace("^","**")
	###
	result = eval(resultat)
	screen.delete(0, END)
	screen.insert(0, result)
def actionpoint():
	screen.insert(len(str(screen.get())), ".")
def actiondelete():
	screen.delete(len(str(screen.get()))-1, END)
def actionpower():
	screen.insert(len(str(screen.get())), "^")

# Font
myFont = font.Font(size=15)
scFont = font.Font(size = 10)


# Buttons
one = Button(calculator , text = "1" , bg="blue" , fg="white", command = actionone)
one.place(x=50, y=150, height=40,width=40)
two = Button(calculator , text = "2" , bg="blue" , fg="white", command = actiontwo)
two.place(x=100, y=150, height=40,width=40)
three = Button(calculator , text = "3" , bg="blue" , fg="white", command = actionthree)
three.place(x=150, y=150, height=40,width=40)
four = Button(calculator , text = "4" , bg="blue" , fg="white", command = actionfour)
four.place(x=50, y=200, height=40,width=40)
five = Button(calculator , text = "5" , bg="blue" , fg="white", command = actionfive)
five.place(x=100, y=200, height=40,width=40)
six = Button(calculator , text = "6" , bg="blue" , fg="white", command = actionsix)
six.place(x=150, y=200, height=40,width=40)
seven = Button(calculator , text = "7" , bg="blue" , fg="white", command = actionseven)
seven.place(x=50, y=250, height=40,width=40)
eight = Button(calculator , text = "8" , bg="blue" , fg="white", command = actioneight)
eight.place(x=100, y=250, height=40,width=40)
nine = Button(calculator , text = "9" , bg="blue" , fg="white", command = actionnine)
nine.place(x=150, y=250, height=40,width=40)
zero = Button(calculator , text = "0" , bg="blue" , fg="white", command = actionzero)
zero.place(x=50, y=300, height=50,width=140)
#######################
plus = Button(calculator , text = "+" , bg="white" , fg="blue", command = actionplus)
plus.place(x=200, y=150, height=40,width=40)
plus['font'] = myFont
minus = Button(calculator , text = "-" , bg="white" , fg="blue", command = actionminus)
minus.place(x=250, y=150, height=40,width=40)
minus['font'] = myFont
mult = Button(calculator , text = "×" , bg="white" , fg="blue", command = actionmult)
mult.place(x=200, y=200, height=40,width=40)
mult['font'] = myFont
div = Button(calculator , text = "/" , bg="white" , fg="blue", command = actiondiv)
div.place(x=250, y=200, height=40,width=40)
div['font'] = myFont
power = Button(calculator , text = "^" , bg="white" , fg="blue", command = actionpower)
power.place(x=300, y=250, height=40,width=40)
power['font'] = myFont
equal = Button(calculator , text = "=" , bg="white" , fg="blue", command = actionequal)
equal.place(x=200, y=300, height=50,width=90)
equal['font'] = myFont
#########################
left = Button(calculator , text = "(" , bg="white" , fg="blue", command = actionleft)
left.place(x=200, y=250, height=40,width=40)
left['font'] = myFont
right = Button(calculator , text = ")" , bg="white" , fg="blue", command = actionright)
right.place(x=250, y=250, height=40,width=40)
right['font'] = myFont
##########################
clear = Button(calculator , text = "C" , bg="white" , fg="blue", command = actionclear)
clear.place(x=300, y=150, height=40,width=40)
clear['font'] = myFont
delete = Button(calculator , text = "←" , bg="white" , fg="blue", command = actiondelete)
delete.place(x=300, y=200, height=40,width=40)
delete['font'] = myFont
#########################
point = Button(calculator , text = "." , bg="white" , fg="blue", command = actionpoint)
point.place(x=300, y=300, height=50,width=40)
point['font'] = myFont
#########################
screen = Entry(calculator , width = 41)
screen.place(height = 30, x = 50 , y = 80)
screen.bind("<Key>", lambda e: "break")
screen['font'] = scFont
#########################



calculator.mainloop()
