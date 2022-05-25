import rps_game
import manual_rps

# 0 Scissors
# 1 Rock
# 2 Paper
# 3 Nothing

def get_prediction(prediction):
    if prediction[0]>[1]or[2]:
        user_choice = 'Scissors'
    elif prediction [1] > [0] or [2]:
        user_choice = 'Rock'
    elif prediction [2] > [0] or [1]:
        user_choice = 'Paper'
    else:
        user_choice = 'Nothing'
    return user_choice
