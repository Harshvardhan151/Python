# 4 types of arguments in python  :  1.default     2.keyword     3.required      4.variable length

#1.default arguments -- arguments have predefined value

def sum(a=2,b=3):
    return a+b

print(sum())

#2.keyword arguments -- reqd args if not provided will give error

def avg(a,b,c):
    return (a+b+c)/3

print(avg(1,2,3))
print(avg(1,2, c=3))    #remove the c to see the error


def name(fname, mname="raymone", lname="james"):
    print("Hello" ,fname, mname, lname)

name("lebron")