import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from addStudent import addStudent
from addProfessor import addProfessor



def open_Adminwin(root, admin):
    adminWin = Tk()

    # For showing result of search
    stextfield = ScrolledText(adminWin, wrap=tk.WORD, width=50, height=13, font=("Times New Roman", 10))
    stextfield.place(x=30, y=120)

    # this is the function called when the button is clicked
    def profWindow():
        adminWin.withdraw()
        addProfessor(adminWin,admin)

    def sudentWindow():
        adminWin.withdraw()
        addStudent(adminWin,admin)

    # this is the function called when the button is clicked
    def searchUser(temp):

        name = str(tInput.get())
        if (not str(tInput.get()).isalpha()):
            messagebox.showinfo(message="No numbers or characters allowed!")
            return
        stextfield.delete(1.0,END)
        if (temp == 1):
            for x in admin.stud:
                if (x.getName().lower() == name.lower()):
                    stextfield.insert(END, x.toString() + "\n")
        elif (temp == 2):
            for x in admin.prof:
                if (x.getName().lower() == name.lower()):
                    stextfield.insert(END, x.toString() + "\n")
        else:
            messagebox.showinfo(message="Make a User selection!")

    # this is a function to get the user input from the text input box
    def getInputBoxValue():
        userInput = tInput.get()
        return userInput

    # this is the function called when the button is clicked
    def btnClickFunction():
        print('clicked')

    # This is the section of code which creates the main window
    adminWin.geometry('500x350+50+100')
    adminWin.configure(background='#FFEFDB')
    adminWin.title('Admin')

    # This is the section of code which creates a button
    Button(adminWin, text='Add Student ', bg='#F0F8FF', font=('helvetica', 12, 'normal'),
           command=sudentWindow).place(
        x=373, y=34)

    # This is the section of code which creates a button
    Button(adminWin, text='Add Professor', bg='#F0F8FF', font=('helvetica', 12, 'normal'),
           command=profWindow).place(
        x=373, y=92)

    # This is the section of code which creates a text input box
    tInput = Entry(adminWin, font=('helvetica', 12, 'normal'))
    tInput.place(x=39, y=38)

    var = IntVar()
    def sel(mvar):
        selection = "You selected the option " + str(mvar)
        var.set(mvar)
        print(selection)

    # variable for radio button

    # group of radio buttons
    R1 = Radiobutton(adminWin, text="Student", variable=var, value=1,
                     command=lambda :sel(1))
    R1.pack(anchor=W)

    R2 = Radiobutton(adminWin, text="Professor", variable=var, value=2,
                     command=lambda :sel(2))
    R2.pack(anchor=W)

    R1.place(x=120, y=80)
    R2.place(x=190, y=80)
    # This is the section of code which creates the a label
    Label(adminWin, text='User : ', bg='#FFEFDB', font=('helvetica', 12, 'normal')).place(x=80, y=80)

    Button(adminWin, text='Search', bg='#F0F8FF', font=('helvetica', 12, 'normal'),
           command=lambda: searchUser(var.get())).place(
        x=191,
        y=35)

    # this defines the operation on closing
    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            adminWin.destroy()
            root.deiconify()

    adminWin.protocol("WM_DELETE_WINDOW", on_closing)

    adminWin.mainloop()

# this is the function called when the button is clicked
