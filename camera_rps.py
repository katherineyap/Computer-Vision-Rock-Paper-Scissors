import rps_game
import manual_rps
import numpy as np

# 0 Scissors
# 1 Rock
# 2 Paper
# 3 Nothing
model_dic = {0:'Scissors', 1:'Rock',2: 'Paper', 3: 'Nothing'}

def get_prediction(prediction):
   indices = np.argmax(prediction[0])
   computer_choice = model_dic[indices]
   return computer_choice