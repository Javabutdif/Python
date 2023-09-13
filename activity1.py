"""
	Name :<ANTON JAMES J. GENABIO>
	Lab Schedule:<9:00 AM - 10:30 AM MW>
	
	Create a python program that would accept two(2)
	integers not greater 10 and not less than 0,(1 to 10 only),
	each inputted value respectively represents the row and the 
	column value of the size of a multiplication table matrix
	example:
		row : 5
		column : 5
		
		output :
		1  2  3  4  5
		2  4  6  8 10
		3  6  9 12 15
		4  8 12 16 20
		5 10 15 20 25
"""


def main()->None:

	
	
	
		row = int(input("Enter row: "))
		col = int(input("Enter col: "))
		
		if row > 0 and row <= 10 and col > 0 and col <= 10:
		
			for i in range (1,row+1):
				out = i
				
				for j in range (1,col+1):
					if i == 1:
						print(f"%4d"% out , end="")
						out+=1
					else:
						
						print(f"%4d"% out,end="")
						out = out + i
					
				
					
						
					
					
				print()
		else:
			print("Number exceed!")



if __name__=="__main__":
	main()