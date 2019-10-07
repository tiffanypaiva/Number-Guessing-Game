import random as r

#Number Guessing Game
Num = r.randint(1,100)
Guessed = False

Guess = input("Guess The Number I am Thinking of (1-100):")

while not Guessed:
    NumberChoosen = int(Guess)
    if(NumberChoosen == Num):
        Guessed = True
    else:
        if (NumberChoosen > Num):
            print("Lower")
        else:
            print("Higher")
        Guess = input("Next guess:")

print("Congratulations! You Have guessed correctly.")
