year = int(input())
totalday = 256
leapday = 244
normalday = 243
day = 0

if year == 1918:
    normalday = 243-13
    day = totalday - normalday
elif (year<1918 and year%4==0) or ((year%400==0) or (year%4== 0 and year%100!=0)):
    day = totalday - leapday
else:
    day = totalday - normalday
print(str(day)+'.09.'+str(year))
