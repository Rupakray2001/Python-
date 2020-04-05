# task 2
#create two empty sets
a=set()
b=set()
#upadte set1 with 7,8,9,1,2,3,4,5,0
c={7,8,9,1,2,3,4,5,0}
a.update(c)
#update set2 with 4,5,6,0
d={4,5,6,0}
b.update(d)
#check whether set2 is subset of set1?
print(a.issubset(b))
#check whether both are disjoint?
print(a.isdisjoint(b))
#remove 8 froms set1
a.remove(8)
#discard 0 from set2
b.discard(0)
#find sum(set1 union set2)
e=a.union(b)
print(sum(e))
