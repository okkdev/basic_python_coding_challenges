grades = []

grade = float(input("Erste Note: "))

while 1:
    if grade == 0:
        print("Durchschnitt: " + str(sum(grades) / len(grades)))
        break
    elif grade > 6 or grade < 1:
        print(str(grade) + " ist keine valide Note!")
    else:
        grades.append(grade)
        print("Zur Berechnung des Durchschnitts geben Sie 0 ein!")

    grade = float(input("Weitere Note: "))