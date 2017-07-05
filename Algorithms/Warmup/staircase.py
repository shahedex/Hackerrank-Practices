size = int(input())

for i in range(size):
    for j in range(size-1,-1,-1):
        if j<=i:
            print("#",end='')
        else:
            print(" ",end='')
    print()

