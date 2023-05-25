# Import Module
from tkinter import *
from tkinter import messagebox
from calculator_test import *

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

        self.welcome = Label(self.window, text="Hello! Welcome to the COGS 1 Grade Calculator!", width=50, height=2,
                             font=("Arial", 12))
        self.menu1 = Label(self.label_frame, text=menu1, font=("Arial", 12))
        self.menu2 = Label(self.label_frame, text=menu2, font=("Arial", 12))
        self.menu3 = Label(self.label_frame, text=menu3, font=("Arial", 12))
        self.menu4 = Label(self.label_frame, text=menu4, font=("Arial", 12))
        self.menu5 = Label(self.label_frame, text=menu5, font=("Arial", 12))
        self.menu6 = Label(self.label_frame, text=menu6, font=("Arial", 12))

        self.menu1.grid(row=0, column=0)
        self.menu2.grid(row=1, column=0)
        self.menu3.grid(row=2, column=0)
        self.menu4.grid(row=3, column=0)
        self.menu5.grid(row=4, column=0)
        self.menu6.grid(row=5, column=0)

        self.welcome.pack()

        self.btn1 = Button(self.label_frame, text="Add", command=lambda: self.create_new_window("add"),
                           font=("Arial", 12))
        self.btn2 = Button(self.label_frame, text="Modify", command=lambda: self.create_new_window("modify"),
                           font=("Arial", 12))
        self.btn3 = Button(self.label_frame, text="Delete", command=lambda: self.create_new_window("delete"),
                           font=("Arial", 12))
        self.btn4 = Button(self.label_frame, text="Calculate", command=self.calculate,
                           font=("Arial", 12))
        self.btn5 = Button(self.label_frame, text="View", command=self.view,
                           font=("Arial", 12))
        self.btn6 = Button(self.label_frame, text="Exit", command=self.destroy, font=("Arial", 12))

        self.btn1.grid(row=0, column=1)
        self.btn2.grid(row=1, column=1)
        self.btn3.grid(row=2, column=1)
        self.btn4.grid(row=3, column=1)
        self.btn5.grid(row=4, column=1)
        self.btn6.grid(row=5, column=1)

        self.label_frame.pack()
        window.protocol("WM_DELETE_WINDOW", self.destroy)

    def create_new_window(self, command):
        new_window = Toplevel(self.window)
        # new_window.geometry('500x300')
        new_window.title("Cogs 1 Grade Calculator")
        new_window.resizable(False, False)
        new_window.grab_set()
        new_window.focus_set()
        new_window.transient(self.window)
        OtherWindow(new_window, command)

    def calculate(self):
        messagebox.showinfo("Calculate", "Your grade is: {}%".format(calculate_grade()))

    def view(self):
        messagebox.showinfo("View", "Your assignments are:\n\n{}".format(view_assignments()))

    def destroy(self):
        close = messagebox.askokcancel("Quit", "Do you want to quit?")
        if close:
            self.window.destroy()


class OtherWindow:

    def __init__(self, master, command):
        self.master = master
        self.command = command
        self.set_up_window()
        master.protocol("WM_DELETE_WINDOW", self.close_window)

    def set_up_window(self, command=None):
        if command == "add" or self.command == "add":
            self.master.title("Add Assignment")
            self.master.geometry('500x300')
            frame = Frame(self.master, height=500, width=300, padx=10, pady=10)
            frame.rowconfigure(0, weight=1, minsize=50)
            frame.rowconfigure(1, weight=1, minsize=50)
            frame.rowconfigure(2, weight=1, minsize=50)
            frame.rowconfigure(3, weight=1, minsize=50)
            frame.columnconfigure(0, weight=1, minsize=150)
            frame.columnconfigure(1, weight=1, minsize=150)

            label1 = Label(frame, text="Section: ", font=("Arial", 12))
            label2 = Label(frame, text="Grade: ", font=("Arial", 12))
            label3 = Label(frame, text="Date: ", font=("Arial", 12))

            entry1 = Entry(frame)
            entry2 = Entry(frame)
            entry3 = Entry(frame)

            label1.grid(row=0, column=0, padx=10, pady=10)
            label2.grid(row=1, column=0, padx=10, pady=10)
            label3.grid(row=2, column=0, padx=10, pady=10)

            entry1.grid(row=0, column=1, padx=10, pady=10)
            entry2.grid(row=1, column=1, padx=10, pady=10)
            entry3.grid(row=2, column=1, padx=10, pady=10)

            frame.pack()

            btn1 = Button(frame, text="Add", command=lambda: self.add(entry1, entry2, entry3),
                          font=("Arial", 12))
            btn2 = Button(frame, text="Cancel", command=self.close_window, font=("Arial", 12))

            btn1.grid(row=3, column=0, padx=10, pady=10)
            btn2.grid(row=3, column=1, padx=10, pady=10)

        elif command == "modify" or self.command == "modify":
            self.master.title("Modify Assignment")
            self.master.geometry('500x300')
            frame = Frame(self.master, height=500, width=300, padx=10, pady=10)
            frame.rowconfigure(0, weight=1, minsize=50)
            frame.rowconfigure(1, weight=1, minsize=50)
            frame.rowconfigure(2, weight=1, minsize=50)
            frame.rowconfigure(3, weight=1, minsize=50)
            frame.rowconfigure(4, weight=1, minsize=50)
            frame.columnconfigure(0, weight=1, minsize=100)
            frame.columnconfigure(1, weight=1, minsize=100)
            frame.columnconfigure(2, weight=1, minsize=100)

            label1 = Label(frame, text="ID:", font=("Arial", 12))
            entry1 = Entry(frame)
            btn1 = Button(frame, text="Find Assignment", command=lambda: self.find_to_modify(frame, entry1, btn1, label1),
                          font=("Arial", 12))

            label1.grid(row=0, column=0, padx=10, pady=10)
            entry1.grid(row=0, column=1, padx=10, pady=10)
            btn1.grid(row=1, column=1, padx=10, pady=10)

            frame.pack()
        elif command == "delete" or self.command == "delete":
            self.master.title("Delete Assignment")
            self.master.geometry('500x300')
            frame = Frame(self.master, height=500, width=300, padx=10, pady=10)
            frame.rowconfigure(0, weight=1, minsize=50)
            frame.rowconfigure(1, weight=1, minsize=50)
            frame.rowconfigure(2, weight=1, minsize=50)
            frame.rowconfigure(3, weight=1, minsize=50)
            frame.rowconfigure(4, weight=1, minsize=50)
            frame.columnconfigure(0, weight=1, minsize=100)
            frame.columnconfigure(1, weight=1, minsize=100)
            frame.columnconfigure(2, weight=1, minsize=100)

            label1 = Label(frame, text="ID:", font=("Arial", 12))
            entry1 = Entry(frame)
            btn1 = Button(frame, text="Delete", command=lambda: self.find_to_delete(frame, entry1),
                          font=("Arial", 12))

            label1.grid(row=0, column=0, padx=10, pady=10)
            entry1.grid(row=0, column=1, padx=10, pady=10)
            btn1.grid(row=1, column=1, padx=10, pady=10)

            frame.pack()

    def find_to_delete(self, frame, entry):
        # Finds assignment with given id
        # If found, displays assignment info
        # If not found, displays error message
        section = ""
        grade = ""
        date = ""
        with open("assignments.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                if line[0] == entry.get().strip():
                    # Display assignment info
                    line = line.split(",")
                    section = line[1].strip()
                    grade = line[2].strip()
                    date = line[3].strip()
                    break
            else:
                messagebox.showerror("Error", "Assignment not found")
                self.set_up_window("delete")
                return
        foo = messagebox.askokcancel("Delete Assignment", "Are you sure you want to delete this assignment?\n\nID: " + entry.get() + "\nSection: " + section + "\nGrade: " + grade + "\nDate: " + date)
        if foo:
            messagebox.showinfo("Success", "Assignment deleted successfully")
            delete(int(entry.get().strip()))
            entry.delete(0, END)
        else:
            self.set_up_window("delete")

    def find_to_modify(self, frame, entry, btn, label):
        # Finds assignment with given id
        # If found, displays assignment info
        # If not found, displays error message
        section = ""
        grade = ""
        date = ""
        with open("assignments.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                if line[0] == entry.get().strip():
                    # Display assignment info
                    line = line.split(",")
                    section = line[1].strip()
                    grade = line[2].strip()
                    date = line[3].strip()
                    break
            else:
                messagebox.showerror("Error", "Assignment not found")
                self.set_up_window("modify")
                return

        entry.destroy()
        btn.destroy()
        label.destroy()

        label1 = Label(frame, text="Old section: \"" + section + "\"", font=("Arial", 12))
        label2 = Label(frame, text="Old grade: \"" + grade + "\"", font=("Arial", 12))
        label3 = Label(frame, text="Old date: \"" + date + "\"", font=("Arial", 12))
        label4 = Label(frame, text="Section:", font=("Arial", 12))
        label5 = Label(frame, text="Grade:", font=("Arial", 12))
        label6 = Label(frame, text="Date:", font=("Arial", 12))

        entry1 = Entry(frame)
        entry2 = Entry(frame)
        entry3 = Entry(frame)

        btn1 = Button(frame, text="Modify",
                      command=lambda: self.modify(entry.get(), entry1.get(), entry2.get(), entry3.get()))
        btn2 = Button(frame, text="Cancel", command=self.close_window)

        label1.grid(row=0, column=2, sticky=W, padx=10, pady=10)
        label2.grid(row=1, column=2, sticky=W, padx=10, pady=10)
        label3.grid(row=2, column=2, sticky=W, padx=10, pady=10)
        label4.grid(row=0, column=0, sticky=W, padx=10, pady=10)
        label5.grid(row=1, column=0, sticky=W, padx=10, pady=10)
        label6.grid(row=2, column=0, sticky=W, padx=10, pady=10)
        btn1.grid(row=3, column=0, padx=10, pady=10)
        btn2.grid(row=3, column=1, padx=10, pady=10)
        entry1.grid(row=0, column=1, padx=10, pady=10)
        entry2.grid(row=1, column=1, padx=10, pady=10)
        entry3.grid(row=2, column=1, padx=10, pady=10)

    def add(self, entry1, entry2, entry3):
        Assignment(entry1.get(), int(entry2.get()), entry3.get(), True)
        entry1.delete(0, END)
        entry2.delete(0, END)
        entry3.delete(0, END)
        messagebox.showinfo("Success", "Successfully added assignment!")

    def modify(self, id, section, grade, date):
        modify(int(id), section, int(grade), date)

        messagebox.showinfo("Success", "Successfully modified assignment!")

    def delete(self, id):
        delete(int(id))

        messagebox.showinfo("Success", "Successfully deleted assignment!")

    def close_window(self):
        self.master.destroy()


fill_dictionary()

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