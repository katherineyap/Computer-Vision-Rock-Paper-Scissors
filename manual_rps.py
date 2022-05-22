
import random

option :['rock','paper','scissors']

def get_computer_choice:
    com_choice = random.choice(option)
    return com_choice

def get_user_choice:
    print ('input')
