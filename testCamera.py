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

        imgName = "{:06d}.png".format(i)

        # Save the image
        cv2.imwrite(imgName, image)

        print(f"{imgName} has been written")

        # wait 10 seconds
        time.sleep(10)
    except KeyboardInterrupt:
        print("Exiting...")
        # Release the camera
        camera.release()
        sys.exit()
