#task1
#re

'''def factorial(n):
    if n>=2:
        return n*factorial(n-1)
    else:
        return 1
print("factorial is ", factorial(7))'''

#The bin() function returns the binary version of a specified integer.
#x = bin(4)
#print(x)

#The bool() function returns the boolean value of a specified object.
#x = bool(2)
#print(x)


#task2


#prime or no using function
def aPrimeNo(x):
    if x >1:
        for i in range(2,(x-1)):
            if (x%i)!=0:
                return(x,"is  prime number")
                break
            else:
                return(x,"is not a prime number")
               
    else:
        return(x,"is not a prime number")
       

x=int(input("Provide a number"))
print(aPrimeNo(x))

#armstrong or no using function
def anArmstrongNo(st):
    p=len(st)
    n=int(st)
    tot=0
    num=n
    if n>0:
        d=n%10
        tot=tot+(d**p)
        n=int(n/10)
    if num==tot:
        return True
    else:
        return False
x=input("Enter no:")
if anArmstrongNo(x):
    print(x,"is an Armstrong number")
else:
    print(x,"is not an Armstrong number")


#fibonacci series using functions

def aFibonacci(n):
    x=0
    y=1
    z=0
    while (z<=n):
        print(z)
        x=y
        y=z
        z=x+y

aFibonacci(int(input("Provde a number")))



    



        


    








