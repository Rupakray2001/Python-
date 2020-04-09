#pgm1

#check whether a string is palindrome or no

#pgm2
#get a mark from student ()
#0 - 100 ==> valid
#100 grade a
#90 to 99 grade b
#80 to 89 grade c
#70 to 79 grade d
#50 to 69 grade e
# 0 to 49 fail grade f
#otherwise ===> invalid

#pgm3
#check whether first char, middle char, last char of a string is same or different

#avvacca ==> True
#hello ==> False







#program 1
a=input("Please provide a string")
b=a[::-1]

if a==b:
    print("Provided string is a palindrome")
else:
    print("Provided string is not a palidrome")

#program2
mark = input("What percentage did you get in your class 10 exam?")
b=int(mark)

if b >= 0 <=100:

    if b > 100:
        print("Cannot be more than 100")
        
    elif b == 100:
        print("A Grade")

    elif b >=90 <=99:
        print("B Grade")

    elif b >=80 <89:
        print("C grade")

    elif b >=70 <79:
        print("D grade")

    elif b >=50 <69:
        print("D grade")

    elif b >=0 <49:
        print("Fail")

        
else:
    print("provide a valid number")


#pgm3
#check whether first char, middle char, last char of a string is same or different
#avvacca ==> True
#hello ==> False

char =input("Please input a character")
middle=(char[((len(char))//2)])
if char[0]==middle==char[-1]:
    print("True")
else:
    print("False")
    
#pgm4
#get two numbers from user
onenumber=input("Please provide one number")# 27
secondnumber=input("Please provide another number")# 9
tostring=list(str(onenumber))
c=int((onenumber[0]))
d=int((onenumber[1]))
total=c+d

if total==int(secondnumber):
    print("True")# True if sum 0f first no equal to second no (2 + 7 = 9)
else:
    print("False")# otherwise False


#pgm5
#check whether a vowel present in a string and print no of occurences
#python  ==> available 1
#fst ==> not available 0
#bengaluru ==> available 4

e=input("Please provide a word")
f=int(e.count("a"))
g=int(e.count("e"))
h=int(e.count("i"))
i=int(e.count("o"))
j=int(e.count("u"))

k=f+g+h+i+j

if k>=1:
    print("Number of vowels available is: ", k)
else:
    print("No vowel available in the provided word")

