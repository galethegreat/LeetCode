def printMove(fro, to):
    print(f'Move from {str(fro)} to {str(to)}')

def towers(Tower_A,Tower_B,Tower_C,num_of_cylinders):
    if num_of_cylinders == 1:
        printMove(Tower_A, Tower_B)
    else:
        towers(Tower_A, Tower_C, Tower_B, num_of_cylinders-1)
        towers(Tower_A, Tower_B, Tower_C, 1)
        towers(Tower_C, Tower_B, Tower_A, num_of_cylinders-1)

n = int(input("Input number of cylinders: "))
a,b,c = 'a','b','c'
towers(a,b,c,n)
