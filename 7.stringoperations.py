fruit = 'apple'

print(len(fruit))       #prints the length of string

#slicing a string
print(fruit[0:4])       #from 0 to 4-1
print(fruit[:4])        #same as above line; if theres nothing, python assumes 0

print(fruit[2:4])

print(fruit[0:-2])      #-2 means len(fruit)-2 ie 3
print(fruit[0:len(fruit)-2])    #same as above
