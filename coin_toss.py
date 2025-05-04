#Coin toss Game
import random
def play():
    coin=['Heads','Tails','Exit']
    win=0
    while True:
        print("\n Guess the side of the coin")
        r=input("Heads or Tails or Exit").title()
        if r=="Exit":
            print("Total points:",win)
            break
        elif r not in coin:
            print(" Invalid selection,Try again")
            continue
        t=input("Will you bet?(yes/no)").lower()
        comp=random.choice(coin)
        print("Tossing the coin..")
        if t=="yes":
            if r==comp:
                print("You won! it was {}".format(comp))
                win=win+1
            else:
                print("You lost, It was {}".format(comp))
        else:
            print("No bet placed, It was {}".format(comp))
        print("Total points",win)
while True:
    n=input("Will you play coin guessing game?").lower()
    if n=="yes":
        play()
    else:
        print("Thanks for playing")
        break
            
    
        
    
        
