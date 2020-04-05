#task4
#create a dictionary {1:["english","maths","science":["bio-zoology","bio-botany","physics"]],2:(10,20,40,"python program")}
a={1:["english","maths","science",["bio-zoology","bio-botany","physics"]],2:(10,20,40,"python program")}
#extract botany
print(a[1][3][1][4:])
#extract "english","maths","science" from that dictionary and covert it into tuple and print len
b=tuple(a[1][0])
c=tuple(a[1][1])
d=tuple(a[1][2])
print(len(b)+len(c)+len(d))

#print all keys in dictionary
print(a.keys())

#extract "python" from dictionary
print(a[2][3][0:6])

#add all numbers in volumes under key 2
