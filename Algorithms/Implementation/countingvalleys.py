n = int(input())
array = input()
count = counter = valley = 0

def opp(char):
    global counter
    if char == 'U':
        counter += 1
    else:
        counter -= 1

for char in array:
    opp(char)
    if counter <= 0:
        count = counter
        if count == 0 and char == 'U':
            valley += 1
print(valley)
