colors = ["Red", "Green", "White", "Blue", "Violet"]

i = 0
found = False
while i < len(colors):
    if colors[i] == input("Enter a color: "):
        found = True
    i = i + 1

if found:
    print("Yes, the car is available in this color")
else:
    print("Sorry, the car is not available in this color")