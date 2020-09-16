

allMeasurements = []
allDates = []
nrOfInputs = int(input("Hur många mätningar?"))
for num in range(0,nrOfInputs):
    print(f"*** Data för mätning nummer {num+1}")    

    print("    Datum")     
    dat= input()
    allDates.append(dat)

    print("    Temperatur")     
    number = float(input())
    allMeasurements.append(number)


for index in range(0,nrOfInputs):
    print(f"Datum:{allDates[index]} Värde:{allMeasurements[index]}")