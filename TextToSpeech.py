import qi
import sys
import time
import cv2
import numpy as np

order = int(sys.argv[1])
url = sys.argv[2]

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
app = qi.Application(sys.argv, url=url)
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
    tts.say('''\\VCT=60\\ \\vol=60\\ \\emph=0\\ In  \\emph=0\\ a \\emph=0\\ quiet \\emph=0\\ little town, lived Penelope, 
            a \\emph=0\\ penguin \\emph=0\\ with \\emph=0\\ a  \\emph=0\\grand \\emph=0\\ culinary  \\emph=0\\ ambition. \pau=350\ 
            Unlike \\emph=0\\ her \\emph=0\\ friends \\emph=0\\, who \\emph=0\\ were  \\emph=0\\content \\emph=0\\ with fish, 
            Penelope \\emph=0\\ dreamed \\emph=0\\ of \\emph=0\\ creating \\emph=0\\ the \\emph=0\\ perfect \\emph=0\\ pizza. \pau=350\ 
            On \\emph=0\\ her \\emph=0\\ big \\emph=0\\ day, \\emph=0\\ Penelope \\emph=0\\ set \\emph=0\\ out \\emph=0\\ to assemble
            her \\emph=0\\ masterpiece. \\emph=0\\ \\pau=350\\ But \\emph=0\\ in \\emph=0\\ her \\emph=0\\ excitement, \\emph=0\\
            she \\emph=0\\ confused \\emph=0\\ the \\emph=0\\ tomato \\emph=0\\ sauce \\emph=0\\ with \\emph=0\\ strawberry \\emph=0\\ jam. 
            \\pau=350\\ As \\emph=0\\ she \\emph=0\\ slid \\emph=0\\ the \\emph=0\\ pizza \\emph=0\\ into \\emph=0\\ the \\emph=0\\ oven, 
            she \\emph=0\\ hummed \\emph=0\\ a \\emph=0\\ tune, \\emph=0\\ oblivious \\emph=0\\ to \\emph=0\\ the \\emph=0\\ sweet \\emph=0\\
            mistake. \\emph=0\\ \pau=350\ When \\emph=0\\ the \\emph=0\\ timer \\emph=0\\ dinged, \\emph=0\\ Penelope, \\emph=0\\ with 
            a \\emph=0\\ flourish, \\emph=0\\ presented  \\emph=0\\ her \\emph=0\\creation \\emph=0\\ to \\emph=0\\ her \\emph=0\\ friends. 
            \\emph=0\\ \pau=350\ One \\emph=0\\ bite, \\emph=0\\ and \\emph=0\\ there \\emph=0\\ was \\emph=0\\ a  \\emph=0\\ pause, \pau=450\ 
            \\emph=0\\ then \\emph=0\\ an \\emph=0\\ eruption \\emph=0\\ of \\emph=0\\ laughter. \pau=350\ \\emph=0\\ Strawberry \\emph=0\\ pizza was, 
            surprisingly,\\emph=0\\ not \\emph=0\\ the \\emph=0\\ worst \\emph=0\\ thing \\emph=0\\ they'd \\emph=0\\ ever \\emph=0\\ tasted.
            \pau=350\ \\emph=0\\ Penelope's \\emph=0\\ pizza \\emph=0\\ adventure \\emph=0\\ became \\emph=0\\ the \\emph=0\\ talk \\emph=0\\
            of \\emph=0\\ the \\emph=0\\ town, \\emph=0\\ proving \\emph=0\\ that \\emph=0\\ sometimes,  \\emph=0\\ the best \\emph=0\\ discoveries 
            are \\emph=0\\ accidents. \\emph=0\\ \pau=350\ And \\emph=0\\ maybe, \\emph=0\\ just \\emph=0\\ maybe, \\emph=0\\ penguins \\emph=0\\ 
            could \\emph=0\\ be \\emph=0\\ gourmet \\emph=0\\ chefs \\emph=0\\ after \\emph=0\\ all.'''
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
