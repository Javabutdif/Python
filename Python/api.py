"""
	Student API(application program interface)
"""
from Student import * #import all properties from Student file
from os import system

slist:list = []
filename:str = "student.csv" #comma-separated-variables

def header(message:str)->None:
	system("cls")
	print(message)
	print("---------------------")


	
def checkid(student:Student)->bool:
    studDict = readerFile()
    
    if student.idno in studDict.keys(): return True
    else: return False
	#######
	
def addStudent()->None:
    header("Add Student")
    idno:str = input("Enter IDNO :")
    lastname:str = input("Enter LASTNAME :")
    firstname:str = input("Enter FIRSTNAME :")
    course:str = input("Enter COURSE :")
    level:str = input("Enter LEVEL :")
    if checkid(Student(idno,lastname,firstname,course,level)):
        print("Error! Student Id number duplicate")
    else:
        student = Student(idno,lastname,firstname,course,level)
        f = open(filename,"a")
        f.write(student.__str__())
        f.write("\n")
        f.close()
        print()
        print("New Student Added")
	
def findStudent()->None:
    studentDict = readerFile()
    header("Find Student")
    idNumber = input("Enter Student ID#: ")

    if idNumber in studentDict.keys():
        print("Student Found!")
        print("==============")
        print(studentDict[idNumber].__str__())
        print("==============")
    else:
        print("Student not found!")
def deleteStudent()->None:
	studentDict = readerFile()
	header("Delete Student")
	idNumber = input("Enter Student ID# to Delete: ")

	if idNumber in studentDict.keys():
		print("Student Found!")
		print("==============")
		print(studentDict[idNumber].__str__())
		print("==============")
		choice = input("Do you really want to delete this student? [Y/N]")
		if choice == 'Y' or choice == 'y':
			del studentDict[idNumber]
			print("Student Deleted!")

			with open(filename, 'w+') as writer:
				for i in studentDict:
					studentDisplay = studentDict[i]
					writer.write(studentDisplay.idno + ',' + studentDisplay.lastname + ',' + studentDisplay.firstname + ',' + studentDisplay.course + ',' + studentDisplay.level)
				writer.close()
	else:
		print("Student not found!")
def updateStudent()->None:
	header("Update Student")
	idNum = input("Enter Student ID# to Delete: ")
	studentDict = readerFile()

	menu: list = [
		"Update Student",
		"1. LastName",
		"2. FirstName",
		"3. Course",
		"4. YearLevel",
	]

	if idNum in studentDict:
		studentDisplay = studentDict[idNum]
		print("Found Student!")
		print("Id#: " + studentDisplay.idno + " | Last Name: " + studentDisplay.lastname + " | First Name: " + studentDisplay.firstname + " | Course: " + studentDisplay.course + " | Year Level: " + studentDisplay.level + "\n")
		[print(x) for x in menu]
		ch = int(input("Choice: "))
		if ch == 1:
			newLast = input("Input new LastName: ")
			studentDisplay.lastname = newLast

		elif ch == 2:
			newF = input("Input new FirstName: ")
			studentDisplay.firstname = newF
		elif ch == 3:
			newC = input("Input new Course: ")
			studentDisplay.course = newC
		elif ch == 4:
			newY = input("Input new YearLevel: ")
			studentDisplay.level = newY
		else:
			print("Invalid Input!")

		with open(filename, 'w+') as writer:
			for i in studentDict:
				studentDisplay = studentDict[i]
				writer.write(studentDisplay.idno + ',' + studentDisplay.lastname + ',' + studentDisplay.firstname + ',' + studentDisplay.course + ',' + studentDisplay.level)
			writer.close()

		print("Student Updated!")
	else:
		print("Student Not Found!")

def displayAllStudent()->None:
	header("Display All Student")
	#must check if file to be opened is existing
	f = open(filename)
	slist = f.readlines()
	f.close()
	for s in slist:
		print(s,end="")
	print("---------------------------")
	print("Nothing follows")
	
def quit()->None:
	header("Program Terminated")

def readerFile()->dict:
	studentDict = dict()
	with open(filename, 'r') as file:
		line = file.readline()
		while line:
			data: str = line
			newData: list = data.split(",")
			if len(newData) >= 5:
				stud = Student(newData[0], newData[1], newData[2], newData[3], newData[4])
				studentDict[newData[0]] = stud
			line = file.readline()

	return studentDict

