#creating a list using []

a=[1,4,5,6,2]

a[1]=98

print(a)

#access using index

print(a[3])

#we can create list with different items

c=["harry",90,"karlu" ,30]
print(c)

#list slicesing

freinds=['oiehrr','oher','oiheroi','heroi']

print(freinds[0:3])

#sorting in list

n=[3,939,478,7392,9834,4,939,9]
n.sort()
n.reverse()
n.append(899)
n.insert(3,3889334)
n.pop(4)
n.remove(4)
print(n)