# Skapa ett program där användaren får upp fyra frågor 
# om att mata in ett tal. Spara alla talen i en array. 
# Loopa igenom arrayen och ta fram det tal som är störst. 
# Skriv tillbaka resultatet på skärmen för användaren. 
allNumbers = []
for num in range(0,4):
    print(f"Mata in tal nummer:{num+1}:")     
    number = int(input())
    allNumbers.append(number)

biggestSoFar = allNumbers[0]
for num in allNumbers:
    if(num > biggestSoFar):
        biggestSoFar = num

print(f"Biggest so far {biggestSoFar}")
