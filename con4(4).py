from tkinter import *


winred = [1, 1, 1, 1]
winyellow = [2, 2, 2, 2]
root = Tk()
color = "red"
turn ="red"
blackcir = PhotoImage(file="blackcir.gif")
redcir = PhotoImage(file="redcir.gif")
yellowcir = PhotoImage(file="yellowcir.gif")
lastplacedx = 0
lastplacedy = 0

def testhoriwinred():
    global winred
    for idx, r in enumerate(row1):
        if winred == row1[idx:idx+len(winred)]:
            print "found"
    for idx, r in enumerate(row2):
        if winred == row2[idx:idx+len(winred)]:
            print "found"
    for idx, r in enumerate(row3):
        if winred == row3[idx:idx+len(winred)]:
            print "found"
    for idx, r in enumerate(row4):
        if winred == row4[idx:idx+len(winred)]:
            print "found"
    for idx, r in enumerate(row5):
        if winred == row5[idx:idx+len(winred)]:
            print "found"
    for idx, r in enumerate(row6):
        if winred == row6[idx:idx+len(winred)]:
            print "found"
            
def testhoriwinyellow():
    global winyellow
    for idx, r in enumerate(row1):
        if winyellow == row1[idx:idx+len(winyellow)]:
            print "found"
    for idx, r in enumerate(row2):
        if winyellow == row2[idx:idx+len(winyellow)]:
            print "found"
    for idx, r in enumerate(row3):
        if winyellow == row3[idx:idx+len(winyellow)]:
            print "found"
    for idx, r in enumerate(row4):
        if winyellow == row4[idx:idx+len(winyellow)]:
            print "found"
    for idx, r in enumerate(row5):
        if winyellow == row5[idx:idx+len(winyellow)]:
            print "found"
    for idx, r in enumerate(row6):
        if winyellow == row6[idx:idx+len(winyellow)]:
            print "found"

#place a circle in column 1
def placecir1():
    global turn
    global lastplacedx
    global lastplacedy
    if row6[0] == 0:
        if turn == "red":
            cir61.configure(image=redcir)
            row6[0] = 1
            col1[5] = 1
        else:
            cir61.configure(image=yellowcir)
            row6[0] = 2
            col1[5] = 2
    elif row5[0] == 0:
            if turn == "red":
                cir51.configure(image=redcir)
                row5[0] = 1
                col1[4] = 1
            else:
                cir51.configure(image=yellowcir)
                row5[0] = 2
                col1[4] = 2
    elif row4[0] == 0:
            if turn == "red":
                cir41.configure(image=redcir)
                row4[0] = 1
                col1[3] = 1
            else:
                cir41.configure(image=yellowcir)
                row4[0] = 2
                col1[3] = 2
    elif row3[0] == 0:
            if turn == "red":
                cir31.configure(image=redcir)
                row3[0] = 1
                col1[2] = 1
            else:
                cir31.configure(image=yellowcir)
                row3[0] = 2
                col1[2] = 2
    elif row2[0] == 0:
            if turn == "red":
                cir21.configure(image=redcir)
                row2[0] = 1
                col1[1] = 1
            else:
                cir21.configure(image=yellowcir)
                row2[0] = 2
                col1[1] = 2
    elif row1[0] == 0:
            if turn == "red":
                cir11.configure(image=redcir)
                row1[0] = 1
                col1[0] = 1
            else:
                cir11.configure(image=yellowcir)
                row1[0] = 2
                col1[0] = 2
                
#place a circle in col 2
def placecir2():
    global turn
    global lastplacedx
    global lastplacedy
    if row6[1] == 0:
        if turn == "red":
            cir62.configure(image=redcir)
            row6[1] = 1
            col2[5] = 1
        else:
            cir62.configure(image=yellowcir)
            row6[1] = 2
            col2[5] = 2
    elif row5[1] == 0:
            if turn == "red":
                cir52.configure(image=redcir)
                row5[1] = 1
                col2[4] = 1
            else:
                cir52.configure(image=yellowcir)
                row5[1] = 2
                col2[4] = 2
    elif row4[1] == 0:
            if turn == "red":
                cir42.configure(image=redcir)
                row4[1] = 1
                col2[3] = 1
            else:
                cir42.configure(image=yellowcir)
                row4[1] = 2
                col2[3] = 2
    elif row3[1] == 0:
            if turn == "red":
                cir32.configure(image=redcir)
                row3[1] = 1
                col2[2] = 1
            else:
                cir32.configure(image=yellowcir)
                row3[1] = 2
                col2[2] = 2
    elif row2[1] == 0:
            if turn == "red":
                cir22.configure(image=redcir)
                row2[1] = 1
                col2[1] = 1
            else:
                cir22.configure(image=yellowcir)
                row2[1] = 2
                col2[1] = 2
    elif row1[1] == 0:
            if turn == "red":
                cir12.configure(image=redcir)
                row1[1] = 1
                col2[0] = 1
            else:
                cir12.configure(image=yellowcir)
                row1[1] = 2
                col2[0] = 2
                
#place a circle in col 3
def placecir3():
    global turn
    global lastplacedx
    global lastplacedy
    if row6[2] == 0:
        if turn == "red":
            cir63.configure(image=redcir)
            row6[2] = 1
            col3[5] = 1
        else:
            cir63.configure(image=yellowcir)
            row6[2] = 2
            col3[5] = 2
    elif row5[2] == 0:
            if turn == "red":
                cir53.configure(image=redcir)
                row5[2] = 1
                col3[4] = 1
            else:
                cir53.configure(image=yellowcir)
                row5[2] = 2
                col3[4] = 2
    elif row4[2] == 0:
            if turn == "red":
                cir43.configure(image=redcir)
                row4[2] = 1
                col3[3] = 1
            else:
                cir43.configure(image=yellowcir)
                row4[2] = 2
                col3[3] = 2
    elif row3[2] == 0:
            if turn == "red":
                cir33.configure(image=redcir)
                row3[2] = 1
                col3[2] = 1
            else:
                cir33.configure(image=yellowcir)
                row3[2] = 2
                col3[2] = 2
    elif row2[2] == 0:
            if turn == "red":
                cir23.configure(image=redcir)
                row2[2] = 1
                col3[1] = 1
            else:
                cir23.configure(image=yellowcir)
                row2[2] = 2
                col3[1] = 2
    elif row1[2] == 0:
            if turn == "red":
                cir13.configure(image=redcir)
                row1[2] = 1
                col3[0] = 1
            else:
                cir13.configure(image=yellowcir)
                row1[2] = 2
                col3[0] = 2
                
                
    
#place a circle in col 4
def placecir4():
    global turn
    global lastplacedx
    global lastplacedy
    if row6[3] == 0:
        if turn == "red":
            cir64.configure(image=redcir)
            row6[3] = 1
            col4[5] = 1
        else:
            cir64.configure(image=yellowcir)
            row6[3] = 2
            col4[5] = 2
    elif row5[3] == 0:
            if turn == "red":
                cir54.configure(image=redcir)
                row5[3] = 1
                col4[4] = 1
            else:
                cir54.configure(image=yellowcir)
                row5[3] = 2
                col4[4] = 2
    elif row4[3] == 0:
            if turn == "red":
                cir44.configure(image=redcir)
                row4[3] = 1
                col4[3] = 1
            else:
                cir44.configure(image=yellowcir)
                row4[3] = 2
                col4[3] = 2
    elif row3[3] == 0:
            if turn == "red":
                cir34.configure(image=redcir)
                col4[2] = 1
                row3[3] = 1
            else:
                cir34.configure(image=yellowcir)
                row3[3] = 2
                col4[2] = 2
    elif row2[3] == 0:
            if turn == "red":
                cir24.configure(image=redcir)
                row2[3] = 1
                col4[1] = 1
            else:
                cir24.configure(image=yellowcir)
                row2[3] = 2
                col4[1] = 2
    elif row1[3] == 0:
            if turn == "red":
                cir14.configure(image=redcir)
                row1[3] = 1
                col4[0] = 1
            else:
                cir14.configure(image=yellowcir)
                row1[3] = 2
                col4[0] = 2

#place a circle in col 5
def placecir5():
    global turn
    global lastplacedx
    global lastplacedy
    if row6[4] == 0:
        if turn == "red":
            cir65.configure(image=redcir)
            row6[4] = 1
            col5[5] = 1
        else:
            cir65.configure(image=yellowcir)
            row6[4] = 2
            col5[5] = 2
    elif row5[4] == 0:
            if turn == "red":
                cir55.configure(image=redcir)
                row5[4] = 1
                col5[4] = 1
            else:
                cir55.configure(image=yellowcir)
                row5[4] = 2
                col5[4] = 2
    elif row4[4] == 0:
            if turn == "red":
                cir45.configure(image=redcir)
                row4[4] = 1
                col5[3] = 1
            else:
                cir45.configure(image=yellowcir)
                row4[4] = 2
                col5[3] = 2
    elif row3[4] == 0:
            if turn == "red":
                cir35.configure(image=redcir)
                row3[4] = 1
                col5[2] = 1
            else:
                cir35.configure(image=yellowcir)
                row3[4] = 2
                col5[2] = 2
    elif row2[4] == 0:
            if turn == "red":
                cir25.configure(image=redcir)
                row2[4] = 1
                col5[1] = 1
            else:
                cir25.configure(image=yellowcir)
                row2[4] = 2
                col5[1] = 2
    elif row1[4] == 0:
            if turn == "red":
                cir15.configure(image=redcir)
                row1[4] = 1
                col5[0] = 1
            else:
                cir15.configure(image=yellowcir)
                row1[4] = 2
                col5[0] = 2

#place a circle in col 6
def placecir6():
    global turn
    global lastplacedx
    global lastplacedy
    if row6[5] == 0:
        if turn == "red":
            cir66.configure(image=redcir)
            row6[5] = 1
            col6[5] = 1
        else:
            cir66.configure(image=yellowcir)
            row6[5] = 2
            col6[5] = 2
    elif row5[5] == 0:
            if turn == "red":
                cir56.configure(image=redcir)
                row5[5] = 1
                col6[4] = 1
            else:
                cir56.configure(image=yellowcir)
                row5[5] = 2
                col6[4] = 2
    elif row4[5] == 0:
            if turn == "red":
                cir46.configure(image=redcir)
                row4[5] = 1
                col6[3] = 1
            else:
                cir46.configure(image=yellowcir)
                row4[5] = 2
                col6[3] = 2
    elif row3[5] == 0:
            if turn == "red":
                cir36.configure(image=redcir)
                row3[5] = 1
                col6[2] = 1
            else:
                cir36.configure(image=yellowcir)
                row3[5] = 2
                col6[2] = 2
    elif row2[5] == 0:
            if turn == "red":
                cir26.configure(image=redcir)
                row2[5] = 1
                col6[1] = 1
            else:
                cir26.configure(image=yellowcir)
                row2[5] = 2
                col6[1] = 2
    elif row1[5] == 0:
            if turn == "red":
                cir16.configure(image=redcir)
                row1[5] = 1
                col6[0] = 1
            else:
                cir16.configure(image=yellowcir)
                row1[5] =  2
                col6[0] = 2

#place a circle in col 7
def placecir7():
    global turn
    global lastplacedx
    global lastplacedy
    if row6[6] == 0:
        if turn == "red":
            cir67.configure(image=redcir)
            row6[6] = 1
            col7[5] = 1
        else:
            cir67.configure(image=yellowcir)
            row6[6] = 2
            col7[5] = 2
    elif row5[6] == 0:
            if turn == "red":
                cir57.configure(image=redcir)
                row5[6] = 1
                col7[4] = 1
            else:
                cir57.configure(image=yellowcir)
                row5[6] = 2
                col7[4] = 2
    elif row4[6] == 0:
            if turn == "red":
                cir47.configure(image=redcir)
                row4[6] = 1
                col7[3] = 1
            else:
                cir47.configure(image=yellowcir)
                row4[6] = 2
                col7[3] = 2
    elif row3[6] == 0:
            if turn == "red":
                cir37.configure(image=redcir)
                row3[6] = 1
                col7[2] = 1
            else:
                cir37.configure(image=yellowcir)
                row3[6] = 2
                col7[2] = 2
    elif row2[6] == 0:
            if turn == "red":
                cir27.configure(image=redcir)
                row2[6] = 1
                col7[1] = 1
            else:
                cir27.configure(image=yellowcir)
                row2[6] = 2
                col7[1] = 2
    elif row1[6] == 0:
            if turn == "red":
                cir17.configure(image=redcir)
                row1[6] = 1
                col7[0] = 1
            else:
                cir17.configure(image=yellowcir)
                row1[6] = 2
                col7[0] = 2
                

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
    else:
        button1["bg"] = "red"
        button2["bg"] = "red"
        button3["bg"] = "red"
        button4["bg"] = "red"
        button5["bg"] = "red"
        button6["bg"] = "red"
        button7["bg"] = "red"


#what each button does

#!!!
def button1com():
    global turn
    global lastplacedx
    button()
    lastplacedx = 1
    placecir1()
    testhoriwinred()
    testhoriwinyellow()
    if turn == "red":
        turn = "yellow"
    else:
        turn = "red"
    
def button2com():
    global turn
    global lastplacedx
    button()
    lastplacedx = 1
    placecir2()
    testhoriwinred()
    testhoriwinyellow()
    if turn == "red":
        turn = "yellow"
    else:
        turn = "red"
    
def button3com():
    global turn
    global lastplacedx
    button()
    lastplacedx = 2
    placecir3()
    testhoriwinred()
    testhoriwinyellow()
    if turn == "red":
        turn = "yellow"
    else:
        turn = "red"
      

def button4com():
    global turn
    global lastplacedx
    button()
    lastplacedx = 3
    placecir4()
    testhoriwinred()
    testhoriwinyellow()
    if turn == "red":
        turn = "yellow"
    else:
        turn = "red"

def button5com():
    global turn
    global lastplacedx
    button()
    lastplacedx = 4
    placecir5()
    testhoriwinred()
    testhoriwinyellow()
    if turn == "red":
        turn = "yellow"
    else:
        turn = "red"
        
def button6com():
    global turn
    global lastplacedx
    button()
    lastplacedx = 5
    placecir6()
    testhoriwinred()
    testhoriwinyellow()
    if turn == "red":
        turn = "yellow"
    else:
        turn = "red"
           
def button7com():
    global turn
    global lastplacedx
    button()
    lastplacedx = 6
    placecir7()
    testhoriwinred()
    testhoriwinyellow()
    if turn == "red":
        turn = "yellow"
    else:
        turn = "red"
              
    
#creates widgets (buttons and circles
button1 = Button(None, text = "Drop here", bg = color, command = button1com)
button2 = Button(None, text = "drop here", bg = color, command = button2com)
button3 = Button(None, text = "drop here", bg = color, command = button3com)
button4 = Button(None, text = "drop here", bg = color, command = button4com)
button5 = Button(None, text = "drop here", bg = color, command = button5com)
button6 = Button(None, text = "drop here", bg = color, command = button6com)
button7 = Button(None, text = "drop here", bg = color, command = button7com)
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
text = Label(text = "connect 4!")

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
text.grid(row = 7, column = 3)
#this stores the data of each row. 0 is unused, 1 is red, 2 is yellow.
row1 = [0,0,0,0,0,0,0]
row2 = [0,0,0,0,0,0,0]
row3 = [0,0,0,0,0,0,0]
row4 = [0,0,0,0,0,0,0]
row5 = [0,0,0,0,0,0,0]
row6 = [0,0,0,0,0,0,0]
col1 = [0,0,0,0,0,0,0]
col2 = [0,0,0,0,0,0,0]
col3 = [0,0,0,0,0,0,0]
col4 = [0,0,0,0,0,0,0]
col5 = [0,0,0,0,0,0,0]
col6 = [0,0,0,0,0,0,0]
col7 = [0,0,0,0,0,0,0]

#lastplacedx is how far into the row the last was placed
#lastplacedy is which row the circle fell to
#is row6[lastplacedx] > 0? if not, check row5[lastplacedx], ect.

root.mainloop()