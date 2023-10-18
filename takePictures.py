import cv2
import sys
import time



i = 0
while True:
    try:

        # Initialize the camera
        camera = cv2.VideoCapture(0)
        
        # Capture an image
        return_value, image = camera.read()

        imgName = "outputImages/{:06d}.png".format(i)

        # Save the image
        cv2.imwrite(imgName, image)

        print(f"{imgName} has been written")

        # release the camera
        camera.release()

        # increment the counter
        i += 1

        # wait 10 seconds
        time.sleep(2)
    except KeyboardInterrupt:
        print("Exiting...")
        # Release the camera
        sys.exit()
