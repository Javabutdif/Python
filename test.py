


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
    matrixA: list = [[1,2,3],[4,5,6],[7,8,9]]
    matrixB: list = [[5,4,3],[1,2,6],[7,9,8]]
    
    print("MatrixA")
    for arrA in matrixA:
        nums: str = "["
        for num in arrA:
            nums += str(num) + ", "
        print(nums+"],")
    
    print("MatrixB")
    for arrB in matrixB:
        nums: str = "["
        for num in arrB:
            nums += str(num) + ", "
        print(nums+"],")
    
    Multiply(matrixA, matrixB)
    
def Multiply(mA, mB):
    print("\nMatrix Multiplication\n")
    
    
    for x in range(len(mA)):
        sum_all: str = "["
        for y in range(len(mA)):
            # matrix A index x
            mAB_sum: int = 0
            for j in range(len(mA[y])):
                
                mA_item: int = mA[x][j]
                
                # multiply in matrix B index X's
                mB_item: int = mB[j][y]
                
                mAB_sum += mA_item * mB_item
            sum_all += str(mAB_sum) + ", "
        print(str(sum_all) + "]")
    
    
if __name__ =="__main__":
    main()