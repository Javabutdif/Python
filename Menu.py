
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
		
	
#Display
def display() -> None :
	system("cls")
	
	menu: list = [
	"======== Menu ========",
	"1. Multiplication",
	"2. Division",
	"3. Addition",
	"4. Subtraction",
	"5. Quit/End",
	"======================"
		
	]
	
	for menuItem in menu:
		print(menuItem)
	
	option: int = 999
	
	while option != 5 :
		option = int(input("Enter option: "))
		
		if option == 0 :
			print("Program terminated")
		elif option == 1 : 
			num1,num2 = acceptInput()
			print("The product of %d and %d is %d" % (num1,num2,multiply(num1,num2))+"\n")
		elif option == 2:
			num1,num2 = acceptInput()
			print("The quotient of %d and %d is %f" % (num1,num2,divide(num1,num2))+"\n")
		elif option == 3:
			num1,num2 = acceptInput()
			print("The sum of %d and %d is %d" % (num1,num2,sum(num1,num2))+"\n")
		elif option == 4:
			num1,num2 = acceptInput()
			print("The difference of %d and %d is %d" % (num1,num2,subtract(num1,num2))+"\n")

if __name__ == "__main__":
	main()