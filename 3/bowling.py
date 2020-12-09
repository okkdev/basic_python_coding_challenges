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

print("--------RESULTATE--------")
for i, resultat in enumerate(resultate, start=1):
    print("Spieler " + str(i) + " Punkte: " + str(sum(resultat)))
