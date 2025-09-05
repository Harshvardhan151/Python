marks = [4,6,8]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1],"\n")

#negative indexing

print(marks[-2])
print(marks[len(marks)-2])
print(marks[1])

#list can have any datatype and different type of data types at once

list = [227,"Motor City",False]
print(list)

#jump index is the no of index to skip; 3rd arg in the syntax

print("\n")
numero = [1,2,3,4,5,6,7,8,9,10,11,12]
print(numero[1:12])
print(numero[1:11:2])

#check for element in a list

if 227 in list:
    print("yes")
else:
    print("no")

if 227 in numero:
    print("yes")
else:
    print("no")