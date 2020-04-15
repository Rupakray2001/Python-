# write a function to check whether a string is palindrome

def aPalindrome(x):
    if (x == x[::-1]):
        print("Provided number is palindrome")
    else:
        print("Provided number is not a plindrome")

aPalindrome(input("Please provide a number "))

# write function to check whether a no is odd or even

def aOddOrEven(x):
    if x%2==0:
        print("Provided number is even")
    else:
        print("Provded number is odd")

aOddOrEven(int(input("Please provide a number ")))

# write function to check whether a no is +ve or -ve

def aPostiveOrNegative(x):
    if x>=0:
        print("Provided number is postive")
    else:
        print("Provided number is negative")

aPostiveOrNegative(int(input("Please provide a number ")))

# get two numbers from user and do below process
#(a + b)(a - b)

def multiple(a,b):
    product=(a + b)*(a - b)
    return product
    
a=int(input("Please provide a number "))
b=int(input("Please provide another number "))
print(multiple(a,b))

# get three numbers from user and do below process
#(a + b)(a - b)(a-c)

def multiple1(d,e,f):
    product=(d + e)*(d - e)*(d-f)
    return product

d=int(input("Please provide a number "))
e=int(input("Please provide another number "))
f=int(input("Please provide another number "))
print(multiple1(d,e,f))



