array = list(map(int,input().strip().split(' ')))
array.sort()
minSum=maxSum=0

for i in array:
    minSum += i
    maxSum += i

minSum -= array[len(array)-1]
maxSum -= array[0]
print(str(minSum)+" "+str(maxSum))

