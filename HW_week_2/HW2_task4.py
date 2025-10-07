import random

numbers = []
i = 0
while i < 20:
    numbers.append(random.randint(1, 100))
    i = i + 1

print("Numbers:", numbers)

count = 0
for n in numbers:
    if n % 2 == 0:
        count = count + 1

print("Even numbers count:", count)