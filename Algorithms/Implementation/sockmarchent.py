n = int(input())
socks = list(map(int,input().strip().split(' ')))
check = set(socks)
counter = count = 0

for num in check:
    for checknum in socks:
        if checknum == num:
            counter += 1
    count += int(counter/2)
    counter = 0
print(count)
