import qi
import sys
import time
import cv2
import numpy as np

class Authenticator:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    # This method is expected by libqi and must return a dictionary containing
    # login information with the keys 'user' and 'token'.
    def initialAuthData(self):
        return {'user': self.username, 'token': self.password}


class AuthenticatorFactory:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    # This method is expected by libqi and must return an object with at least
    # the `initialAuthData` method.
    def newAuthenticator(self):
        return Authenticator(self.username, self.password)

# Connect to the robot fails at app.start() => RuntimeError: disconnected
app = qi.Application(sys.argv, url="tcps://10.0.0.17:9503")
logins = ("nao", "nao")
factory = AuthenticatorFactory(*logins)
app.session.setClientAuthenticatorFactory(factory)
app.start()
print("started")

tts = app.session.service("ALAnimatedSpeech")

# order = int(input())
order = int(sys.argv[1])

if order == 0:          # story 1 animated
    tts.say('''\\VCT=80\\ \\style=joyful\\ Once upon a time, in a world not too different from ours,
    lived Robbie, a robot with a peculiar problem. \pau=350\ Unlike his precise peers, Robbie had two left feet, 
    figuratively speaking, making him the most clumsy robot in town.\pau=350\ One sunny day, Robbie decided to bake 
    a cake, a task that should have been simple.\pau=350\ As he danced around the kitchen, mixing ingredients 
    with a flourish only he could manage, things took a hilarious turn.\pau=350\ With a twirl too many, he accidentally launched 
    the flour bag into the ceiling fan, turning his kitchen into a winter wonderland. Robbie, 
    covered in flour from head to toe, could only laugh at his snowy mishap. He realized then, maybe he wasn't cut out for baking, 
    or twirling, but he definitely had a knack for making the best snow angels indoors. And so, Robbie's misadventure left everyone chuckling, 
    reminding them that sometimes, it's our quirks that make the best stories. Who knew robots could be so... human?''')

elif order == 1:        # story 2 animated
    tts.say("Hello,")