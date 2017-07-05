n = int(input())
array = list(map(int,input().strip().split(' ')))
day,month = map(int,input().split())
length = len(array)
counter = summation = 0

for n in range(length):
    for m in range(month):
        if n+m >= length:
            break
        else:
            summation += array[n+m]
    if summation == day:
        counter += 1
    summation = 0
print(counter)
