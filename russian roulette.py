from random import *
bullet=randint(1,6)
chamber=randint(1,6)
game=True
print("Welcome to russian roulette")
def player():
    global game
    global bullet
    global chamber
    if bullet==chamber:
        print("You pull the trigger and you die :/")
        game=False
    elif chamber==6:
        chamber=1
        print("You pull the trigger and you survive")
    else:
        chamber+=1
        print("You pull the trigger and you survive") 
def dealer():    
    global game  
    global bullet     
    global chamber
    if chamber==bullet:
        print("The dealer pulls the trigger and dies. You won :)")
        game=False
    elif chamber==6:
        chamber=1
        print("The dealer pulls the trigger and survives")
    else:
        chamber+=1
        print("The dealer pulls the trigger and survives")
first=input("Do you want ot go first? (Y,N)")
if first=="Y":
    player()
    while game==True:
        dealer()
        player()
else:
    dealer()
    while game==True:
        player()
        dealer()