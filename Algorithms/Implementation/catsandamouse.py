n = int(input())

for i in range(n):
    a,b,c = map(int,input().strip().split(' '))
    dista = abs(c-a)
    distb = abs(c-b)
    if dista<distb:
        print('Cat A')
    elif distb<dista:
        print('Cat B')
    else:
        print('Mouse C')
