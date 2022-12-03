import tkinter as tk
import random
from tkinter import ttk, messagebox
from tkinter import *
import re
from entities.Professor import Professor

# Make a regular expression
# for validating an Email

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


# this is the function called when the button is clicked
def addProfessor(root, admin):
    # this is a function to react to button click
    def add():
        if(not re.match(regex, str(email.get()))):
            messagebox.showinfo(title="Error",message="Enter valid Email")
            return
        if (not str(dept.get()).isalpha()):
            messagebox.showinfo(title="Error", message="Enter valid Department")
            return
        if( not str (name.get()).isalpha()):
            messagebox.showinfo(title="Error",message="Enter valid Name")
            return
        if (not str(number.get()).isdigit()):
            messagebox.showinfo(title="Error",message="Enter valid number in Contact")
            return
        if (not str(salary.get()).isdigit()):
            messagebox.showinfo(title="Error", message="Enter valid number Salary")
            return

        s = Professor()
        s.setVals(name.get(), email.get(), int(salary.get()), number.get(),random.randint(1,11),dept.get())
        admin.prof.append(s)
        messagebox.showinfo(title="Success", message="User Added")

    stuWIn = Tk()

    # This is the section of code which creates the main window
    stuWIn.geometry('500x350+50+100')
    stuWIn.configure(background='#FFEFDB')
    stuWIn.title('Add Professor')
    # variable of aligning y axis
    y=72
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
    Label(stuWIn, text='Contact', bg='#FFEFDB', font=('arial', 12, 'normal')).place(x=91, y=y)

    # This is the section of code which creates a text input box
    number = Entry(stuWIn)
    number.place(x=190, y=y)

    y += 40
    # This is the section of code which creates the a label
    Label(stuWIn, text='Department', bg='#FFEFDB', font=('arial', 12, 'normal')).place(x=91, y=y)

    # This is the section of code which creates a text input box
    dept = Entry(stuWIn)
    dept.place(x=190, y=y)
    y += 40
    Label(stuWIn, text='Salary', bg='#FFEFDB', font=('arial', 12, 'normal')).place(x=91, y=y)

    # This is the section of code which creates a text input box
    salary = Entry(stuWIn)
    salary.place(x=190, y=y)

    # this defines the operation on closing
    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            stuWIn.destroy()
            root.deiconify()

    stuWIn.protocol("WM_DELETE_WINDOW", on_closing)

    Button(stuWIn, text='Add Professor', bg='#F0F8FF', font=('arial', 12, 'normal'), command=add).place(x=307, y=311)
    stuWIn.mainloop()
