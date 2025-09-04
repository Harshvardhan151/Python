#def is used to define a function

def calulateGmean(a,b):
    gmean = (a*b)/(a+b)
    print("Geometric mean = ",gmean)

def isGreater(a,b):
    if(a>b):
        print("First number is greater than second number")
    elif(a<b):
        print("Second number is greater than first number")
    else:
        print("First number is equal to the second number")

def isLesser(a,b):
    pass                #you can do it later

x = int(input("Enter 1st number: "))
y = int(input("Enter 2nd number: "))

calulateGmean(x,y)
isGreater(x,y)

