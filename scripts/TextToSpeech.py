import qi
import sys
import time
import cv2
import numpy as np

class Authenticator:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    # This method is required by libqi and should return a dictionary with login information.
    # The dictionary should have the keys 'user' and 'token'.
    def initialAuthData(self):
        return {'user': self.username, 'token': self.password}


class AuthenticatorFactory:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    # This method is required by libqi and should return an object that has at least
    # the `initialAuthData` method. It is used for authentication.
    def newAuthenticator(self):
        return Authenticator(self.username, self.password)

# Connect to the robot 
app = qi.Application(sys.argv, url="tcps://10.0.0.17:9503")
logins = ("nao", "nao")
factory = AuthenticatorFactory(*logins)
app.session.setClientAuthenticatorFactory(factory)
app.start()
print("started")

tts = app.session.service("ALTextToSpeech")
# tts.say("Hello, how are you")

order = int(sys.argv[1])
# print(sys.argv)

if order == 0: # story 2 monotone
  tts.say(''' \\style=neutral\\ \\VCT=60\\ \\vol=60\\ In a quiet little town, lived Penelope, 
    a penguin with a grand culinary ambition. \pau=350\ 
    Unlike her friends, who were content with fish, 
    Penelope dreamed of creating the perfect pizza. \pau=350\ 
    On her big day, Penelope set out to assemble
    her masterpiece. \\pau=350\\ But in her excitement,  
    she confused the tomato sauce with strawberry jam. 
    \\pau=350\\ As she slid the pizza into the oven, 
    she hummed a tune, oblivious to the sweet  
    mistake. \pau=350\ When the timer dinged, Penelope, with 
    a flourish, presented  her  creation to her friends. 
      \pau=350\ One bite, and there was a  pause, \pau=450\ 
      then an eruption of laughter. \pau=350\ Strawberry pizza was, 
    surprisingly,  not the worst thing they'd ever tasted.
    \pau=350\ Penelope's pizza adventure became the talk  
    of the town, proving that sometimes,  the best discoveries 
    are accidents. \pau=350\ And maybe, just maybe, penguins 
    could be gourmet chefs after all.'''
)

elif order == 1: #story 1 monotone
  tts.say('''\\VCT=60\\ \\vol=60\\ Once upon a 
  time, in a world not too different from ours,
  lived Robbie, a robot with a peculiar problem. \pau=350\ Unlike his precise peers, Robbie had two left feet, 
  figuratively speaking, making him the most clumsy robot in town.\pau=350\ One sunny day, Robbie decided to bake 
  a cake, a task that should have been simple.\pau=350\ As he danced around the kitchen, mixing ingredients 
  with a flourish only he could manage, things took a hilarious turn.\pau=350\ With a twirl too many, he accidentally launched 
  the flour bag into the ceiling fan, turning his kitchen into a winter wonderland. Robbie, 
  covered in flour from head to toe, could only laugh at his snowy mishap. He realized then, maybe he wasn't cut out for baking, 
  or twirling, but he definitely had a knack for making the best snow angels indoors. And so, Robbie's misadventure left everyone chuckling, 
  reminding them that sometimes, it's our quirks that make the best stories. Who knew robots could be so... human?''')