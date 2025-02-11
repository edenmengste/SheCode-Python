# number guessing game 
# lets assume the correct number is 5

print("Hey welcome to 'Guess the number' game")
num = int(input("You can guess here: "))
while num>0:
 if num==5:
    print("Congrats! you guessed it right")
 elif num>7:
    print("Too high, guess again")   
 elif num<3:
    print ("too low, guess again")
    break   
 else:
    print("Not correct")
    

