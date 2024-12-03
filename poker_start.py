'''Poker game created by Fernando Blum Garcia
FBG: https://github.com/fblumgarcia97'''

import main
import os
import random


ranks=("2","3","4","5","6","7","8","9","10","J","Q","K","A")
suits=("Clubs","Diamonds","Hearts","Spades")
cards=[]

def start_page():
    cards.clear()
    os.system('cls')
    print ("Welcome to FBG Poker  \n Do you want to try your lucky? \n 1. YES :) \n 2. NO :(")
    selection_menu_start=int(input("Choose an option: "))
    if selection_menu_start!=1 and selection_menu_start!=2:
        print("Check the options")
        os.system('cls')
        start_page()
    elif selection_menu_start==2:
        os.system('cls')
        print("See you soon")
    elif selection_menu_start==1:
        os.system('cls')
        print("You join the table!!!!\n Good luck")
        play_game()
        
def create_card():
    counter=0
    while counter==0:
        created_card=random.choice(ranks)+" "+random.choice(suits)
        if created_card in cards:
            continue
        else:
            cards.append(create_card)
            counter=1
    return created_card

def verify_result():
    os.system('cls')
    print(cards)

def play_game():
    first_card_player=create_card()
    second_card_player=create_card()
    print("Your cards are: "+first_card_player+" and "+second_card_player)
    print("Do you want continue to the FLOP: \n 1. Yes \n 2. No")
    selection_flop=int(input())
    if selection_flop==2:
        print("Bye Bye")
        start_page()
    elif selection_flop==1:
        first_flop=create_card()
        second_flop=create_card()
        third_flop=create_card()
        print("The flop are: "+first_flop+", "+second_flop+" and "+third_flop)
        while True:
            print("Do you want continue to the TURN: \n 1. Yes \n 2. No")
            selection_turn=int(input())
            if selection_turn==2:
                print("Bye Bye")
                start_page()
                break
            elif selection_turn==1:
                turn=create_card()
                print("The turn is: "+turn)
                while True:
                    print("Do you want continue to the RIVER: \n 1. Yes \n 2. No")
                    selection_river=int(input())
                    if selection_river==2:
                        print("Bye Bye")
                        start_page()
                        break
                    elif selection_river==1:
                        river=create_card()
                        print("The turn is: "+river)
                        verify_result()
                        break
                    else:
                        print("Check options")
                break
            elif selection_turn!=1 and selection_turn!=2:
                print("check the options")