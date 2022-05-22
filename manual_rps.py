
import random

option = ['rock','paper','scissors']

def get_winner():
    computer_choice = random.choice(option)
    user_choice = input('please select your option:')
    if computer_choice == user_choice:
        print ("It's a tie")

    elif computer_choice == 'rock':
        if user_choice == 'paper':
            print(f'user choice is : ', user_choice,' ' + 'computer choice is : ', computer_choice,'. User wins')
        else :
            print(f'user choice is : ', user_choice,' ' + 'computer choice is : ', computer_choice,'. Computer wins')

    elif computer_choice == 'paper':
        if user_choice == 'rock':
            print(f'user choice is : ', user_choice,' ' + 'computer choice is : ', computer_choice,'. Computer wins')
        if user_choice == 'scissors':
            print(f'user choice is : ', user_choice,' ' + 'computer choice is : ', computer_choice,'. User wins')

    elif computer_choice == 'scissors':
        if user_choice == 'rock':
            print(f'User choice is : ', user_choice,' ' + 'computer choice is : ', computer_choice,'. User wins')
        if user_choice == 'paper':
            print(f'user choice is :', user_choice,' ' + 'computer choice is : ', computer_choice,'. Computer wins')

    return get_winner

get_winner()
