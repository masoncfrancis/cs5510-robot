import cv2
import sys
import time

# Initialize the camera
camera = cv2.VideoCapture(0)  # 0 indicates the default camera (Raspberry Pi camera module)

# Set camera resolution (optional)
# camera.set(3, 640)  # Width
# camera.set(4, 480)  # Height

while True:
    try:
        # Capture an image
        return_value, image = camera.read()
        # Save the image
        cv2.imwrite('testimage_opencv.jpg', image)

        # wait 10 seconds
        time.sleep(10)
    except KeyboardInterrupt:
        # Release the camera
        camera.release()
        sys.exit()
