tup = (1,5,8,"green",False)
print(type(tup),tup)

singletup = (1,)    #even if single value followit with ,

# you cannot make changes in tuple  ie   tuples are immutable

print(tup[2])
print(len(tup))

if 8 in tup:
    print("yes")
else:
    print("no")

# if red in tup:
#     print("yes")
# else:
#     print("no")

tup2 = tup[1:4] #tuple slicing
print(tup2)