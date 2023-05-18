# Import Module
from tkinter import *
# from tkinter.ttk import *
from calculator_test import *

# create root window
root = Tk()

# root window title and dimension
root.title("Cogs 1 Grade Calculator")
# Set geometry (widthxheight)
root.geometry('1000x600')

# all widgets will be here
welcome = Label(text="Hello! Welcome to the COGS 1 Grade Calculator!", width=50, height=2)

menu_message = """
Choose one of the following options:
1. Add assignment (type add)
2. Modify assignment (type modify)
3. Delete assignment (type delete)
4. Calculate grade (type calculate)
5. View assignments (type view)
6. Exit (type exit)
"""

label_menu = Label(text=menu_message, width=100, height=10)
entry1 = Entry(width=50)

welcome.pack()

label_menu.pack()
entry1.pack()



# Execute Tkinter
root.mainloop()

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