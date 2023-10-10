import cv2

# Initialize the camera
camera = cv2.VideoCapture(0)  # 0 indicates the default camera (Raspberry Pi camera module)

# Set camera resolution (optional)
# camera.set(3, 640)  # Width
# camera.set(4, 480)  # Height

# Capture an image
return_value, image = camera.read()

# Save the image
cv2.imwrite('/home/ubuntu/image_opencv.jpg', image)

# Release the camera
camera.release()