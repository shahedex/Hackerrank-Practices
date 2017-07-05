string = input()
time =int(string[:2:])
notation = string[-2]
final = string[2:len(string)-2:]
pm = str(time+12)
if time == 12 and notation == 'A':
    print("00"+string[2:len(string)-2:])
elif time >= 1 and time <= 11 and notation == 'P':
    print(pm+final)
else:
    print(string[:len(string)-2:])
