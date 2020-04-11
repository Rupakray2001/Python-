#user 10  user 30
# multiples of 8 list
# multiples 0f 9 list
a=int(input("Provide a from Value"))
b=int(input("Provide an end Value"))
c=[]
d=[]
for i in range(a,b):
    if i%8==0:
        c.append(i)
    if i%9==0:
        d.append(i)
print(c)
print(d)

#user 10  user 30
# odd number
# even number
e=int(input("Provide a from Value"))
f=int(input("Provide an end Value"))
g=[]
h=[]
for i in range(a,b):
    if i%2!=0:
        g.append(i)
    if i%2==0:
        h.append(i)
print("Odd numbers in the range are" ,g)
print("Even numbers in the range are" ,h)

#with/without vowel check
# ["hello", "bcd", "gcd", "hhmmm", "python"]

# expected output with vowels ["hello","python"]
# expected output without vowels ["bcd", "gcd", "hhmmm"]

#starting with h Expected output["hhmmm", "hello"]
# remainder of the output

j=["hello", "bcd", "gcd", "hhmmm", "python"]
k=[]
l=[]
for i in j:
    if("a" in i or "e" in i or "i" in i or "o" in i or "u" in i):
        k.append(i)
    else:
        l.append(i)

print("List contains vowels", k)
print("List do not contain vowel",l)
    
    



        
