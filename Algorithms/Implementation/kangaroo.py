x1,v1,x2,v2 = map(int,input().split())
x1dist = x1
x2dist = x2
lstdist = []
counter = 0

while True:
    x1dist += v1
    x2dist += v2
    if x1dist >= x2dist:
        diff = x1dist - x2dist
    elif x1dist < x2dist:
        diff = x2dist - x1dist
    lstdist.append(diff)
    if len(lstdist)>1:
        if lstdist[len(lstdist)-1] > lstdist[len(lstdist)-2] or lstdist[len(lstdist)-1] ==  lstdist[len(lstdist)-2]:
            counter += 1
    if diff == 0:
        print('YES')
        break
    elif diff < 0 or counter > 3:
        print('NO')
        break
