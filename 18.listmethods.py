list = [11,32,56,21,71]
print(list)

list.append(3)
print(list)

list.sort()
print(list)

list.reverse()
print(list)

l = [1,2,3,1,3,7,4,3]
print(l.index(3))       #returns first occurence

print(l.count(3))       #number of times occured

m = l                   #m becomes reference of l; changes also reflect in l
m[0] = 0
print(l)

# to avoid that use copy instead

n = l.copy()
n[0] = 1
print("output of n after using copy func:\n",n,"\n",l)

n.insert(2,67)
print(n)

color = ['red','green','blue']
mcolor = ['cyan','magenta','yellow']

color.extend(mcolor)
print(color)

color = ['red','green','blue']
mcolor = ['cyan','magenta','yellow']

print(color+mcolor)