from random import randint
winning_number=randint(0,100)
guess_count=0
while(guess_count<3):
    guess=int(input("guess a number:"))
    guess_count+=1
    if(guess==9):
        print("you won the game")
        break
else:
    print("you lose the game")