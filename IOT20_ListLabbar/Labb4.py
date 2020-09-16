
allMeasurements = []
nrOfInputs = int(input("Hur många mätningar?"))
for num in range(0,nrOfInputs):
    print(f"Mata in mätning nummer:{num+1}:")     
    number = float(input())
    allMeasurements.append(number)

for measurement in allMeasurements:
    print(measurement)

maxMeasure = allMeasurements[0]
for measurement in allMeasurements:
    if(measurement > maxMeasure):
        maxMeasure = measurement
print(f"Max {maxMeasure}")

sum = 0
for measurement in allMeasurements:
    sum = sum + measurement
print(f"Avg {sum / nrOfInputs}")

