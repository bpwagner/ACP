from tkinter import *
import pyowm
import time

root = Tk()
root.title("Mr. Wagner's Cool Weather App")
degrees = "°"
v = IntVar()
v.set(1)

LocationStr = StringVar()
LocationStr.set("Louisville")

owm = pyowm.OWM('978910f354606707ef717cdf3b483575')
observation = owm.weather_at_place(LocationStr.get())
w = observation.get_weather()
temp_dict = w.get_temperature('fahrenheit')

def UpdateTemp():
    if v.get() == 0:
        LabelTemp['text'] =  w.get_temperature('celsius')['temp']
    elif v.get() ==1:
        LabelTemp['text'] = w.get_temperature('fahrenheit')['temp']
    else:
        LabelTemp["text"] = w.get_temperature('kelvin')['temp']

def UpdateTime():
    LabelTime['text']= time.strftime("%-I:%M:%S %p")
    listenID = root.after(1000, UpdateTime) #Call UpdateTime after a second

def UpdateWeather():
    s = LocationStr.get()
    observation = owm.weather_at_place(LocationStr.get())
    w = observation.get_weather()
    v=1
    temp_dict = w.get_temperature('fahrenheit')
    LabelTemp['text'] = w.get_temperature('fahrenheit')['temp']
    LabelLoc['text'] = observation.get_location().get_name()
    print("Weather updated")

frame1 = Frame(root, bd=10)
frame1.pack()

frame2 = Frame(root, bd=10)
frame2.pack()

frame2l = Frame(frame2)
frame2l.pack(side=LEFT)

frame2r = Frame(frame2)
frame2r.pack(side=RIGHT)

frame3 = Frame(root, bd=10)
frame3.pack()

LabelTime = Label(frame1, text=time.strftime( "%-I:%M:%S %p"), bg="red", fg="white")
LabelTime.pack(side=LEFT)
LabelLoc = Label(frame1, text="Louisville", bg="white", fg="red")
LabelLoc.pack(side=RIGHT)
b = Button(frame1, text="Refresh", command=UpdateWeather)
b.pack(side=RIGHT)
e = Entry(frame1, textvariable=LocationStr)
e.pack()

LabelTemp = Label(frame2l, font=("Courier", 44), text=str(temp_dict['temp']) + degrees, bg="white", fg="blue", bd=10)
LabelTemp.pack()
LabelChill = Label(frame2r, text="feels like 72" + degrees, bg="white", fg="blue")
LabelChill.pack()

windCanvas = Canvas(frame2r, width=100, height=100)
windCanvas.create_oval(10, 10, 90, 90, outline="red", fill="white", width=2)
windCanvas.pack()

RC = Radiobutton(frame2l, text="C", padx=0, variable=v, value=0, command = UpdateTemp)
RC.pack(side=LEFT)
RF = Radiobutton(frame2l, text="F", padx=0, variable=v, value=1, command = UpdateTemp)
RF.pack(side=LEFT)
RK = Radiobutton(frame2l, text="K", padx=0, variable=v, value=2, command = UpdateTemp)
RK.pack(side=LEFT)


LabelPress = Label(frame3, text="pressure rising", bg="blue", fg="white")
LabelPress.pack()

listenID = root.after(1000, UpdateTime) #call UpdateTime after a second

mainloop()




