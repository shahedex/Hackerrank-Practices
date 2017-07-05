n = int(input())
array = list(map(int,input().strip().split(' ')))
tallest = max(array)
counter = 0
for i in array:
    if i == tallest:
        counter += 1
print(counter)
