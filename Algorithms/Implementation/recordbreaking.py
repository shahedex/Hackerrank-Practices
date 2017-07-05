n = int(input())
array = list(map(int,input().strip().split(' ')))
lowest=highest=array[0]
lowestcounter=highestcounter=0

for num in array:
    if num<lowest:
        lowest = num
        lowestcounter += 1
    elif num>highest:
        highest = num
        highestcounter += 1
print(str(highestcounter) + ' ' + str(lowestcounter))
