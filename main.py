

"""
	A program that accepts 2 integer values 
	and display the sum, product and the quotient of the inputed value
"""
from os import system



def main(): 
	system("cls")
	
	a = int(input("Input first value: "))
	b = int(input("Input second value: "))
	sum = a + b
	product = a * b
	qou = a / b 
	
	print(f"The sum of %d and %d is %d" % (a,b,sum))
	print(f"The sum of %d and %d is %d" % (a,b,(a*b)))
	print(f"The sum of %d and %d is %f" % (a,b,qou))

#main trigger
if __name__=="__main__":
	main()