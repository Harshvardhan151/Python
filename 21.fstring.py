# f-string is used for string formatting

# how string formatting is normally done in python
print("by normal string formating:")
str1 = "Hi my name is {1} and i am from {0}"
country = "India"
name = "Harshvardhan"
print(str1.format(country,name))

print("\nby f-string formating:")
print(f"Hi my name is {name} and i am from {country}")
print("How it actually looks:")
print(f"Hi my name is {{name}} and i am from {{country}}")

price = 49.0909987
txt = f"\nGet this limited edition casette for just {price:.2f}"
print(txt)

print("\n{2*3}")
print(f"{2*3}")
