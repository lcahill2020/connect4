from tkinter import *



root = Tk()
color = "red"
turn ="red"
blackcir = PhotoImage(file="blackcir.gif")
redcir = PhotoImage(file="redcir.gif")
yellowcir = PhotoImage(file="yellowcir.gif")
lastplacedx = 0
lastplacedy = 0

def placecir1():
    print "hi"

#when a button is pressed, changes the turn and the color of the buttons    
def button():
    global color
    global turn
    if turn == "red":
        button1["bg"] = "yellow"
        button2["bg"] = "yellow"
        button3["bg"] = "yellow"
        button4["bg"] = "yellow"
        button5["bg"] = "yellow"
        button6["bg"] = "yellow"
        button7["bg"] = "yellow"
        turn = "yellow"
    else:
        button1["bg"] = "red"
        button2["bg"] = "red"
        button3["bg"] = "red"
        button4["bg"] = "red"
        button5["bg"] = "red"
        button6["bg"] = "red"
        button7["bg"] = "red"
        turn = "red"


#what each button does

#!!!
def button1com():
    placecir1()
    
def button2com():
    global turn
    global lastplacedx
    button()
    lastplacedx = 1
    
def button3com():
    global turn
    global lastplacedx
    button()
    lastplacedx = 2
    

def button4com():
    global turn
    global lastplacedx
    button()
    lastplacedx = 3

def button5com():
    global turn
    global lastplacedx
    button()
    lastplacedx = 4

def button6com():
    global turn
    global lastplacedx
    button()
    lastplacedx = 5
    
def button1com():
    global turn
    global lastplacedx
    button()
    lastplacedx = 6
    
    
#creates widgets (buttons and circles
button1 = Button(None, text = "Drop here", bg = color, command = button1com)
button2 = Button(None, text = "drop here", bg = color, command = button2com)
button3 = Button(None, text = "drop here", bg = color, command = button2com)
button4 = Button(None, text = "drop here", bg = color, command = button2com)
button5 = Button(None, text = "drop here", bg = color, command = button2com)
button6 = Button(None, text = "drop here", bg = color, command = button2com)
button7 = Button(None, text = "drop here", bg = color, command = button2com)
cir11 = Label(root, image = blackcir)
cir12 = Label(root, image = blackcir)
cir13 = Label(root, image = blackcir)
cir14 = Label(root, image = blackcir)
cir15 = Label(root, image = blackcir)
cir16 = Label(root, image = blackcir)
cir17 = Label(root, image = blackcir)
cir21 = Label(root, image = blackcir)
cir22 = Label(root, image = blackcir)
cir23 = Label(root, image = blackcir)
cir24 = Label(root, image = blackcir)
cir25 = Label(root, image = blackcir)
cir26 = Label(root, image = blackcir)
cir27 = Label(root, image = blackcir)
cir31 = Label(root, image = blackcir)
cir32 = Label(root, image = blackcir)
cir33 = Label(root, image = blackcir)
cir34 = Label(root, image = blackcir)
cir35 = Label(root, image = blackcir)
cir36 = Label(root, image = blackcir)
cir37 = Label(root, image = blackcir)
cir41 = Label(root, image = blackcir)
cir42 = Label(root, image = blackcir)
cir43 = Label(root, image = blackcir)
cir44 = Label(root, image = blackcir)
cir45 = Label(root, image = blackcir)
cir46 = Label(root, image = blackcir)
cir47 = Label(root, image = blackcir)
cir51 = Label(root, image = blackcir)
cir52 = Label(root, image = blackcir)
cir53 = Label(root, image = blackcir)
cir54 = Label(root, image = blackcir)
cir55 = Label(root, image = blackcir)
cir56 = Label(root, image = blackcir)
cir57 = Label(root, image = blackcir)
cir61 = Label(root, image = blackcir)
cir62 = Label(root, image = blackcir)
cir63 = Label(root, image = blackcir)
cir64 = Label(root, image = blackcir)
cir65 = Label(root, image = blackcir)
cir66 = Label(root, image = blackcir)
cir67 = Label(root, image = blackcir)

#places widgets
button1.grid(row = 0, column = 0)
button2.grid(row = 0, column = 1)
button3.grid(row = 0, column = 2)
button4.grid(row = 0, column = 3)
button5.grid(row = 0, column = 4)
button6.grid(row = 0, column = 5)
button7.grid(row = 0, column = 6)
cir11.grid(row = 1, column = 0)
cir12.grid(row = 1, column = 1)
cir13.grid(row = 1, column = 2)
cir14.grid(row = 1, column = 3)
cir15.grid(row = 1, column = 4)
cir16.grid(row = 1, column = 5)
cir17.grid(row = 1, column = 6)
cir21.grid(row = 2, column = 0)
cir22.grid(row = 2, column = 1)
cir23.grid(row = 2, column = 2)
cir24.grid(row = 2, column = 3)
cir25.grid(row = 2, column = 4)
cir26.grid(row = 2, column = 5)
cir27.grid(row = 2, column = 6)
cir31.grid(row = 3, column = 0)
cir32.grid(row = 3, column = 1)
cir33.grid(row = 3, column = 2)
cir34.grid(row = 3, column = 3)
cir35.grid(row = 3, column = 4)
cir36.grid(row = 3, column = 5)
cir37.grid(row = 3, column = 6)
cir41.grid(row = 4, column = 0)
cir42.grid(row = 4, column = 1)
cir43.grid(row = 4, column = 2)
cir44.grid(row = 4, column = 3)
cir45.grid(row = 4, column = 4)
cir46.grid(row = 4, column = 5)
cir47.grid(row = 4, column = 6)
cir51.grid(row = 5, column = 0)
cir52.grid(row = 5, column = 1)
cir53.grid(row = 5, column = 2)
cir54.grid(row = 5, column = 3)
cir55.grid(row = 5, column = 4)
cir56.grid(row = 5, column = 5)
cir57.grid(row = 5, column = 6)
cir61.grid(row = 6, column = 0)
cir62.grid(row = 6, column = 1)
cir63.grid(row = 6, column = 2)
cir64.grid(row = 6, column = 3)
cir65.grid(row = 6, column = 4)
cir66.grid(row = 6, column = 5)
cir67.grid(row = 6, column = 6)
#this stores the data of each row. 0 is unused, 1 is red, 2 is yellow.
row1 = [0,0,0,0,0,0,0]
row2 = [0,0,0,0,0,0,0]
row3 = [0,0,0,0,0,0,0]
row4 = [0,0,0,0,0,0,0]
row5 = [0,0,0,0,0,0,0]
row6 = [0,0,0,0,0,0,0]

#lastplacedx is how far into the row the last was placed
#lastplacedy is which row the circle fell to
#is row6[lastplacedx] > 0? if not, check row5[lastplacedx], ect.

root.mainloop()