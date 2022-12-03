import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
import re
from entities.Student import Student

# Make a regular expression
# for validating an Email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'



# this is the function called when the button is clicked
def addStudent(root, admin):
    # this is a function to react to button click
    def add():
        if(not re.match(regex, str(email.get()))):
            messagebox.showinfo(title="Error",message="Enter valid Email")
            return
        if( not str (name.get()).isalpha()):
            messagebox.showinfo(title="Error",message="Enter valid Name")
            return
        if (not str(number.get()).isdigit()):
            messagebox.showinfo(title="Error",message="Enter valid Credits number")
            return
        if (not str(dept.get()).isalpha()):
            messagebox.showinfo(title="Error", message="Enter valid Department")
            return
        if (not str(coarse.get()).isalpha()):
            messagebox.showinfo(title="Error", message="Enter valid Coarse")
            return

        s=Student()
        s.setVals(name.get(),email.get(),coarse.get(),dept.get(),number.get())
        admin.stud.append(s)
        messagebox.showinfo(title="Success",message="User Added")

    stuWIn = Tk()

    # This is the section of code which creates the main window
    stuWIn.geometry('500x350+50+100')
    stuWIn.configure(background='#FFEFDB')
    stuWIn.title('Add Student')

    # vairable for alignment of y axis
    y=74
    # This is the section of code which creates the a label
    Label(stuWIn, text='Name', bg='#FFEFDB', font=('arial', 12, 'normal')).place(x=94, y=y)

    # This is the section of code which creates a text input box
    name = Entry(stuWIn)
    name.place(x=191, y=y)
    y+=40
    # This is the section of code which creates the a label
    Label(stuWIn, text='Email', bg='#FFEFDB', font=('arial', 12, 'normal')).place(x=94, y=y)

    # This is the section of code which creates a text input box
    email = Entry(stuWIn)
    email.place(x=189, y=y)
    y += 40
    # This is the section of code which creates the a label
    Label(stuWIn, text='Credits', bg='#FFEFDB', font=('arial', 12, 'normal')).place(x=91, y=y)

    # This is the section of code which creates a text input box
    number = Entry(stuWIn)
    number.place(x=190, y=y)

    y += 40

    # This is the section of code which creates the a label
    Label(stuWIn, text='Coarse', bg='#FFEFDB', font=('arial', 12, 'normal')).place(x=91, y=y)

    # This is the section of code which creates a text input box
    coarse = Entry(stuWIn)
    coarse.place(x=190, y=y)
    y += 40

    Label(stuWIn, text='Department', bg='#FFEFDB', font=('arial', 12, 'normal')).place(x=91, y=y)

    # This is the section of code which creates a text input box
    dept = Entry(stuWIn)
    dept.place(x=190, y=y)

    # this defines the operation on closing
    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            stuWIn.destroy()
            root.deiconify()

    stuWIn.protocol("WM_DELETE_WINDOW", on_closing)


    Button(stuWIn, text='Add Student', bg='#F0F8FF', font=('arial', 12, 'normal'), command=add).place(x=307, y=311)
    stuWIn.mainloop()
