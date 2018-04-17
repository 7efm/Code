# imports modules, API's, libraries
import time
import sys
import random
# Definitions of functions, classes, etc


def start():
    print("Welcome to rock, paper, scissors deluxe!")
    print("Select the computer's difficulty to begin.")
    for i in level:
        print(i)
    ans = input('---> ')
    ans = ans.upper()
    if ans == 'A':
        print('You will play against a regular computer. ')
        print('')
        print('Enter your choice')
        return 0
    elif ans == 'B':
        print('You will play against a smart computer (adapts to your choices).')
        print('')
        print('Enter your choice')
        return 1


def smart_comp_choice(predict):
        if predict == 0:
            return 1
        elif predict == 1:
            return 2
        elif predict == 2:
            return 0
        else:
            choice = random.randint(0, 2)
            return choice


def regular_user_choice():
    for i in options:
        print(i)
    user_choice = input(': ')
    user_choice = user_choice.upper()
    if user_choice == 'A':
        print('You chose rock')
        print('Wait for your opponent to choose...')
        time.sleep(2)
        return 0
    elif user_choice == 'B':
        print('You chose paper')
        print('Wait for your opponent to choose...')
        time.sleep(2)
        return 1
    else:
        print('You chose scissors')
        print('Wait for your opponent to choose...')
        time.sleep(2)
        return 2


def regular_comp_choice():
    choice = random.randint(0, 2)
    print(choice)
    print('comp chose ' + options[choice])
    return choice


def decision():
    predict = random.randint(0, 2)
    rounds = 0
    while rounds < 5:
        rock = 0
        paper = 0
        scissors = 0
        if re == 0:
            comp = regular_comp_choice()
            user = regular_user_choice()
            rounds += 1
        else:
            if rounds >= 1:
                comp = smart_comp_choice(predict)
                user = regular_user_choice()
                if user == 0:
                    rock += 1
                elif user == 1:
                    paper += 1
                else:
                    scissors += 1
                if rock > paper and rock > scissors:
                    predict = 0
                elif paper > rock and paper > scissors:
                    predict = 1
                elif scissors > paper and scissors > rock:
                    predict = 2
                else:
                    print("ERROR")
                    predict = random.randint(0, 2)
                rounds += 1
            else:
                comp = regular_comp_choice()
                user = regular_user_choice()
                rounds += 1

        if user == 0 and comp == 1:
            print('Sorry! Your opponent won this round by choosing paper')

        elif user == 0 and comp == 2:
            print('Nice Job! You won this round, your opponent chose scissors')

        elif user == 1 and comp == 0:
            print('Nice Job! You won this round, your opponent chose rock')

        elif user == 1 and comp == 2:
            print('Sorry! Your opponent won this round by choosing scissors')

        elif user == 2 and comp == 0:
            print('Sorry! Your opponent won this round by choosing rock')

        elif user == 2 and comp == 1:
            print('Nice Job! You won this round, your opponent chose paper')
        elif user == comp:
            print("Oops, looks like you both chose %s, it's a tie" % options[comp])
        else:
            print('error')


# Define global variables, lists, dictionaries

userchoices = []
level = ['A: Regular', 'B: Smart']
options = ['A: Rock', 'B: Paper', 'C: Scissors']
# Main Program, Program Logic or Algorithm
re = start()
decision()
