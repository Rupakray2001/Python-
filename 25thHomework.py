#get input from user
# try to convert second last and second to capital letters eg. python o/p pYthOn
a=input("Please provide a string")
print(a[0]+(a[1].upper())+a[2:-2]+(a[-2].upper())+a[-1])

#get one stirng from user
# get one number from user
#o/p pythonpythonpythonpythonpythonpythonpython777777
b=input("provide provide a string")
c=int(input("please provide an integer"))
print((b*c)+(len(b)*str(c)))

#get pme string from user("python")
#convert first letter, last letter, middle letter in caps
d=input("Please provide a string")
e=d[0]
f=e.upper()
g=d[-1]
h=g.upper()
m=int(len(d)/2)
r=m+1
n=(a[m])
o=n.upper()
p=a[1:m]
q=a[r:-1]
print(f+p+o+q+h)

#task4
#get two strings from user(pyton, java)
#convert first letter and last letter in to caps in both strings concat
#PythoNJavA
s=input("provide one string")
t=input("provide another string")
print(((s[0].upper())+s[1:-1]+(s[-1].upper()))+((t[0].upper())+t[1:-1]+(t[-1].upper())))


#task8
#get two numbers from user(3,5)
#o/p 55533333
u=input("provide 1 number greater than 4")
v=input("provide one number less than 4")
w=(int(v)*u)
x=(int(u)*v)
print(w+x)


      
        



