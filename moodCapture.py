import qi
import sys
import time
import pandas as pd
import numpy as np


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

# This doesn't work either => RuntimeError: disconnected
# session = qi.Session()
# logins = ("nao", "OMITTED")
# factory = AuthenticatorFactory(*logins)
# session.setClientAuthenticatorFactory(factory)
# session.connect("tcp://192.168.1.59:9503")

# tts = app.session.service("ALTextToSpeech")
# tts.say("video session started")

# Get the service ALVideoDevice.
ALMood = app.session.service("ALMood")
duration = 5  # seconds

mood_df = pd.DataFrame(columns = ['Timestamp', 'MoodValue'])
rows = []

# try:
start_time = time.time()
while time.time() - start_time < duration:
    data = ALMood.currentPersonState()
    timestamp =time.time()
    # rows.append(data)
    row = {'Timestamp':timestamp, 'MoodValue':data}
    mood_df.loc[len(mood_df.index)] = [timestamp, data]
        
        # if naoImage is None:
            
        # else:
    time.sleep(1)
            

# mood_df["valenceValue"] = (mood_df["MoodValue"])["valence"]['value']
# mood_df["valenceConfidence"] = (mood_df["MoodValue"])["valence"]['confidence']

# mood_df["attentionValue"] = (mood_df["MoodValue"])["attention"]['value']
# mood_df["attentionConfidence"] = (mood_df["MoodValue"])["attention"]['confidence']
mood_df.to_csv("mood_data")


