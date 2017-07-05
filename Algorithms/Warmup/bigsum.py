def aVeryBigSum(n,ar):
    summation = 0
    for i in range(n):
        summation += ar[i]
    return summation

n = int(input().strip())
array = list(map(int,input().strip().split(' ')))
result = aVeryBigSum(n,array)
print(result)
