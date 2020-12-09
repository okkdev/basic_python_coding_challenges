# Pollendaten zeitlich sortiert
# Sorry black formatiert das so. Man sollte nicht so lange Listen hard coded haben.
pollen = [
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    2,
    0,
    2,
    0,
    0,
    4,
    2,
    2,
    2,
    2,
    0,
    2,
    0,
    0,
    2,
    12,
    2,
    4,
    16,
    10,
    88,
    24,
    88,
    78,
    320,
    220,
    72,
    80,
    104,
    146,
    106,
    44,
    14,
    8,
    0,
    2,
    22,
    312,
    142,
    56,
    88,
    202,
    242,
    194,
    86,
    194,
    126,
    48,
    26,
    60,
    28,
    30,
    12,
    14,
    24,
    22,
    76,
    22,
    12,
    8,
    24,
    22,
    8,
    6,
    56,
]
messzeitpunkte = [
    "01.03.2015",
    "02.03.2015",
    "03.03.2015",
    "04.03.2015",
    "05.03.2015",
    "06.03.2015",
    "07.03.2015",
    "08.03.2015",
    "09.03.2015",
    "10.03.2015",
    "11.03.2015",
    "12.03.2015",
    "13.03.2015",
    "14.03.2015",
    "15.03.2015",
    "16.03.2015",
    "17.03.2015",
    "18.03.2015",
    "19.03.2015",
    "20.03.2015",
    "21.03.2015",
    "22.03.2015",
    "23.03.2015",
    "24.03.2015",
    "25.03.2015",
    "26.03.2015",
    "27.03.2015",
    "28.03.2015",
    "29.03.2015",
    "30.03.2015",
    "31.03.2015",
    "01.04.2015",
    "02.04.2015",
    "03.04.2015",
    "04.04.2015",
    "05.04.2015",
    "06.04.2015",
    "07.04.2015",
    "08.04.2015",
    "09.04.2015",
    "10.04.2015",
    "11.04.2015",
    "12.04.2015",
    "13.04.2015",
    "14.04.2015",
    "15.04.2015",
    "16.04.2015",
    "17.04.2015",
    "18.04.2015",
    "19.04.2015",
    "20.04.2015",
    "21.04.2015",
    "22.04.2015",
    "23.04.2015",
    "24.04.2015",
    "25.04.2015",
    "26.04.2015",
    "27.04.2015",
    "28.04.2015",
    "29.04.2015",
    "30.04.2015",
    "01.05.2015",
    "02.05.2015",
    "03.05.2015",
    "04.05.2015",
    "05.05.2015",
    "06.05.2015",
    "07.05.2015",
    "08.05.2015",
    "09.05.2015",
    "10.05.2015",
    "11.05.2015",
    "12.05.2015",
    "13.05.2015",
    "14.05.2015",
    "15.05.2015",
    "16.05.2015",
    "17.05.2015",
    "18.05.2015",
    "19.05.2015",
    "20.05.2015",
    "21.05.2015",
    "22.05.2015",
    "23.05.2015",
    "24.05.2015",
    "25.05.2015",
    "26.05.2015",
    "27.05.2015",
    "28.05.2015",
    "29.05.2015",
    "30.05.2015",
    "31.05.2015",
    "01.06.2015",
    "02.06.2015",
    "03.06.2015",
    "04.06.2015",
    "05.06.2015",
    "06.06.2015",
    "07.06.2015",
    "08.06.2015",
    "09.06.2015",
    "10.06.2015",
    "11.06.2015",
    "12.06.2015",
    "13.06.2015",
    "14.06.2015",
    "15.06.2015",
    "16.06.2015",
    "17.06.2015",
    "18.06.2015",
    "19.06.2015",
    "20.06.2015",
    "21.06.2015",
    "22.06.2015",
    "23.06.2015",
    "24.06.2015",
    "25.06.2015",
    "26.06.2015",
    "27.06.2015",
    "28.06.2015",
    "29.06.2015",
    "30.06.2015",
]

# Ausgabe der unsortierte Liste
print(pollen)
# Bestimmung der Laenge des Arrays list
laenge = len(pollen)
print("Laenge: ", laenge)

# Suche nach dem Maxium

# Lineare Suche implementieren ist nicht nötig:
maximum = max(pollen)
index = pollen.index(maximum)
print("Maximum " + str(maximum))
print("Position " + str(index))
print("Maximum Datum " + messzeitpunkte[index])

# Lineare Suche
maximum = pollen[0]
index = 0
for i, value in enumerate(pollen):
    if value > maximum:
        maximum = value
        index = i

print("Maximum " + str(maximum))
print("Position " + str(index))
print("Maximum Datum " + messzeitpunkte[index])

# Suche Pollenwert 07.06.2015
print("Pollenwert vom 07.06.2015: " + str(pollen[messzeitpunkte.index("07.06.2015")]))
# nochmal aber mit Linearer Suche...
for i, value in enumerate(messzeitpunkte):
    if value == "07.06.2015":
        print("Pollenwert vom 07.06.2015: " + str(pollen[i]))


# Bubble Sort
def bubble_sort(list):
    # hack damit die pollen liste nicht mutiert wird
    list = list.copy()
    l = len(list)
    for i in range(l):
        for j in range(0, l - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]

    return list


# # Ausgabe sortierte Liste
print(bubble_sort(pollen))

pollen_mit_datum = [(pollen[i], messzeitpunkte[i]) for i in range(0, len(pollen))]
print(bubble_sort(pollen_mit_datum))
