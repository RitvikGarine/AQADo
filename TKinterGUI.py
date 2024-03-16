from tkinter import *
from tkinter import ttk

def name_entry():  # Create a function to take in the names inputted in the entry box
    global name1, name2, input2, input1
    name1 = input1.get()
    name2 = input2.get()
    entrywindow.destroy()

def entryGUI():  # Create the GUI to take in the user's file name
    global name1, name2, input2, input1

    # Create a window
    global entrywindow
    entrywindow = Tk()
    entrywindow.title('AQADo Game')
    entrywindow.geometry("300x200")

    # Create a heading
    title = Label(entrywindow, text="Please enter the Player Names:", font=("Helvetica", 13))
    title.place(x=45, y=30)
    text1 = Label(entrywindow, text="Player 1:", font=("Helvetica", 13))
    text1.place(x=35, y=70)
    text2 = Label(entrywindow, text="Player 2:", font=("Helvetica", 13))
    text2.place(x=35, y=100)

    # Create an entry box
    input1 = ttk.Entry(entrywindow, font=('Helvetica', 13), width=20)
    input1.place(x=100, y=70)
    input2 = ttk.Entry(entrywindow, font=('Helvetica', 13), width=20)
    input2.place(x=100, y=100)

    # Create a button to submit the data
    ttk.Button(entrywindow, text="Submit", command=name_entry).place(x=100, y=145)

    entrywindow.mainloop()  # Run the TKinter functions

    return name1, name2  # Return the users name input

def ip_entry():  # Create a function to take in the IP Address inputted in the entry box
    global ip_address, ipInput
    ip_address = ipInput.get()
    entrywindow.destroy()

def IPInput():
    global entrywindow, ip_address, ipInput

    # Create a window
    entrywindow = Tk()
    entrywindow.title('AQADo Game')
    entrywindow.geometry("300x200")

    # Create a heading
    title = Label(entrywindow, text="Please enter the IP:", font=("Helvetica", 13))
    title.place(x=80, y=30)
    text1 = Label(entrywindow, text="IP:", font=("Helvetica", 13))
    text1.place(x=50, y=70)

    # Create an entry box
    ipInput = ttk.Entry(entrywindow, font=('Helvetica', 13), width=20)
    ipInput.place(x=80, y=70)

    # Create a button to submit the data
    ttk.Button(entrywindow, text="Submit", command=ip_entry).place(x=100, y=115)

    # Run the TKinter functions
    entrywindow.mainloop()

    return ip_address  # Return the users IP input
