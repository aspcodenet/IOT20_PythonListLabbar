
allaNamn = []
allaStreet = []
allaPostnr = []
allaPostOrt = []


for num in range(0,5):
    print(f"Data för person {num+1}:")
    namn = input(" Namn:")
    street = input(" Gata:")
    postnr = input(" Postnummer:")
    postort = input(" Postort:")
    allaNamn.append(namn)
    allaStreet.append(street)
    allaPostnr.append(postnr)
    allaPostOrt.append(postort)
    if input("Mata in en till J/N?") == "N":
        break

for index in range(0,len(allaNamn)):
    print(f"{allaNamn[index]} {allaStreet[index]} {allaPostnr[index]} {allaPostOrt[index]}")


