allNumbers = [1,55,4,2,5]
for index in range(0,5):
    if allNumbers[index]  % 2 == 1:
        allNumbers[index] = 0

for num in allNumbers:
    print(num)


