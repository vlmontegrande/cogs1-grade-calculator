# Import Module
from tkinter import *
# from tkinter.ttk import *
from calculator_test import *

menu_message = """
Choose one of the following options:
1. Add assignment (type add)
2. Modify assignment (type modify)
3. Delete assignment (type delete)
4. Calculate grade (type calculate)
5. View assignments (type view)
6. Exit (type exit)
"""


class MainWindow:

    def __init__(self, window):
        self.window = window
        self.frame = Frame(window, width=0, height=0)
        self.welcome = Label(self.frame, text="Hello! Welcome to the COGS 1 Grade Calculator!", width=50, height=2)
        self.menu = Label(self.frame, text=menu_message, width=100, height=10)
        self.entry = Entry(self.frame, width=50)
        self.welcome.pack()
        self.menu.pack()
        self.btn = Button(self.frame, text="Button", command=self.command)
        self.frame.grid(row=0, column=0)
        self.btn.pack()
        self.frame.pack()

    def command(self):

        self.newWindow = Toplevel(self.window)
        self.app = OtherWindow(self.newWindow)


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

# option = entry1.get()
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
