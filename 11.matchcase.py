# this is the same as switch in c and java

x = int(input("Enter a number between 1-3 : "))

match x:
    case 1:
        print("Number is 0")
    case 2:
        print("Number is 2")
    case 3:
        print("Number is 3")
    case _:
        print("Number is not between 1 and 3")