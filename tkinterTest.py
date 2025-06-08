from tkinter import *

x = 100
y = 100


def gameLoop():
    global x
    global y
    canvas1.delete(ALL)
    canvas1.create_rectangle(x,y,x+50,y+50, fill = 'black')
    x+=1
    y+=1

    listenID = root.after(10, gameLoop)



root = Tk()
root.title("Test program")
root.configure(background = 'sky blue')

frame1 = Frame(root, bg='sky blue', bd= 10)
frame1.pack(side=TOP)

canvas1 = Canvas(frame1, width = 800, height=600)
canvas1.pack()

listenID = root.after(10, gameLoop)

mainloop()