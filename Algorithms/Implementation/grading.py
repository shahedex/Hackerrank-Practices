size = int(input())
array = []
for i in range(size):
    array.append(int(input()))

for num in array:
    count = 0
    n = num
    if num <38:
        print(num)
        continue
    for i in range(3):
        num += i
        if num%5 == 0:
            print(num)
            count += 1
            break
        num = n
    if count == 0:
        print(n)
