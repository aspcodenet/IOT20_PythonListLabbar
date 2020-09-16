
nrOfInputs = int(input("Hur många produkter?"))
allaNamn = []
allaPris = []
allaNum = []
for num in range(0,nrOfInputs):
    print(f"Data för produkt {num+1}:")
    namn = input(" Namn:")
    pris = int(input(" Pris:"))
    num = int(input(" Produktnummer:"))
    allaNamn.append(namn)
    allaPris.append(pris)
    allaNum.append(num)

for index in range(0,nrOfInputs):
    print(f"{allaNum[index]} {allaNamn[index]} {allaPris[index]}")


