from tkinter import *

PlayerX = 100
PlayerY = 100


Defenders = []

defender1 = (20,20)
defender2 = (30,20)
defender3 = (40,20)

Defenders.append(defender1)
Defenders.append(defender2)
Defenders.append(defender3)

def onKeyPressed(e):
    # not sure why I need global here
    global rightDirection
    global leftDirection
    global upDirection
    global downDirection

    key = e.keysym
    if key == "Right" and not rightDirection:
        leftDirection = False
        rightDirection = True
        upDirection = False
        downDirection = False

    if key == "Left" and not leftDirection:
        leftDirection = True
        rightDirection = False
        upDirection = False
        downDirection = False

    if key == "Up" and not upDirection:
        leftDirection = False
        rightDirection = False
        upDirection = True
        downDirection = False

    if key == "Down" and not downDirection:
        leftDirection = False
        rightDirection = False
        upDirection = False
        downDirection = True


def gameLoop():
    global PlayerX
    global PlayerY
    global Defenders
    canvas1.delete(ALL)
    # redraw of the field
    canvas1.create_rectangle(0, 0, 8000, 600, fill='dark green')
    line1 = canvas1.create_line(160, 0, 160, 600, fill='white')
    line2 = canvas1.create_line(160, 0, 160, 600, fill='white')

    canvas1.create_rectangle(PlayerX,PlayerY,PlayerX+10,PlayerY+10, fill = 'black')

    for d in Defenders:
        canvas1.create_rectangle(d[0], d[1], d[0] + 10, d[1] + 10, fill='red')

    #go thhrough the defenderlist and make a random move for each defender

    listenID = root.after(100, gameLoop)



root = Tk()
root.title("Test program")
root.configure(background = 'sky blue')

frame1 = Frame(root, bg='sky blue', bd= 10)
frame1.pack(side=TOP)

canvas1 = Canvas(frame1, width = 800, height=600)
canvas1.pack()

listenID = root.after(10, gameLoop)

mainloop()