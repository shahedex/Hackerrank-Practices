s,n,m = map(int,input().strip().split(' '))
keyboards = list(map(int,input().strip().split(' ')))
drives = list(map(int,input().strip().split(' ')))
totalMoney =  0
spent = -199

for keyboard in keyboards:
    for drive in drives:
        totalMoney = keyboard + drive
        if totalMoney > spent and totalMoney <= s:
            spent = totalMoney
if spent < 0:
    print('-1')
else:
    print(spent)
