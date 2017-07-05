size = int(input())
mat = [[int(i) for i in input().strip().split(' ')] for j in range(size)]
sumOne = 0
sumTwo = 0
counter = size-1

for x in range(size):
    for y in range(size):
        if x == y:
            sumOne += mat[x][y]
            sumTwo += mat[x][counter]
            counter -= 1
print(abs(sumOne-sumTwo))
