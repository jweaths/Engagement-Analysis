import qi
import sys
import time
import cv2
import numpy as np
import random

url = sys.argv[1]

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

gesture_service = app.session.service("ALAnimationPlayer")
# tts.say("Hello, how are you")

start_time = time.time()
duration = 65
tags = ["global", "diversity"]

while time.time() - start_time < duration:
    gesture = random.choice(tags)
    gesture_service.runTag(gesture)
