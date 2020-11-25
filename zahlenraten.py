import random

num = random.randint(1, 100)
tries = 0

while 1:
    tries += 1
    i = int(input("Geben Sie eine Ganzzahl zwischen 1 und 100 ein! "))
    if i > 100 or i < 1:
        print(str(i) + " liegt nicht zwischen 1 und 100...")
    elif i == num:
        print("erraten!")
        print(str(tries) + " Mal geraten")
        break
    elif i < num:
        print("zu klein")
    elif i > num:
        print("zu gross")
