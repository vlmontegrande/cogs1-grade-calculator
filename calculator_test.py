# get input from user for assignment

import time

dictionary = {}


class Assignment:
    count = 0

    def __init__(self, section, grade, date, foo):
        with open("assignments.txt", "r") as f:
            data = f.readlines()
        if foo:
            self.count = int(data[0].split(" ")[1])
        else:
            while self.count in dictionary:
                self.count += 1
        self.id = self.count
        self.count += 1
        data[0] = "count: " + str(self.count) + "\n"
        self.section = section
        self.grade = int(grade)
        self.date = date
        dictionary[self.id] = self
        if foo:
            with open('assignments.txt', 'w') as f:
                f.writelines(data)
                f.write(str(self.id) + "," + self.section + "," + str(self.grade) + "," + self.date + "\n")

    def update(self, section, grade, date):
        self.section = section
        self.grade = grade
        self.date = date

    def __str__(self):
        return self.section + " " + str(self.grade) + " " + self.date


def modify(id):
    print("Modify assignment")
    section = input("Section: ")
    grade = input("Grade: ")
    date = input("Date: ")
    dictionary.get(id).update(section, grade, date)
    # writes changes to file
    with open("assignments.txt", "r") as f:
        data = f.readlines()
    data[id + 1] = str(id) + "," + section + "," + str(grade) + "," + date + "\n"
    with open('assignments.txt', 'w') as f:
        f.writelines(data)


def delete(id):
    del dictionary[id]
    # deletes line in file
    with open("assignments.txt", "r") as f:
        data = f.readlines()
    data[id + 1] = "\n"
    with open('assignments.txt', 'w') as f:
        f.writelines(data)


def calculate_grade():
    quizzes = 0
    midterm1 = 0
    midterm2 = 0
    final = 0
    count = 0
    for assignment in dictionary:
        if dictionary[assignment].section == "quiz":
            quizzes += dictionary[assignment].grade
            count += 1
        elif dictionary[assignment].section == "midterm1":
            midterm1 = dictionary[assignment].grade
        elif dictionary[assignment].section == "midterm2":
            midterm2 = dictionary[assignment].grade
        elif dictionary[assignment].section == "final":
            final = dictionary[assignment].grade
        else:
            print("Invalid section")
    quizzes /= count if count != 0 else 90
    midterm1 = 90 if midterm1 == 0 else midterm1
    midterm2 = 90 if midterm2 == 0 else midterm2
    final = 90 if final == 0 else final
    return quizzes * 0.25 + midterm1 * 0.25 + midterm2 * 0.25 + final * 0.25


def get_input():
    choice = ""
    print("Hi! Welcome to the grade calculator!")
    while choice != "exit":
        print("Choose one of the following options:")
        print("1. Add assignment (type add)")
        print("2. Modify assignment (type modify)")
        print("3. Delete assignment (type delete)")
        print("4. Calculate grade (type calculate)")
        print("5. See all assignments (type see all)")
        print("6. Clear all assignments (type clear)")
        print("7. Exit (type exit)")
        choice = input("Type your answer: ")
        if choice == "add":
            section = input("Section: ")
            grade = input("Grade: ")
            date = input("Date: ")
            Assignment(section, int(grade), date, True)
            print("Successfully added assignment!")
        elif choice == "modify":
            id = input("ID: ")
            modify(int(id))
            print("Successfully modified assignment!")
        elif choice == "delete":
            id = input("ID: ")
            delete(int(id))
            print("Successfully deleted assignment!")
        elif choice == "calculate":
            print("Your grade is: {}%".format(calculate_grade()))
        elif choice == "see all":
            see_all()
        elif choice == "clear":
            clear()
        elif choice == "exit":
            print("Goodbye!")
        else:
            print("Invalid input")


def fill_dictionary():
    with open("assignments.txt", "r") as f:
        data = f.readlines()
    for i in range(1, len(data)):
        if data[i] == "\n":
            continue
        line = data[i].split(",")
        Assignment(line[1], int(line[2]), line[3].strip(), False)


def see_all():
    for assignment in dictionary:
        print(dictionary[assignment])


def clear():
    dictionary.clear()
    # deletes all lines in file
    with open("assignments.txt", "r") as f:
        data = f.readlines()
    data = ["count: 0\n"]
    with open('assignments.txt', 'w') as f:
        f.writelines(data)


def main():
    fill_dictionary()
    get_input()


# if __name__ == "__main__":
    # main()
