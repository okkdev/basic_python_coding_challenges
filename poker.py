# Test hand
# hand_dict = {
#     "1": {"wert": 12, "farbe": 2},
#     "2": {"wert": 11, "farbe": 2},
#     "3": {"wert": 10, "farbe": 2},
#     "4": {"wert": 9, "farbe": 2},
#     "5": {"wert": 7, "farbe": 2},
# }
hand_dict = {}

print("*********")
print("P O K E R")
print("*********")
print("EINGABE IHRER KARTEN")
print("Geben Sie Ihre Karten ein: ")
print()
for i in range(1, 6):
    karte = {}
    karte["wert"] = int(input(str(i) + ". Wert: "))
    karte["farbe"] = int(input(str(i) + ". Farbe: "))
    hand_dict[str(i)] = karte
print()
print("Sie haben eingegeben: ")
for karte in hand_dict:
    print(
        "Karte " + str(karte) + " (Wert|Farbe): ",
        hand_dict[karte]["wert"],
        hand_dict[karte]["farbe"],
    )

# Bewertung der Hand


# Check functions


# extract all values from hand to list
def create_list(hand, value):
    return [hand[k][value] for k in hand]


def check_flush(hand):
    farben = create_list(hand, "farbe")
    if len(set(farben)) == 1:
        return True
    else:
        return False


def check_straight(hand):
    werte = create_list(hand, "wert")
    if sorted(werte) == list(range(min(werte), max(werte) + 1)):
        return True
    else:
        return False


def check_straight_flush(hand):
    if check_flush(hand) and check_straight(hand):
        return True
    else:
        return False


def check_royal_flush(hand):
    werte = create_list(hand, "wert")
    if check_flush(hand) and check_straight(hand) and max(werte) == 14:
        return True
    else:
        return False


def get_pairs(hand):
    werte = create_list(hand, "wert")
    # create dictionary
    pairs = {"two": 0, "three": 0, "four": 0}
    # loop through all available werte and count how many times they appear
    for w in set(werte):
        if werte.count(w) == 2:
            pairs["two"] += 1
        elif werte.count(w) == 3:
            pairs["three"] += 1
        elif werte.count(w) == 4:
            pairs["four"] += 1

    return pairs


def check_pair(hand):
    if get_pairs(hand)["two"] == 1:
        return True
    else:
        return False


def check_two_pair(hand):
    if get_pairs(hand)["two"] == 2:
        return True
    else:
        return False


def check_three_kind(hand):
    if get_pairs(hand)["three"] == 1:
        return True
    else:
        return False


def check_four_kind(hand):
    if get_pairs(hand)["four"] == 1:
        return True
    else:
        return False


def check_full_house(hand):
    if get_pairs(hand)["three"] == 1 and get_pairs(hand)["two"] == 1:
        return True
    else:
        return False


# Checks

if check_royal_flush(hand_dict):
    print("ROYAL FLUSH")
elif check_straight_flush(hand_dict):
    print("STRAIGHT FLUSH")
elif check_four_kind(hand_dict):
    print("FOUR OF A KIND")
elif check_full_house(hand_dict):
    print("FULL HOUSE")
elif check_flush(hand_dict):
    print("FLUSH")
elif check_straight(hand_dict):
    print("STRAIGHT")
elif check_three_kind(hand_dict):
    print("THREE OF A KIND")
elif check_two_pair(hand_dict):
    print("TWO PAIRS")
elif check_pair(hand_dict):
    print("ONE PAIR")
else:
    print("Sie haben nichts.")
