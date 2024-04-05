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

tts = app.session.service("ALTextToSpeech")
# tts.say("Hello, how are you")

order = int(sys.argv[1])
# print(sys.argv)

if order == 0: # story 2 monotone
    tts.say(''' \\state=neutral\\ \\VCT=60\\ \\vol=60\\ \\emph=0\\ \\wait=1\\ In  \\emph=0\\ \\wait=1\\ a \\emph=0\\ \\wait=1\\ quiet \\emph=0\\ \\wait=1\\ little town, lived Penelope, 
            a \\emph=0\\ \\wait=1\\ penguin \\emph=0\\ \\wait=1\\ with \\emph=0\\ \\wait=1\\ a  \\emph=0\\ \\wait=1\\grand \\emph=0\\ \\wait=1\\ culinary  \\emph=0\\ \\wait=1\\ ambition. \pau=350\ 
            Unlike \\emph=0\\ \\wait=1\\ her \\emph=0\\ \\wait=1\\ friends \\emph=0\\ \\wait=1\\, who \\emph=0\\ \\wait=1\\ were  \\emph=0\\ \\wait=1\\content \\emph=0\\ \\wait=1\\ with fish, 
            Penelope \\emph=0\\ \\wait=1\\ dreamed \\emph=0\\ \\wait=1\\ of \\emph=0\\ \\wait=1\\ creating \\emph=0\\ \\wait=1\\ the \\emph=0\\ \\wait=1\\ perfect \\emph=0\\ \\wait=1\\ pizza. \pau=350\ 
            On \\emph=0\\ \\wait=1\\ her \\emph=0\\ \\wait=1\\ big \\emph=0\\ \\wait=1\\ day, \\emph=0\\ \\wait=1\\ Penelope \\emph=0\\ \\wait=1\\ set \\emph=0\\ \\wait=1\\ out \\emph=0\\ \\wait=1\\ to assemble
            her \\emph=0\\ \\wait=1\\ masterpiece. \\emph=0\\ \\wait=1\\ \\pau=350\\ But \\emph=0\\ \\wait=1\\ in \\emph=0\\ \\wait=1\\ her \\emph=0\\ \\wait=1\\ excitement, \\emph=0\\ \\wait=1\\
            she \\emph=0\\ \\wait=1\\ confused \\emph=0\\ \\wait=1\\ the \\emph=0\\ \\wait=1\\ tomato \\emph=0\\ \\wait=1\\ sauce \\emph=0\\ \\wait=1\\ with \\emph=0\\ \\wait=1\\ strawberry \\emph=0\\ \\wait=1\\ jam. 
            \\pau=350\\ As \\emph=0\\ \\wait=1\\ she \\emph=0\\ \\wait=1\\ slid \\emph=0\\ \\wait=1\\ the \\emph=0\\ \\wait=1\\ pizza \\emph=0\\ \\wait=1\\ into \\emph=0\\ \\wait=1\\ the \\emph=0\\ \\wait=1\\ oven, 
            she \\emph=0\\ \\wait=1\\ hummed \\emph=0\\ \\wait=1\\ a \\emph=0\\ \\wait=1\\ tune, \\emph=0\\ \\wait=1\\ oblivious \\emph=0\\ \\wait=1\\ to \\emph=0\\ \\wait=1\\ the \\emph=0\\ \\wait=1\\ sweet \\emph=0\\ \\wait=1\\
            mistake. \\emph=0\\ \\wait=1\\ \pau=350\ When \\emph=0\\ \\wait=1\\ the \\emph=0\\ \\wait=1\\ timer \\emph=0\\ \\wait=1\\ dinged, \\emph=0\\ \\wait=1\\ Penelope, \\emph=0\\ \\wait=1\\ with 
            a \\emph=0\\ \\wait=1\\ flourish, \\emph=0\\ \\wait=1\\ presented  \\emph=0\\ \\wait=1\\ her \\emph=0\\ \\wait=1\\creation \\emph=0\\ \\wait=1\\ to \\emph=0\\ \\wait=1\\ her \\emph=0\\ \\wait=1\\ friends. 
            \\emph=0\\ \\wait=1\\ \pau=350\ One \\emph=0\\ \\wait=1\\ bite, \\emph=0\\ \\wait=1\\ and \\emph=0\\ \\wait=1\\ there \\emph=0\\ \\wait=1\\ was \\emph=0\\ \\wait=1\\ a  \\emph=0\\ \\wait=1\\ pause, \pau=450\ 
            \\emph=0\\ \\wait=1\\ then \\emph=0\\ \\wait=1\\ an \\emph=0\\ \\wait=1\\ eruption \\emph=0\\ \\wait=1\\ of \\emph=0\\ \\wait=1\\ laughter. \pau=350\ \\emph=0\\ \\wait=1\\ Strawberry \\emph=0\\ \\wait=1\\ pizza was, 
            surprisingly,\\emph=0\\ \\wait=1\\ not \\emph=0\\ \\wait=1\\ the \\emph=0\\ \\wait=1\\ worst \\emph=0\\ \\wait=1\\ thing \\emph=0\\ \\wait=1\\ they'd \\emph=0\\ \\wait=1\\ ever \\emph=0\\ \\wait=1\\ tasted.
            \pau=350\ \\emph=0\\ \\wait=1\\ Penelope's \\emph=0\\ \\wait=1\\ pizza \\emph=0\\ \\wait=1\\ adventure \\emph=0\\ \\wait=1\\ became \\emph=0\\ \\wait=1\\ the \\emph=0\\ \\wait=1\\ talk \\emph=0\\ \\wait=1\\
            of \\emph=0\\ \\wait=1\\ the \\emph=0\\ \\wait=1\\ town, \\emph=0\\ \\wait=1\\ proving \\emph=0\\ \\wait=1\\ that \\emph=0\\ \\wait=1\\ sometimes,  \\emph=0\\ \\wait=1\\ the best \\emph=0\\ \\wait=1\\ discoveries 
            are \\emph=0\\ \\wait=1\\ accidents. \\emph=0\\ \\wait=1\\ \pau=350\ And \\emph=0\\ \\wait=1\\ maybe, \\emph=0\\ \\wait=1\\ just \\emph=0\\ \\wait=1\\ maybe, \\emph=0\\ \\wait=1\\ penguins \\emph=0\\ \\wait=1\\ 
            could \\emph=0\\ \\wait=1\\ be \\emph=0\\ \\wait=1\\ gourmet \\emph=0\\ \\wait=1\\ chefs \\emph=0\\ \\wait=1\\ after \\emph=0\\ \\wait=1\\ all.'''
)

elif order == 1: #story 1 monotone
    tts.say('''\\VCT=70\\ Once upon a 
    time, in a world not too different from ours,
    lived Robbie, a robot with a peculiar problem. \pau=350\ Unlike his precise peers, Robbie had two left feet, 
    figuratively speaking, making him the most clumsy robot in town.\pau=350\ One sunny day, Robbie decided to bake 
    a cake, a task that should have been simple.\pau=350\ As he danced around the kitchen, mixing ingredients 
    with a flourish only he could manage, things took a hilarious turn.\pau=350\ With a twirl too many, he accidentally launched 
    the flour bag into the ceiling fan, turning his kitchen into a winter wonderland. Robbie, 
    covered in flour from head to toe, could only laugh at his snowy mishap. He realized then, maybe he wasn't cut out for baking, 
    or twirling, but he definitely had a knack for making the best snow angels indoors. And so, Robbie's misadventure left everyone chuckling, 
    reminding them that sometimes, it's our quirks that make the best stories. Who knew robots could be so... human?''')
