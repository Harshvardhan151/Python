name = 'Harshvardhan'

for i in name:
    print(i,end=",")

print("\n")

colors = ['red', 'green', 'blue']

for color in colors:
    print(color)
    if(color == 'red'):
        for i in color:
            print(i)

for x in range(6) :
    print(x, end="~")

print("\n")

for h in range(1,4) :
    print(h,end="")
print("\n")
# step in range is like increment & decrement syntax:(start,stop,range)

for pbc in range(9,91,9) :
    print(pbc,end=",")