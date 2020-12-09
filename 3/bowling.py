spieler = int(input("Anzahl Spieler: "))
runden = int(input("Anzahl Runden: "))

resultate = []

for i, _ in enumerate(range(0, spieler), start=1):
    print("Spieler " + str(i))
    scores = []
    for i, _ in enumerate(range(0, runden), start=1):
        print("Runde " + str(i))
        scores.append(int(input("Wert: ")))
    resultate.append(scores)

summe = {}
for i, resultat in enumerate(resultate, start=1):
    summe["Spieler " + str(i)] = sum(resultat)

print("--------RESULTATE--------")
for s in summe:
    print(s + " Punkte: " + str(summe[s]))
