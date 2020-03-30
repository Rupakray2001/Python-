''' copy - It copies and creates a seperate object altogether. The example
shows that the out of this would be "[4, 3, 2, 1, 1, 2, 3, 4]".
Where due to the "reverse" function the only the original list is getting
reversed whereas the copied object is not getting reversed '''
a=[1,2,3,4]
b=a.copy()
e=a.reverse()
print(a+b)



''' Direct assignment = just simply creates a referance to the origianl list.
That is when the reverse function is used it reverse both the orginal list and
the referenced list '''
c=[1,2,3,4]
d=c
f=c.reverse()
print(c+d)

#_______________________________________________________________________________
#difference between del and clear
# Del = can be used with list, it deletes the specified index
g = ["apple", "banana", "cherry","mango"]
del g[1]
print(g)
print(type(g))

# Clear =  it would clear the whole data 
e={1,2,3,4,5,6,7,8}
f=e
g=e.clear()
print(g)
print(e)

# Clear = can be used with list 
h={1,2,3,4,5,6,7,8}
i=h.copy()
print(type(i))
j=h.clear()
print(i)
print(j)

k = ["apple", "banana", "cherry","mango"]
l=k.clear()
print(l)
#_____________________________________________________________________________
#how to reverse the list
m = ["apple", "banana", "cherry","mango"]
n=m[::-1]
print(n)




