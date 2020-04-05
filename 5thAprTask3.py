#task3
#create two tuples(1,4,5,6,7)(5,6,7,8,9)
tuple1=(1,4,5,6,7)
tuple2=(5,6,7,8,9)

#concatenate two tuples after duplicate removal from both
tuple3=(tuple1+tuple2)
tuple4=tuple(set(tuple3))
print(tuple4)

#find the index value of 9
print(tuple4.index(9))


#find common elements between above elements with {0,4,5}
a=set(tuple1)
b=set(tuple2)
c=a.intersection(b)
print(c)

#multiple above tuple 3 times
print(tuple4*3)
