size = int(input())
array = [int(i) for i in input().strip().split(' ')]
arrayLength = len(array)
positive=negative=zero=0

for x in array:
    if x > 0:
        positive += 1
    elif x < 0:
        negative += 1
    else:
        zero += 1

pos = (positive/arrayLength)
neg = (negative/arrayLength)
zer = (zero/arrayLength)
print(pos)
print(neg)
print(zer)
