spieler = int(input("Anzahl Spieler: "))
runden = int(input("Anzahl Runden: "))

resultate = []

for i in range(1, spieler + 1):
    print("Spieler " + str(i))
    score = 0
    for i in range(1, runden + 1):
        print("Runde " + str(i))
        score += int(input("Wert: "))
    resultate.append(score)

print("--------RESULTATE--------")
for i, resultat in enumerate(resultate, start=1):
    print("Spieler ", i, " Punkte: ", resultat)
