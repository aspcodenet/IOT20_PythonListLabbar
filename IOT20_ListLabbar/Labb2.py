allNumbers = []
nrOfInputs = int(input("Hur många tal?"))
for num in range(0,nrOfInputs):
    print(f"Mata in tal nummer:{num+1}:")     
    number = int(input())
    allNumbers.append(number)

biggestSoFar = allNumbers[0]
for num in allNumbers:
    if(num > biggestSoFar):
        biggestSoFar = num

print(f"Biggest so far {biggestSoFar}")
