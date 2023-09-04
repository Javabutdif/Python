
"""
	Create a program that will display a menu
	======== Menu ========
	1. Multiplication
	2. Division
	3. Addition
	4. Subtraction
	5. Quit/End
	======================
	
	Enter Option (0-4)
	Add function to each option using a module
	for each operation
"""
#import necessary packages 
from os import system


def main():
	display()




#Calculate Values

def multiply(num1:int , num2:int)->int : 
	return num1*num2
	
def divide(num1:int , num2:int)->float : 
	return num1/num2
	
def sum(num1:int , num2:int)->int : 
	return num1+num2
	
def subtract(num1:int , num2:int)->int : 
	return num1-num2
	
#Display Option
def acceptInput()->int:
	num1, num2 = int(input("Enter num1: ")) , int(input("Enter num2: "))
	
	return num1,num2

def quit()-> None:
	print("Program terminated")


#Display
def display() -> None :
	system("cls")
	

	menu: list = [
	"======== Menu ========",
	"1. Multiplication",
	"2. Division",
	"3. Addition",
	"4. Subtraction",
	"0. Quit/End",
	"======================"
		
	]
	menuDict : dict = {
	1: multiply,
	2: divide,
	3: sum,
	4: subtract,
	0: quit,
	
}
	for menuItem in menu:
		print(menuItem)
	
	

	
	
	
	option: int = 999
	
	while option != 0 :
		option = int(input("Enter option: "))
		
		if option == 0 :
			system("cls")
			
		elif option == 1 : 
			system("cls")
			print("Multiply 2 numbers\n")
			num1,num2 = acceptInput()
			print("The product of %d and %d is %d" % (num1,num2,menuDict.get(option)(num1,num2))+"\n")
		elif option == 2:
			system("cls")
			print("Divide 2 numbers\n")
			num1,num2 = acceptInput()
			print("The quotient of %d and %d is %f" % (num1,num2,menuDict.get(option)(num1,num2))+"\n")
		elif option == 3:
			system("cls")
			print("Add 2 numbers\n")
			num1,num2 = acceptInput()
			print("The sum of %d and %d is %d" % (num1,num2,menuDict.get(option)(num1,num2))+"\n")
		elif option == 4:
			system("cls")
			print("Subtract 2 numbers\n")
			num1,num2 = acceptInput()
			print("The difference of %d and %d is %d" % (num1,num2,menuDict.get(option)(num1,num2))+"\n")
		
		for menuItem in menu:
			print(menuItem)
		
		
if __name__ == "__main__":
	main()