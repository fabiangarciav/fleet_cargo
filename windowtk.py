from tkinter import *
from tkinter import filedialog
from fleetApp import *

ws = Tk()
ws.title("Get the Best Route for Each Driver")
ws.geometry("900x600")
ws['bg']='#fb0'
win = Tk()
win.title("List of the Best Routes for Each Drivers")

def openFile():
    addresstxtfile = filedialog.askopenfilename(
        initialdir="C:/Users/MainFrame/Desktop/", 
        title="PLEASE SELECT A ADDRESS'S FILE", 
        filetypes=(("Text Files", "*.txt"),)
        )
    
    driverstxtfile = filedialog.askopenfilename(
        initialdir="C:/Users/MainFrame/Desktop/", 
        title="PLEASE SELECT A DRIVER'S FILE", 
        filetypes=(("Text Files", "*.txt"),)
        )

    arrOfAddress = openTextFiletoArray(addresstxtfile,'address')
    arrOfDrivers = openTextFiletoArray(driverstxtfile,'driver')
    arrIndexBySS = applySSFactorAlgorithm(arrOfDrivers,arrOfAddress)
    bestRoutes = getBestRoutes(arrIndexBySS)
    for row in range(len(bestRoutes)):
        txtarea.insert(END, '--'.join(bestRoutes[row]))

    pathh.insert(END, addresstxtfile)
    pathh2.insert(END, driverstxtfile)
    
    #win.geometry("700x350")
    for x in range(len(bestRoutes)):
        for y in range(3):
            gridarea = Text(win, width=40, height=2)
            gridarea.grid(row=x,column=y)
            gridarea.insert(END, bestRoutes[x][y])

def openGrid():
    win.attributes('-topmost',1)

txtarea = Text(ws, width=95, height=25)
txtarea.pack(pady=20)
Label(
    ws,
    text="Address File Path"
    ).place(x=30, y=450, height=25, width=120)
pathh = Entry(ws)
pathh.place(x=155, y=450, height=25, width=400)
Label(
    ws,
    text="Drivers File Path"
    ).place(x=30, y=500, height=25, width=120)
pathh2 = Entry(ws)
pathh2.place(x=155, y=500, height=25, width=400)

Button(
    ws, 
    text="CLICK TO OPEN A: Address's and Driver's Files", 
    command=openFile
    ).place(x=580, y=450, height=25, width=280)

Button(
    ws, 
    text="Open a Grid Viewer", 
    command=openGrid
    ).place(x=400, y=550, height=25, width=150)

ws.mainloop()