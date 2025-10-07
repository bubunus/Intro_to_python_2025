num = int(input("Enter a number: "))

if num > 1:
    i = 2
    prime = True
    while i < num:
        if num % i == 0:
            prime = False
        i = i + 1
    if prime:
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")
else:
    print(num, "is  not a prime number")
