sentence = input("Enter a sentence: ")
letter = input("Enter a letter: ")
count = 0
for ch in sentence:
    if ch == letter:
        count += 1
print("The letter", letter, "appears", count, "times.")