############### Blackjack Project #####################

import random

def compare(computer,user):
    if user > 21 and computer > 21:
        return "you lost....you went over"

    if computer==user:
        return "its a draw "
    elif computer==0:
        return "You lost...the computer has blackJack"
    elif user==0 :
        return "you won...you have the blackJack"
    elif  computer>21:
        return "you won...computer's score went over"
    elif user>21:
        return"you lost...you went over"


    elif user>computer:
         return "You won...your score is higher"
    elif computer>user:
         return "you lost...computer's score is higher"


def deal_card():
    cards = [ 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10 ]
    random_card= random.choice(cards)
    return random_card


def calculate_score(cards_list):
    score = sum(cards_list)
    if  score==21 and len(cards_list)==2:
        return 0
    if 11 in cards_list and score>21 :
        cards_list.remove(11)
        cards_list.append(1)
    return score

def play_game():

    user_cards = [ deal_card() for each in range(2) ]
    computer_cards = [ deal_card() for each in range(2) ]
    game_over = False
    while not game_over:

        calculated_user_score = calculate_score(user_cards)
        calculated_computer_score=calculate_score(computer_cards)
        print(f"Your cards : {user_cards}, your score : {calculated_user_score}")
        print(f"computer's first card : {computer_cards[0]}")
        if calculated_user_score ==0 or calculated_computer_score==0 or calculated_user_score>21:
            game_over=True
        else:
            gamer_wants_another_card=input("do you want to draw another card? if yes type y else type n ").lower()
            if gamer_wants_another_card=="y":
                user_cards.append(deal_card())
            else:
                game_over=True
        while calculated_computer_score<17 and calculated_computer_score!=0:
            computer_cards.append(deal_card())
            calculated_computer_score=calculate_score(computer_cards)
        if game_over==True:
            print(f"Your final cards : {user_cards}, your score : {calculated_user_score}")
            print(f"computer's final cards : {computer_cards}, computer score : {calculated_computer_score}")
            print(compare(calculated_computer_score,calculated_user_score))
while input("do you want to play blackJack?...type 'yes' or 'no ").lower()=="yes":

    play_game()

