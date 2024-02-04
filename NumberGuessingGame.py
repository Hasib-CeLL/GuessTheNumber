import random
import math
lower = int(input("Enter lower number: "))
upper = int(input("Enter upper number: "))
X = random.randint(lower, upper)
print("\nYou have only",round(math.log(upper-lower+1,2)),"chances to guess the integer\n")
count = 0
while count < math.log(upper-lower+1,2) :
    count = count + 1
    guess = int(input("\nGuess a number: "))
    if X == guess :
        print("\nCongratulations!You have won the game in",count,"try")
        break
    elif X > guess :
        print("\nYou have guessed too small")
    elif X < guess :
        print("\nYou have guessed too high")
if count >= math.log(upper-lower+1,2) :
    print("\nThe number is %d" %X)
    print("\nBetter luck next time")
