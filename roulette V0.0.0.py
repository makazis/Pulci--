from random import *
color=["black","red"]
number=randint(0,36)
green=0
red=(1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36)
black=(2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35)
if input("Will you bet on a number or color?" )=="color":
     color_win = choice(color)
     color_choice = input("Red or black? ")
     bet = int(input("How much would you like to bet? "))
     print("Result:",color_win)
     if color_choice==color_win:
          print("You won",bet*2,"!" )
     else:
          print("You lost...")
else:
    number_bet=int(input("On which number would you like to bet?"))
    bet= int(input("How much would you like to bet? "))
    print("Result:",number)
    if number==number_bet:
         print("You won",bet*2,"!" )
    else:
          print("You lost...")
