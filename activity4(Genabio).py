"""
    <Anton James J. Genabio>
    <MW 9:00 AM - 10:30 AM>
    <13953>
	create a file 'student.txt', read,write and update this file
	for the student list
	Create the student list with a menu provided below
	----------- Student List -----------
    1. Add Student
    2. Find Student
    3. Delete Student
    4. Update Student
    5. Display All Student
    0. Quit/End
    ------------------------------------
    Enter Option(0..5):
    sample student entry below

    student:dict = {
        'idno':'0001',
        'lastname':'alpha',
        'firstname':'bravo',
        'course':'bsit',
        'level':'3',
    }
"""

from os import system


def display() -> None:
    disp: list = (
        "----------- Student List -----------",
        "1. Add Student",
        "2. Find Student",
        "3. Delete Student",
        "4. Update Student",
        "5. Display All Student",
        "0. Quit/End",
        "------------------------------------"
    )

    [print(d) for d in disp]


def addStud() -> None:
    system("cls")
    print("-----ADD STUDENT-----")
    idNum = input("Enter ID Number: ")
    lastName = input("Enter Last Name: ")
    firstName = input("Enter First Name: ")
    course = input("Enter Course: ")
    yearLevel = input("Enter Year Level: ")

    with open('students.txt', 'a') as writer:
        writer.write("\n"+idNum+','+lastName+','+firstName+','+course+','+yearLevel)
        writer.close()







def findStud() -> None:
    system("cls")
    print("-----FIND STUDENT-----")
    idNum = input("Input ID Number to find Student (xxxx): ")
    studentDict = readFile()

    if idNum in studentDict:
        studentDisplay = studentDict[idNum]
        print("Student Found!")
        print("Id#: " + studentDisplay.idNum + "\nLast Name: " + studentDisplay.lastName + "\nFirst Name: " + studentDisplay.firstName + "\nCourse: " + studentDisplay.course + "\nYear Level: " + studentDisplay.yearLevel)
    else:
        print("Student Not Found!")

def deleteStud() -> None:
    system("cls")
    print("-----DELETE STUDENT-----")
    idNum = input("Input ID Number to delete Student (xxxx): ")
    studentDict = readFile()

    if idNum in studentDict:
        del studentDict[idNum]
        print("Student Deleted!")


        with open('students.txt', 'w+') as writer:
            for i in studentDict:
                studentDisplay = studentDict[i]
                writer.write(studentDisplay.idNum + ',' + studentDisplay.lastName + ',' + studentDisplay.firstName + ',' + studentDisplay.course + ',' + studentDisplay.yearLevel+"\n")
            writer.close()

    else:
        print("Student Not Found!")


def updateStud() -> None:
    system("cls")
    print("-----UPDATE STUDENT-----")
    idNum = input("Input ID Number to Update Student (xxxx): ")
    studentDict = readFile()

    menu : list = [
        "Update Student",
        "1. ID#",
        "2. LastName",
        "3. FirstName",
        "4. Course",
        "5. YearLevel",
    ]


    if idNum in studentDict:
        studentDisplay = studentDict[idNum]
        print("Found Student!")
        print("Id#: " + studentDisplay.idNum + " | Last Name: " + studentDisplay.lastName + " | First Name: " + studentDisplay.firstName + " | Course: " + studentDisplay.course + " | Year Level: " + studentDisplay.yearLevel+"\n")
        [print(x) for x in menu]
        ch = int(input("Choice: "))
        if ch == 1:
            newId = input("Input new ID: ")
            studentDisplay.idNum = newId
        elif ch == 2:
            newLast = input("Input new LastName: ")
            studentDisplay.lastName = newLast
        elif ch == 3:
            newF = input("Input new FirstName: ")
            studentDisplay.firstName = newF
        elif ch == 4:
            newC = input("Input new Course: ")
            studentDisplay.course = newC
        elif ch == 5:
            newY = input("Input new YearLevel: ")
            studentDisplay.yearLevel = newY
        else:
            print("Invalid Input!")

        with open('students.txt', 'w+') as writer:
            for i in studentDict:
                studentDisplay = studentDict[i]
                writer.write(studentDisplay.idNum + ',' + studentDisplay.lastName + ',' + studentDisplay.firstName + ',' + studentDisplay.course + ',' + studentDisplay.yearLevel+"\n")
            writer.close()



def displayStud() -> None:
    system("cls")
    print("-----DISPLAY STUDENT-----")
    studentDict = readFile()
    for i in studentDict:
        studentDisplay = studentDict[i]
        print("Id#: " + studentDisplay.idNum + "\nLast Name: " + studentDisplay.lastName + "\nFirst Name: " + studentDisplay.firstName + "\nCourse: " + studentDisplay.course + "\nYear Level: " + studentDisplay.yearLevel)



def end() -> None:
    print("Program Terminated!")





def readFile() -> dict:
    studentDict = dict()
    with open('students.txt', 'r') as file:
        line = file.readline()
        while line:
            data: str = line
            newData: list = data.split(",")
            if len(newData) >= 5:
                stud = Student(newData[0], newData[1], newData[2], newData[3], newData[4])
                studentDict[newData[0]] = stud
            line = file.readline()

    return studentDict

class Student:
    def __init__(self, idNum, lastName, firstName, course, yearLevel):
        self.idNum = idNum
        self.lastName = lastName
        self.firstName = firstName
        self.course = course
        self.yearLevel = yearLevel


def choices(i) -> str:
    ch: dict = {
        1: addStud,
        2: findStud,
        3: deleteStud,
        4: updateStud,
        5: displayStud,
        0: end,
    }

    return ch.get(i)


def main() -> None:


    while True:
        system("cls")
        display()
        opt = int(input("Enter Option(0..5): "))
        if opt >= 0 and opt <= 5:
            choices(opt)()
            if opt == 0:
                break

        else:
            print("Invalid Input!")


if __name__ == "__main__":
    main()
