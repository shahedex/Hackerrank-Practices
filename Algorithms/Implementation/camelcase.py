string = input()
counter = 1

for s in string:
    if ord(s) >= 65 and ord(s) <= 90:
        counter += 1
print(counter)
