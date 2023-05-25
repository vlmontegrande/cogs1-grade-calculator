# Import Module
from tkinter import *
from tkinter import messagebox

menu1 = "1. Add assignment"
menu2 = "2. Modify assignment"
menu3 = "3. Delete assignment"
menu4 = "4. Calculate grade"
menu5 = "5. View assignments"
menu6 = "6. Exit"


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

        self.btn1 = Button(self.label_frame, text="Add", command=lambda: self.create_new_window("add"))
        self.btn2 = Button(self.label_frame, text="Modify", command=lambda: self.create_new_window("modify"))
        self.btn3 = Button(self.label_frame, text="Delete", command=lambda: self.create_new_window("delete"))
        self.btn4 = Button(self.label_frame, text="Calculate", command=lambda: self.create_new_window("calculate"))
        self.btn5 = Button(self.label_frame, text="View", command=lambda: self.create_new_window("view"))
        self.btn6 = Button(self.label_frame, text="Exit", command=self.destroy)

        self.btn1.grid(row=0, column=1)
        self.btn2.grid(row=1, column=1)
        self.btn3.grid(row=2, column=1)
        self.btn4.grid(row=3, column=1)
        self.btn5.grid(row=4, column=1)
        self.btn6.grid(row=5, column=1)

        self.label_frame.pack()

    def create_new_window(self, command):
        new_window = Toplevel(self.window)
        # new_window.geometry('500x300')
        new_window.title("Cogs 1 Grade Calculator")
        new_window.resizable(False, False)
        new_window.grab_set()
        new_window.focus_set()
        new_window.transient(self.window)
        # new_window.protocol("WM_DELETE_WINDOW", lambda: self.close_window(new_window))
        OtherWindow(new_window, command)

    def destroy(self):
        close = messagebox.askokcancel("Quit", "Do you want to quit?")
        if close:
            self.window.destroy()


class OtherWindow:

    def __init__(self, master, command):
        self.master = master
        self.command = command
        self.set_up_window()

    def set_up_window(self):
        if self.command == "add":
            self.master.title("Add Assignment")
            self.master.geometry('500x300')
            frame = Frame(self.master, height=500, width=300, padx=10, pady=10)
            frame.rowconfigure(0, weight=1, minsize=50)
            frame.rowconfigure(1, weight=1, minsize=50)
            frame.rowconfigure(2, weight=1, minsize=50)
            frame.rowconfigure(3, weight=1, minsize=50)
            frame.columnconfigure(0, weight=1, minsize=150)
            frame.columnconfigure(1, weight=1, minsize=150)

            label1 = Label(frame, text="Section: ")
            label2 = Label(frame, text="Grade: ")
            label3 = Label(frame, text="Date: ")

            entry1 = Entry(frame)
            entry2 = Entry(frame)
            entry3 = Entry(frame)

            label1.grid(row=0, column=0)
            label2.grid(row=1, column=0)
            label3.grid(row=2, column=0)

            entry1.grid(row=0, column=1)
            entry2.grid(row=1, column=1)
            entry3.grid(row=2, column=1)

            frame.pack()

            btn1 = Button(frame, text="Add", command=self.add)
            btn2 = Button(frame, text="Cancel", command=self.close_window)

            btn1.grid(row=3, column=0)
            btn2.grid(row=3, column=1)

        elif self.command == "modify":
            self.master.title("Modify Assignment")
            self.master.geometry('500x300')
            frame = Frame(self.master, height=500, width=300, padx=10, pady=10)
            frame.rowconfigure(0, weight=1, minsize=50)
            frame.rowconfigure(1, weight=1, minsize=50)
            frame.rowconfigure(2, weight=1, minsize=50)
            frame.rowconfigure(3, weight=1, minsize=50)
            frame.rowconfigure(4, weight=1, minsize=50)
            frame.columnconfigure(0, weight=1, minsize=150)
            frame.columnconfigure(1, weight=1, minsize=150)
            frame.columnconfigure(2, weight=1, minsize=150)

            label1 = Label(frame, text="ID: ")
            entry1 = Entry(frame)
            btn1 = Button(frame, text="Find Assignment", command=lambda: self.find(frame, entry1, btn1, label1))

            label1.grid(row=0, column=0)
            entry1.grid(row=0, column=1)
            btn1.grid(row=1, column=1)

            frame.pack()
        elif self.command == "delete":
            self.delete()
        elif self.command == "calculate":
            self.calculate()
        elif self.command == "view":
            self.view()

    def find(self, frame, entry, btn, label):
        # Finds assignment with given id
        # If found, displays assignment info
        # If not found, displays error message
        section = ""
        grade = ""
        date = ""
        with open("assignments.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                if line[0] == entry.get():
                    # Display assignment info
                    line = line.split(",")
                    section = line[1]
                    grade = line[2]
                    date = line[3]
                    break
            else:
                messagebox.showerror("Error", "Assignment not found")

        entry.destroy()
        btn.destroy()
        label.destroy()

        label1 = Label(frame, text="Old section: \"" + section + "\"")
        label2 = Label(frame, text="Old grade: \"" + grade + "\"")
        label3 = Label(frame, text="Old date: \"" + date + "\"")
        label4 = Label(frame, text="Section: ")
        label5 = Label(frame, text="Grade: ")
        label6 = Label(frame, text="Date: ")

        entry1 = Entry(frame)
        entry2 = Entry(frame)
        entry3 = Entry(frame)

        btn1 = Button(frame, text="Modify", command=lambda: self.modify(entry.get(), entry1.get(), entry2.get(), entry3.get()))
        btn2 = Button(frame, text="Cancel", command=self.close_window)

        label1.grid(row=0, column=2)
        label2.grid(row=1, column=2)
        label3.grid(row=2, column=2)
        label4.grid(row=0, column=0)
        label5.grid(row=1, column=0)
        label6.grid(row=2, column=0)
        btn1.grid(row=3, column=0)
        btn2.grid(row=3, column=1)
        entry1.grid(row=0, column=1)
        entry2.grid(row=1, column=1)
        entry3.grid(row=2, column=1)




    def add(self):
        pass

    def modify(self):
        pass

    def delete(self):
        pass

    def calculate(self):
        pass

    def view(self):
        pass

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
