# tuples are immutable so you cant make changes // to make changes convert it to a list

countries = ("Brazil","Russia","India","China")
temp = list(countries)
print(temp)
temp.append("South Africa")
print(temp)
temp.pop(2)
print(temp)
temp[2] = "Japan"
print(temp)
countries = tuple(temp)
print(countries)

# methods in tuple

marks = (41,67,41,67,41,67)
print(marks.count(41))

