import random

numbers = []
i = 0
while i < 100:
    numbers.append(random.randint(1, 50))
    i = i + 1

print("Numbers:", numbers)

target = int(input("Enter a number to search (1-50): "))

count = 0
for n in numbers:
    if n == target:
        count = count + 1

print("The number", target, "appears", count, "times.")