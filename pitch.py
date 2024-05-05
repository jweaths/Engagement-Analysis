import qi
import sys
import time
import cv2
import numpy as np


url = 'tcps://10.0.0.5:9503'
if len(sys.argv) > 1:
	vol = sys.argv[1]
else:
	vol = 60 # default volume is 60

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
tts.say(f'''\\VCT=80\\ \\style=neutral\\ \\vol={vol}\\ Hello, I'm Pepper. This is my Text To Speech Functionality.''')

tts = app.session.service("ALAnimatedSpeech")
tts.say(f'''\\VCT=80\\ \\vol={vol}\\ \\style=joyful\\ And this is my Animated Speech Functionality.''')

tts.say(f'''\\VCT=80\\ \\vol={vol}\\ \\style=neutral\\ Can an expressive robot engage humans more effectively than a unexpressive gesture-less robot?
        Our study aims to shed light on this question!''')

tts = app.session.service("ALTextToSpeech")
tts.say(f'''\\VCT=80\\ \\style=neutral\\ \\vol={vol}\\ For the first condition of the experiment,
         I told a story talking without gestures in a neutral voice, like this, to the human participant''')

tts = app.session.service("ALAnimatedSpeech")
tts.say(f'''\\VCT=80\\ \\vol={vol}\\ \\style=joyful\\ And the second condition is me narrating, like this, using expressive gesturing and vocal tone.''')

tts = app.session.service("ALAnimatedSpeech")
tts.say(f'''\\VCT=80\\ \\vol={vol}\\ \\style=neutral\\ I mapped the participants valence and attention using my built-in sensors.''')
        
tts.say(f'''\\VCT=80\\ \\vol={vol}\\ and the participants completed a survey to measure their internal reactions.''')

