K = 50
v = 50
laenge = 30

N = [2]

for i in range(0, laenge):
    N.append(N[i] + (v / 100) * N[i] * ((K - N[i]) / K))

print("Kaninchen Anzahl:")
print(N)
