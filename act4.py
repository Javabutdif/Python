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

def display()->None:
	
	disp : list = (
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


def addStud()->None:
	print("this is add method")
def findStud()->None:pass	
def deleteStud()->None:pass	
def updateStud()->None:pass	
def displayStud()->None:
    file = open("students.txt")
    
    print(file.read)
def end()->None:pass

def readFile()->None:
    file = open("students.txt")
    studentDict = dict()
    
    for x in file:
        data : str = file.readline()
        newData : list = data.split(",")
        stud = Student(newData[0],newData[1],newData[2],newData[3],newData[4])
    
        studentDict[newData[0]] = stud
    
    for i in studentDict:
        studentDisplay = i
        print("Id#: "+ studentDisplay.idNum +"\nLast Name: " + studentDisplay.lastName +"\nFirst Name: "+studentDisplay.firstName+"\nCourse: "+studentDisplay.course+"\nYear Level: "+studentDisplay.yearLevel)
        


class Student:
    def __init__ (self,idNum,lastName, firstName,course,yearLevel):
        self.idNum = idNum
        self.lastName = lastName
        self.firstName = firstName
        self.course = course
        self.yearLevel = yearLevel
        
    
        
  
	


def choices(i)->str:
	ch : dict = {
		1 : addStud,
		2 : findStud,
		3 : deleteStud,
		4 : updateStud,
		5 : displayStud,
		0 : end,
	}
	
	return ch.get(i)

 
   
    
    


def main()->None:
	system("cls")
	
    
	readFile()
"""
	displayStud()
	display()
	opt = int(input("Enter Option(0..5): "))
	choices(opt)()
"""
	
	
	
	
	


if __name__ == "__main__":
	main()