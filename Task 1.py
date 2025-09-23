amount = float(input("Amount: "))
vat = float(input("VAT %: "))
total = amount + (amount * vat / 100)
print("TOTAL:", total)