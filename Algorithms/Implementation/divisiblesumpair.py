n,k = map(int,input().split())
array = list(map(int,input().strip().split()))
length = len(array)
summation = counter = 0

for i in range(length):
    for j in range(i+1,length):
        summation = array[i] + array[j]
        if summation%k == 0:
            counter += 1
        summation = 0
print(counter)
