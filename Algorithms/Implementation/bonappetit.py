n,k = map(int,input().split())
array = list(map(int,input().strip().split(' ')))
charged = int(input())
summation = 0

for i in range(len(array)):
    if i == k:
        continue
    summation += array[i]
summation = int(summation/2)
if summation == charged:
    print('Bon Appetit')
else:
    print(abs(charged-summation))
