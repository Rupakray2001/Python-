a=[]#create empty list
b= [5,6,8,9]
print(a+b)
c=(a+b)+[8,9,1,-5,6,7,8]#concatenate it with [5,6,8,9]
print(c)#add 8,9,1,-5,6,7,8 in to list1
print(c.count(8))#no. of accounrance of 8
print(sum(c)/len(c))#average of the list
print(sum(c)+min(c)+max(c))#sum of list+min ele+max ele of list
print((sum(c)/len(c)))#mean is
print(len(c)/2)#median is
d=tuple(set(c))
print(d)
