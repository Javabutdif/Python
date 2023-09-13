"""
<Anton James J. Genabio>
<MW 9:00 - 10:30 AM>

Create a python that would multiply two(2) integer matrix
requirement , row of the 1st of the matrix should have the same
size of the column of the 2nd matrix.
Result should be displayed in matrix similar to the multiplication table activity
matrix A(rxc)       matrix B(rxc)
1 2 3                   5 4 3
4 5 6                   1 2 6
7 8 9                   7 9 8
https://www.mathsisfun.com/algebra/matrix-multiplying.html
"""

from os import system


def main()-> None:
	system("cls")
	
	n: int = 0
	b: int = 0
	matrixA: int = [1,2,3,4,5,6,7,8,9]
	matrixB: int = [5,4,3,1,2,6,7,9,8]
	
	print("Matrix A")
	for i in range(n,len(matrixA)):
		if n < len(matrixA):
			for j in range(0,3):
				print(matrixA[n],end=" ")
			
				n += 1
			print("")
	

	print("\nMatrix B")
	
	for i in range(b,len(matrixB)):
		if b < len(matrixB):
			for j in range(0,3):
				print(matrixB[b],end=" ")
			
				b += 1
			print("")
	number: int = 0
	n = 0
	b = 0
	
	output: str = ""
	
	print("")
	
	for i in range(0, (len(matrixA)+len(matrixB))):
		if n < len(matrixA) and n < len(matrixB) :
			for j in range (0,3):
				if n < 3 :
					number += (matrixA[n] * matrixB[n*3])
					
				n+= 1
			output += str(number) + " "
			
			
	
	print(output)



if __name__ =="__main__":
	main()