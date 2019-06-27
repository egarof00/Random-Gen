from random import*
aRandomNumber = randint(1, 20)
for i in range (3):
    guess = input("Guess a number between 1 and 20. You have three tries to get it right!")
    guess=int(guess)
    if guess == aRandomNumber:
        print("Nice! You guessed it!")
        
        break
    else:
        if aRandomNumber > guess:
            print("A little higher!")
        if aRandomNumber < guess:
            print("A teeny bit lower")
    continue
if guess != aRandomNumber:
    print("Nice try! The number was...")
    print(aRandomNumber)
