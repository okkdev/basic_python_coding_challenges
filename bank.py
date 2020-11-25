def calculate_money(amount, note):
    print(str(note) + "er: " + str(int(amount / note)))
    return amount % note


print("Willkommen bei der Bank Ihres Vertrauens")
print("****************************************")

withdraw_amount = int(input("Wieviel möchten Sie abheben? "))

print("Eingegebener Geldbetrag: " + str(withdraw_amount) + " Fr.")

if withdraw_amount < 10:
    print("Wählen Sie einen höheren Betrag")
else:
    print("Bitte warten...")

    remainder = calculate_money(
        calculate_money(calculate_money(calculate_money(withdraw_amount, 100), 50), 20),
        10,
    )

    print("Rest: " + str(remainder))