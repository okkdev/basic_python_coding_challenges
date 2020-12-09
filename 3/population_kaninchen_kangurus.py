Kan = 50
Kae = 10
vkan = 50
vkae = 10
a = 5
laenge = 20

NKan = [2]
NKae = [5]
ZKan = []
ZKae = []

for i in range(0, laenge):
    ZKan.append((vkan / 100) * NKan[i] * ((Kan - NKan[i] - NKae[i] * a) / Kan))
    ZKae.append((vkae / 100) * NKae[i] * ((Kae - NKan[i] / a - NKae[i]) / Kae))
    NKan.append(NKan[i] + ZKan[i])
    NKae.append(NKae[i] + ZKae[i])

print("--------------------")
print("Kaninchen: ")
for i in range(0, laenge):
    print("Anzahl:\t", str(NKan[i]), "\tZuwachs:\t", str(ZKan[i]))
print("--------------------")

print("--------------------")
print("Kängurus: ")
for i in range(0, laenge):
    print("Anzahl:\t", str(NKae[i]), "\tZuwachs:\t", str(ZKae[i]))
print("--------------------")