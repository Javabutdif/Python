"""
    Activity#3
    <Anton James J. Genabio>
    <MW 9:00AM - 10:30AM>
	A program that would display a menu
	shown below
	------- Main Menu -------
	1. Add Name
	2. Find Name
	3. Delete Name
	4. Update Name
	5. Display All Names
	0. Quit/Exit
	-------------------------
	Enter Option(0..5):
	provide functionalities of the menu options
"""

from os import system

names: list = []


def displayMenu()->None:
	system("cls")
	
	display :tuple = (
		"------- Main Menu -------",
		"1. Add Name",
		"2. Find Name",
		"3. Delete Name",
		"4. Update Name",
		"5. Display All Names",
		"0. Quit/Exit",
		"-------------------------",
	)
	
	[print(displaymen) for displaymen in display]

	
def addName()->None:
	system("cls")
	add = input("Enter to add name: ")
	names.append(add)
	
	print(f"{add} is add on the list")
	input("Press any key to continue!")
	
	
	
def findName()->None:
	system("cls")
	found = input("Enter to find name: ")
	
	if found in names:
		print(f"{found} is found in the list")
	
	input("Press any key to continue!")
	

def deleteName()->None:
	system("cls")
	found = input("Enter to delete name: ")
	
	if found in names:
		print(f"{found} is found in the list!")
		choice= input(f"Do you want to delete {found}[Y/N]?: ")
		
		choice = choice.upper()
		if choice == "Y":
			names.remove(found)
			print(f"{found} is deleted in the list!")
			input("Press any key to continue!")
	else:
		print(f"{found} is not found in the list!")
	
def updateName()->None:
	system("cls")
	found = input("Enter to update name: ")
	
	if found in names:
		print(f"{found} is found in the list!")
		index:int = names.index(found)
		
		choice = input(f"Do you want to update {found}[Y/N]?: ")
		
		choice = choice.upper()
		if choice == 'Y':
			names.remove(found)
			newName = input("Input new name: ")
			names.append(newName)
			
			print(f"{found} is replace by {newName}")
			input("Press any key to continue!")
	else:
		print(f"{found} is not found in the list!")
			
			

def displayAllName()->None:
	system("cls")
	[print(name) for name in names]
	input("Press any key to continue!")
	
	
def terminate()->None:
	print("Program terminated")

def main()->None:
	system("cls")
	choices:int = -1
	
	menuItems : dict = {
	
		
		1:addName,
		2:findName,
		3:deleteName,
		4:updateName,
		5:displayAllName,
		0:terminate,
	
	}
	
	
	
	
	while choices != 0:
		displayMenu()
		choices = int(input("Enter choices(0..5): "))
		
		menuItems.get(choices)()
		
		
			
			

if __name__=="__main__":
	main()