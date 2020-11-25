cipher_input = input("Wort? ")
cipher_key = int(input("Schlüssel? "))

cipher_chars = list(cipher_input)

cipher = ""

for char in cipher_chars:
    if char.isspace():
        cipher += " "
    else:
        cipher += chr(ord(char) - cipher_key)


print(cipher_input + " wird zu " + cipher)
