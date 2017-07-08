n = int(input())
p = int(input())

left = int(p/2)
right = int(n/2) - left

if left < right:
    print(left)
else:
    print(right)
