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

    # This method is required by libqi and should return a dictionary with login information.
    # The dictionary should have thels keys 'user' and 'token'.
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
app = qi.Application(sys.argv, url=url)
logins = ("nao", "nao")
factory = AuthenticatorFactory(*logins)
app.session.setClientAuthenticatorFactory(factory)
app.start()
print("started")


# Get the service ALVideoDevice.
ALMood = app.session.service("ALMood")
duration = 65  # seconds

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
            

mood_df.to_csv("mood_data")


