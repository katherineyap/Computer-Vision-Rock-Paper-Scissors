
import random

option = ['rock','paper','scissors']

computer_choice = random.choice(option)
user_choice = input('please select your option:')


def get_winner(computer_choice, user_choice):
    computer_win = 0
    user_win = 0

    if computer_choice == user_choice:
        print ("It's a tie")

    elif computer_choice == 'rock':
        if user_choice == 'paper':
            user_win +=1
            print(f'user choice is :', user_choice,' ' + 'computer choice is :', computer_choice,'. User wins')
            print (f'user wins,', user_win,'rounds.')
        else :
            computer_win +=1
            print(f'user choice is :', user_choice,' ' + 'computer choice is :', computer_choice,'. Computer wins')
            print (f'computer wins,', computer_win,'rounds.')

    elif computer_choice == 'paper':
        if user_choice == 'rock':
            computer_win +=1
            print(f'user choice is :', user_choice,' ' + 'computer choice is :', computer_choice,'. Computer wins')
            print (f'computer wins,', computer_win,'rounds.')
            who_wins (computer_win, user_win)
        if user_choice == 'scissors':
            user_win +=1
            print(f'user choice is :', user_choice,' ' + 'computer choice is :', computer_choice,'. User wins')
            print (f'user wins,', user_win,'rounds.')
            who_wins (computer_win, user_win)

    elif computer_choice == 'scissors':
        if user_choice == 'rock':
            user_win +=1
            print(f'User choice is :', user_choice,' ' + 'computer choice is :', computer_choice,'. User wins')
            print (f'user wins,', user_win,'rounds.')
        if user_choice == 'paper':
            computer_win +=1
            print(f'user choice is :', user_choice,' ' + 'computer choice is :', computer_choice,'. Computer wins')
            print (f'computer wins,', computer_win,'rounds.')

def who_wins (computer_win, user_win):
    if computer_win == 3 or user_win == 3:
        if computer_win == 3:
            print ('The computer wins')
        elif user_win ==3:
            print ('The user wins')

get_winner(computer_choice, user_choice)