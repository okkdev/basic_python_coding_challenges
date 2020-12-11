spieler = int(input("Anzahl Spieler: "))
runden = int(input("Anzahl Runden: "))

resultate = []

for i in range(1, spieler + 1):
    print("Spieler ", i)
    scores = []
    for i in range(1, runden + 1):
        print("Runde ", i)
        scores.append(int(input("Wert: ")))
    resultate.append(scores)

print("--------RESULTATE--------")
for i, scores in enumerate(resultate, start=1):
    print("Spieler ", i, " Punkte: ", sum(scores))