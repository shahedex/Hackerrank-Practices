s,t = map(int,input().split())
a,b = map(int,input().split())
m,n = map(int,input().split())
apples = list(map(int,input().strip().split(' ')))
oranges = list(map(int,input().strip().split(' ')))
appleCounter = 0
orangeCounter = 0

for apple in apples:
    dist = a+apple
    if dist >= s and dist <= t:
        appleCounter += 1
for orange in oranges:
    dist = b+orange
    if dist >= s and dist <= t:
        orangeCounter += 1
print(appleCounter)
print(orangeCounter)
