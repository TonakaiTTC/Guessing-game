import random

print('Hello please enter your name')
playername = input()
secretnum = random.randint(1,100)
print('Thanks,' + playername + " please choose a number between 1 and 100, and remember you only have 5 guesses")



for totalguesses in range(5):
    guess = int(input())

    if guess == secretnum:
        print('You won! Yayy')
    elif guess > secretnum:
        print('Your guess was too high')
    else:
        print('Your guess was too low')    
if guess != secretnum: 
    print('You lost.The secret Number was')
    print(secretnum)
else:
    print('You won!!!')
