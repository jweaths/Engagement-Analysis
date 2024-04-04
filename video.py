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

# This doesn't work either => RuntimeError: disconnected
# session = qi.Session()
# logins = ("nao", "OMITTED")
# factory = AuthenticatorFactory(*logins)
# session.setClientAuthenticatorFactory(factory)
# session.connect("tcp://192.168.1.59:9503")

# tts = app.session.service("ALTextToSpeech")
# tts.say("video session started")

# Get the service ALVideoDevice.
video_service = app.session.service("ALVideoDevice")

# Subscribe to the top camera, VGA resolution, BGR color space
resolution = 3    # VGA
colorSpace = 13   # BGR
fps = 15


# Create a video writer to output the video file
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('output.avi', fourcc, fps, (320, 240))

cameraId = 0  # 0 for top camera, 1 for bottom camera
subscriberId = video_service.subscribeCamera("videoCapture", cameraId, resolution, colorSpace, fps)


duration = 10  # seconds

try:
    start_time = time.time()
    while time.time() - start_time < duration:
        # Get image frame from the camera
        naoImage = video_service.getImageRemote(subscriberId)
        
        if naoImage is None:
            print("Cannot capture.")
        else:
            # Get the image size and pixel array.
            imageWidth = naoImage[0]
            imageHeight = naoImage[1]
            # print(imageWidth, imageHeight)
            array = naoImage[6]
            image_string = bytes(bytearray(array))
            
            # Create an OpenCV image from the raw image data
            img = np.frombuffer(image_string, dtype=np.uint8).reshape((imageHeight, imageWidth, 3))
            
            # Write the frame to the video file
            out.write(img)
            
            # Display the frame for demonstration purposes
            # cv2.imshow('Frame', img)
            # cv2.waitKey(1)

finally:
    # Unsubscribe the camera
    video_service.unsubscribe(subscriberId)
    out.release()
    cv2.destroyAllWindows()
