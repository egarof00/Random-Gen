from random import*
i = 0
aRandomNumber = randint(1, 20)
while i<3:
    guess = input("Guess a number between 1 and 20. You have three tries to get it right!")
    guess=int(guess)
    if guess == aRandomNumber:
        print("Nice! You guessed it!")
        break
    else:
        print("Try Again!")
        i += 1
        if aRandomNumber > guess and i<3:
            print("A little higher!")
        if aRandomNumber < guess and i<3:
            print("A teeny bit lower")
if i==3:
    print("Nice try!The number was...")
    print(aRandomNumber)
