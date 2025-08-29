#string is immutable so all the changes are temporary
a = "Harsh"
print(a)

print(a.upper())                    #capital everthing
print(a.lower())                    #lower case erthng

b = " Praise Fly* Praise Stove* Praise God !!!   "
print(b.strip())                    #removes white space b4 and after the string

c = "Harambe !!!"
print(c.rstrip("!"))                #removes trailing character from string

print(b.replace("God","Me")) #replace a word from string
print(b.split("*"))                 #splits string for a mentioned character

print(b.capitalize())               #capitalizes first charac in string else lc //1st is space here so not working

print(b.count("Praise"))            #how many times charac appears

print(c.endswith("!"))              #checks if string ends with given charac

print(b.find("Praise"))             #finds FIRST occurance
print(b.find("Stove"))
print(b.find("Me"))
print(b.find("Praise"))             #same as find() but if word not found it will give error stead of -1

print(b.title())                    #capital first letter of each word

print(b.islower())                  #tells if string is in lower case or not

