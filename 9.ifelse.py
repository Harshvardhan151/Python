age = int(input("Enter your age: "))

if (age >= 18):
    print("You can drive")
else:
    print("You can't drive")

#elif

n = int(input("Enter a number: "))

if (n < 0):
    print("number is negative")
elif (n == 0):
    print("number is zero")
else:
    print("number is positive")

#nested if else

x = int(input("Enter a number: "))

if (x > 0):
    print("number is positive")
    if (0 > x > 10):
        print("number is between 0 and 10")
    else:
        print("number is greater than 10")
elif (x < 0):
    print("number is negative")
else:
    print("number is zero")