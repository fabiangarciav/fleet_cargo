from tkinter import *
from tkinter import filedialog
from fleetApp import *

#Initialize the UI enviroment and set the visual elements
ws = Tk()
ws.title("Get the Best Route for Each Driver")
ws.geometry("900x600")
ws['bg']='#fb0'
win = Tk()
win.title("List of the Best Routes for Each Drivers")
txtarea = Text(ws, width=95, height=25)
txtarea.pack(pady=20)

# Function to open dialog for get the information of the two txt files 
def openFile():
    # Open dialogo box to select Address file
    addresstxtfile = filedialog.askopenfilename(
        initialdir="C:/Users/MainFrame/Desktop/", 
        title="PLEASE SELECT A ADDRESS'S FILE", 
        filetypes=(("Text Files", "*.txt"),)
        )
    
    # Open dialogo box to select Driver's file
    driverstxtfile = filedialog.askopenfilename(
        initialdir="C:/Users/MainFrame/Desktop/", 
        title="PLEASE SELECT A DRIVER'S FILE", 
        filetypes=(("Text Files", "*.txt"),)
        )

    # Invoke the fuctions how open the file and return an array
    arrOfAddress = openTextFiletoArray(addresstxtfile,'address')
    arrOfDrivers = openTextFiletoArray(driverstxtfile,'driver')
    # Run the algorithm to find the best rated routes
    arrIndexBySS = applySSFactorAlgorithm(arrOfDrivers,arrOfAddress)
    bestRoutes = getBestRoutes(arrIndexBySS)

    #Insert the results into window text area
    for row in range(len(bestRoutes)):
        txtrow = 'SS FACTOR: ' + bestRoutes[row][0] + '\n -- DRIVER: ' + bestRoutes[row][1] + '\n -- DELIVERY ADDRESS: ' + bestRoutes[row][2] + '\n'
        txtarea.insert(END, txtrow)

    # Show in the Window the path and file name of two txt source information
    pathh.insert(END, addresstxtfile)
    pathh2.insert(END, driverstxtfile)
    
    # Fill the window grid with the results of best routes
    for x in range(len(bestRoutes)):
        for y in range(3):
            gridarea = Text(win, width=40, height=2)
            gridarea.grid(row=x,column=y)
            gridarea.insert(END, bestRoutes[x][y])

#Set at the top the grid window
def openGrid():
    win.attributes('-topmost',1)

# Destroy windows for exit
def exitWindows():
    win.destroy()
    ws.destroy()

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
    text="Open a Grid Viewer Mode the Routes", 
    command = openGrid
    ).place(x=580, y=500, height=25, width=280)

Button(
    ws,
    text="Save the Results into a Txt File",
    ).place(x=650, y=550, height=25, width=150)

Button(
    ws,
    text="EXIT",
    command = exitWindows
    ).place(x=650, y=550, height=25, width=150)

ws.mainloop()