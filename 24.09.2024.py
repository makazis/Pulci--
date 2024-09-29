from random import *
def run_blackjack(first_card=0,depth=0):
    output=0
    cards=[2,3,4,5,6,7,8,9,10,10,10,10,11]
    card_names=["Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace"]
    score=first_card
    dealer_pot=0

    drawn_card_prime=int(randint(0,len(cards)-1))
    drawn_card=cards[drawn_card_prime]
    print("The dealer drew a",card_names[drawn_card_prime])
    dealer_pot+=drawn_card

    drawn_cards=[]
    if first_card!=0:
        drawn_cards.append(first_card)
        score+=cards[first_card]
    while score<21:
        drawn_card_prime=int(randint(0,len(cards)-1))
        drawn_card=cards[drawn_card_prime]
        drawn_cards.append(drawn_card_prime)
        print("You drew a",card_names[drawn_card_prime])
        print("The dealer drew a card face down")
        score+=drawn_card
        print(score,"In pot")
        if score<21 and len(drawn_cards)>(int(first_card)==0):
            if len(drawn_cards)==2:
                if drawn_cards[0]==drawn_cards[1]:
                    if input("Do you want to split (yes/no): ")=="yes":
                        print("Another game begins! ",end="")
                        if depth>0:
                            print("(Depth:",depth+1,")")
                        else:
                            print()
                        output+=run_blackjack(drawn_cards[0],depth+1)
            if input("Do you want to draw again: ")=="no":
                break
    victory=False
    draw=False
    if score>21:
        print("Bust!")
    else:
        if len(drawn_cards)==2 and score==21:
            print("Blackjack")
            victory=True
        else:
            for i in range(len(drawn_cards)-1):
                drawn_card_prime=int(randint(0,len(cards)-1))
                drawn_card=cards[drawn_card_prime]
                print("The dealer opened a",card_names[drawn_card_prime])
                dealer_pot+=drawn_card
                print("The dealer has",dealer_pot,"in their pot")
            
            if dealer_pot<score:
                victory=True
            if dealer_pot==score:
                draw=True
            if dealer_pot>21:
                victory=True
    if victory:
        print("You WIN! Good Job!")
        return 1
    else:
        if draw:
            print("Draw! You get your money back")
            return 0
        else:
            print("You Lose! Skill Issue")
            return -1
cash=100
while cash>0:
    money_in=0
    print("You have",cash,"cash, let's go gambling!")
    while not cash>=money_in>0:
        money_in=input("How much would you like to bet?")
        try:
            money_in=int(money_in)
        except:
            money_in=0
    cash+=money_in*run_blackjack()
print("Out of cash!")