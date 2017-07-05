def solve(a0,a1,a2,b0,b1,b2):
    alice = 0
    bob = 0
    aPoint = [a0,a1,a2]
    bPoint = [b0,b1,b2]

    for i in range(3):
        if aPoint[i] > bPoint[i]:
            alice += 1
        elif aPoint[i] < bPoint[i]:
            bob += 1
    return alice,bob


a0,a1,a2 = map(int,input().strip().split(' '))
b0,b1,b2 = map(int,input().strip().split(' '))

alice,bob = solve(a0,a1,a2,b0,b1,b2)
print(str(alice) + " " + str(bob))

