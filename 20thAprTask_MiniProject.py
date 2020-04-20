import random

choicePredefined=("gun","water","snake")

attempts=0
acceptedNoOfAttempts=10
userWin=0
systemWin=0
Tie=0

#rRandom=random.choice(choicePredefined)

while attempts<acceptedNoOfAttempts:
    rRandom=random.choice(choicePredefined)
    userChoice=str(input("Please guess the winner amongst snake, gun and water"))
    if userChoice==rRandom=="gun":
        userWin=userWin+1
    elif userChoice==rRandom=="water":        
        userWin=userWin+1
    elif userChoice==rRandom=="snake":
        userWin=userWin+1
    else:
        systemWin=systemWin+1
    print("System guess the winner is:",rRandom)
    attempts=attempts+1

if userWin==systemWin:
    print("This is a Tie")
        

print("User won" , userWin ,"times")
print("System won", systemWin, "times")
    
if userWin>systemWin:
    print("Congratulation you WON the contest")
else:
    print("Better luck next time, System WON")
