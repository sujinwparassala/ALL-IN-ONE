
# importing only those functions
# which are needed
import tkinter
from tkinter import *
from tkinter.ttk import *
from time import strftime
root = Tk()
root.title('Menu Demonstration')

# Creating Menubar
menubar = Menu(root)

root.geometry("850x700")
root.configure(bg='light blue')
root.title('ALL IN ONE')
photo = PhotoImage(file = "suv.png")
root.iconphoto(False, photo)



# Adding File Menu and commands
file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='File', menu = file)
file.add_command(label ='New File', command = None)
file.add_command(label ='Open...', command = None)
file.add_command(label ='Save', command = None)
file.add_separator()
file.add_command(label ='Exit', command = root.destroy)

# Adding Edit Menu and commands
edit = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Edit', menu = edit)
edit.add_command(label ='Cut', command = None)
edit.add_command(label ='Copy', command = None)
edit.add_command(label ='Paste', command = None)
edit.add_command(label ='Select All', command = None)
edit.add_separator()
edit.add_command(label ='Find...', command = None)
edit.add_command(label ='Find again', command = None)

# Adding Help Menu
help_ = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Help', menu = help_)
help_.add_command(label ='Tk Help', command = None)
help_.add_command(label ='Demo', command = None)
help_.add_separator()
help_.add_command(label ='About Tk', command = None)

# Adding Help Menu
help_ = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Help', menu = help_)
help_.add_command(label ='Tk Help', command = None)
help_.add_command(label ='Demo', command = None)
help_.add_separator()
help_.add_command(label ='About Tk', command = None)

# Adding Help Menu
help_ = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Help', menu = help_)
help_.add_command(label ='Tk Help', command = None)
help_.add_command(label ='Demo', command = None)
help_.add_separator()
help_.add_command(label ='About Tk', command = None)



#tkinter.Label(root, text ='ALL IN ONE',font = "50")
#a.pack()

def hai():
    import pyqrcode
    s=input("PLEASE ENTER CHARACTER")
    b=pyqrcode.create(s)
    x = input("Enter the size you want")
    b.svg('qr.svg',scale=int(x))

lab1=tkinter.Label(root, 
		 text="ALL IN ONE",
		 fg = "light green",
		 bg = "dark green",
		 font = "Helvetica 16 bold italic",)
lab1.pack(side = TOP)


lab2=tkinter.Label(root, 
		 text="Blue Text in Verdana bold",
		 fg = "blue",
		 bg = "yellow",
		 font = "Verdana 10 bold")
lab2.pack(padx=10)


#lab3=tkinter.Label(root, 
#		 text="Red Text in Times Font",justify="left",
#		 fg = "red",
#		 font = "Times")
#lab3.pack(padx=5,pady=5)


B = tkinter.Button(root, activebackground="BLUE",activeforeground="red",bd=6,bg="brown",text ="QR-CODE",height="2",width="8",underline=-1,wraplength=-1, command = hai)

B.pack(side=LEFT)

B2 = tkinter.Button(root, activebackground="BLUE",activeforeground="red",bd=6,bg="GREEN",text ="PDF",height="2",width="8",underline=-1,wraplength=-1, command = hai)

B2.pack(side=LEFT)


B3 = tkinter.Button(root, activebackground="BLUE",activeforeground="red",bd=6,bg="brown",text ="YOUTUBE DOWNLOADER",height="2",width="8",underline=-1,wraplength=-1, command = hai)

B3.pack(side=LEFT)

# display Menu
root.config(menu = menubar)
mainloop()









