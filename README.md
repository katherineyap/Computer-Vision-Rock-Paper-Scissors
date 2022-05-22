# Computer-Vision-Rock-Paper-Scissors - Aicore Project 2
	A new play of an old game based upon Machine Learning and Computer Vision
-------------------------------------------------------------------------------------

## Milestone 1 - Create the Model
* Gathered four classes of image samples (hand gestures of paper, rock, scissors and nothing) and trained the model on Teachable Machine
* The model was then downloaded and pushed to github

## Milestone 2 - Install the Dependencies
Created a virtual environment with Conda and installed all necessary packages. In this case, *opencv-python, tensorflow, ipykernel*.
The commands are as follow:
* conda env list - (*to check all conda environments*)
* conda create --name filename (*create a new environment*)
* confa activate filename (*activate new environment*)
* conda install pip (*use conda to install pip, and (via pip) access Github, because conda cannot install files from Github directly*)
* pip install opencv-python(*cv2, a great tool for image processing and performing computer vision tasks*)
* pip install tensorflow
* pip install ipykernel

Then, run the downloaded model with the given code.
Get familiar with the code
```
import cv2 
from keras.models import load_model
import numpy as np
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

while True: 
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    cv2.imshow('frame', frame)
    # Press q to close the window
    print(prediction)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
            
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()
```
## Milestone 3 - Create a Rock-Paper-Scissors Game
Created a separate file to play the game without using the camera
* Import Random module for computer's choice, and Input for user's choice 
* Use if-elif-else statement to figure who wins 
* stimulate the game


