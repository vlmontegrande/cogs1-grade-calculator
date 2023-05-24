# Import Module
from tkinter import *
# from tkinter.ttk import *
from calculator_test import *

menu1 = "1. Add assignment (type add)"
menu2 = "2. Modify assignment (type modify)"
menu3 = "3. Delete assignment (type delete)"
menu4 = "4. Calculate grade (type calculate)"
menu5 = "5. View assignments (type view)"
menu6 = "6. Exit (type exit)"


class MainWindow:

    def __init__(self, window):
        self.window = window

        self.label_frame = Frame(window)
        self.label_frame.rowconfigure(0, weight=1)
        self.label_frame.rowconfigure(1, weight=1)
        self.label_frame.rowconfigure(2, weight=1)
        self.label_frame.rowconfigure(3, weight=1)
        self.label_frame.rowconfigure(4, weight=1)
        self.label_frame.columnconfigure(0, weight=1)
        self.label_frame.columnconfigure(1, weight=1)

        self.welcome = Label(self.window, text="Hello! Welcome to the COGS 1 Grade Calculator!", width=50, height=2)
        self.menu1 = Label(self.label_frame, text=menu1)
        self.menu2 = Label(self.label_frame, text=menu2)
        self.menu3 = Label(self.label_frame, text=menu3)
        self.menu4 = Label(self.label_frame, text=menu4)
        self.menu5 = Label(self.label_frame, text=menu5)
        self.menu6 = Label(self.label_frame, text=menu6)

        self.menu1.grid(row=0, column=0)
        self.menu2.grid(row=1, column=0)
        self.menu3.grid(row=2, column=0)
        self.menu4.grid(row=3, column=0)
        self.menu5.grid(row=4, column=0)
        self.menu6.grid(row=5, column=0)

        self.welcome.pack()

        self.btn1 = Button(self.label_frame, text="Add", command=self.command)
        self.btn2 = Button(self.label_frame, text="Modify", command=self.command)
        self.btn3 = Button(self.label_frame, text="Delete", command=self.command)
        self.btn4 = Button(self.label_frame, text="Calculate", command=self.command)
        self.btn5 = Button(self.label_frame, text="View", command=self.command)
        self.btn6 = Button(self.label_frame, text="Exit", command=self.destroy)

        self.btn1.grid(row=0, column=1)
        self.btn2.grid(row=1, column=1)
        self.btn3.grid(row=2, column=1)
        self.btn4.grid(row=3, column=1)
        self.btn5.grid(row=4, column=1)
        self.btn6.grid(row=5, column=1)

        self.label_frame.pack()

    def command(self):

        self.newWindow = Toplevel(self.window)
        self.app = OtherWindow(self.newWindow)

    def destroy(self):
        self.window.destroy()


class OtherWindow:

    def __init__(self, master):
        self.master = master
        self.frame = Frame(master)
        master.title("a")
        self.quitButton = Button(self.frame, text='Quit', width=25, command=self.close_window)
        self.quitButton.pack()
        self.frame.pack()

    def close_window(self):
        self.master.destroy()


# create root window
root = Tk()

# root window title and dimension
root.title("Cogs 1 Grade Calculator")
# Set geometry (widthxheight)
root.geometry('500x300')

cls = MainWindow(root)

root.mainloop()

"""
option = entry1.get()
while option != exit:
    if option == "add":
        section = input("Section: ")
        grade = input("Grade: ")
        date = input("Date: ")
        Assignment(section, int(grade), date, True)
        print("Successfully added assignment!")
    elif option == "modify":
        id = input("ID: ")
        modify(int(id))
        print("Successfully modified assignment!")
    elif option == "delete":
        id = input("ID: ")
        delete(int(id))
        print("Successfully deleted assignment!")
    elif option == "calculate":
        print("Your grade is: {}%".format(calculate_grade()))
    elif option == "view":
        see_all()
    elif option == "exit":
        break
    else:
        print("Invalid option")
    option = input("Type your answer: ")
"""
