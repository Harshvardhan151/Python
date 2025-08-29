#strings in python

a = "Harsh"
# triple """ or ''' are used to print string as it is with eol and allat
b = """The Mayor's a cop,
the blues quadrupled up"""
c = 'i want an apple'

print(a)
print(b)
print(c)

#in python str **ACTS** like an array
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])

print("\ndoing the same now but with a loop\n")
for character in a:
    print(character)