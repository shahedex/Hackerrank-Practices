n = int(input())
array = list(map(int,input().strip().split()))
numarr = [1,2,3,4,5]
length = len(array)
counter = temp = flag= com = 0
array.sort()
for i in numarr:
    for j in range(flag,length):
        if array[j] == i:
            counter += 1
        elif array[j] > i:
            flag = j
            break
    if counter > temp:
        temp = counter
        com = i
    elif counter == temp:
        if array[j-1] < i:
            com = array[j-1]
    counter = 0
print(com)

