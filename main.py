from tkinter import ttk, messagebox
from tkinter import *
from adminWin import open_Adminwin
from AdminEmployee import AdminEmployee
from addStudent import addStudent
from addProfessor import addProfessor
# this is a function to get the user input from the text input box
def getInputBoxValue():
	pass


# this is a function to get the user input from the text input box
def getInputBoxValue():
	pass



def mainwin():
	root = Tk()
	admin= AdminEmployee()
	# This is the section of code which creates the main window
	root.geometry('500x350+50+100')
	root.configure(background='#FFEFDB')
	root.title('Login')


	# This is the section of code which creates the a label
	Label(root, text='Name', bg='#FFEFDB', font=('helvetica', 12, 'normal')).place(x=151, y=110)


	# This is the section of code which creates a text input box
	password=Entry(root)
	password.place(x=262, y=139)


	# This is the section of code which creates a text input box
	uname=Entry(root)
	uname.place(x=263, y=108)

	# This is the section of code which creates the a label
	Label(root, text='Pass', bg='#FFEFDB', font=('helvetica', 12, 'normal')).place(x=153, y=143)

	def checkIdPass(tempVar):
		# if(tempVar==0):
		# 	messagebox.showinfo(message="Select a User option")
		# 	return
		#

		if (password.get() == "123" and uname.get() == "admin"):
			root.withdraw()
			open_Adminwin(root, admin)
		else:
		 	messagebox.showinfo(message="Incorrect Username or password")
		# if(tempVar==1):
		# 	if(password.get()=="123" and uname.get()=="admin"):
		# 		open_Adminwin(root, admin)
		# 	else:
		# 		messagebox.showinfo(message="Incorrect Username or password")
		# else
		# 	if (password.get() == "123" and uname.get() == "prof"):
		# 		addProfessor(root, admin)
		# 	else:
		# 		messagebox.showinfo(message="Incorrect Username or password")
		#


	# This is the section of code which creates a button



	# this is the declaration of the variable associated with the radio button group


	def sel(x):
		#selection = "You selected the  " + str(var.get())
		tempVar=var.get()
		print(tempVar)
		#print(selection)
	#................................for creating radio button for user selection if more than one user can login
	var = IntVar()
	# R1 = Radiobutton(root, text="Admin", variable=var, value=1,
	# 				 command=lambda :sel(1))
	#
	# R1.pack(anchor=W)
	# R2 = Radiobutton(root, text="Professor", variable=var, value=2,
	# 				 command=lambda :sel(2))
	# R2.pack(anchor=W)
	#
	# R3 = Radiobutton(root, text="Student", variable=var, value=3,
	# 				 command=lambda :sel(3))
	# R3.pack(anchor=W)
	# R3.place(x=300, y=178)
	#
	# R1.place(x=200, y=178)
	# R2.place(x=250, y=178)
	# This is the section of code which creates the a label
	#Label(root, text='User : ', bg='#FFEFDB', font=('helvetica', 12, 'normal')).place(x=153, y=178)

	Button(root, text='Login', bg='#F0FFFF', font=('helvetica', 12, 'bold'), command=lambda :checkIdPass(var.get())).place(x=218, y=230)

	# this defines the operation on closing
	def on_closing():
		admin.save()
		root.destroy()

	root.protocol("WM_DELETE_WINDOW", on_closing)

	root.mainloop()



mainwin()