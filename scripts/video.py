import qi
import sys
import time
import cv2
import numpy as np

url = sys.argv[1]

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
app = qi.Application(sys.argv, url=url)
logins = ("nao", "nao")
factory = AuthenticatorFactory(*logins)
app.session.setClientAuthenticatorFactory(factory)
app.start()
print("started")

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


duration = 5  # seconds

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

