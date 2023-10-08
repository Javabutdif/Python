"""
	<name>
	<schedule>
	<edpcode>
"""

from api import *
from pathlib import Path

def displaymenu()->None:
	header("     Main Menu     ")
	menuitems:tuple = (
		"1. Add Student",
		"2. Find Student",
		"3. Delete  Student",
		"4. Update Student",
		"5. Display All Student",
		"0. Quit/End",
	)
	[print(menu) for menu in menuitems]


def main()->None:
    path:str = Path('student.csv')
    if path.is_file() == False:
        f = open("student.csv", "x")
    menuoptions:dict = {
		1:addStudent,
		2:findStudent,
		3:deleteStudent,
		4:updateStudent,
		5:displayAllStudent,
		0:quit,
    }
    option:int = -1
    while option != 0:
        displaymenu()
        option = int(input("Enter Option (0...5):"))
        selected_option = menuoptions.get(option,"invalid")
        if selected_option!= "invalid":
            selected_option()
        else:
            print("Invalid Option")
        input("Press any key to continue...")
		
if __name__=="__main__":
	main()
		