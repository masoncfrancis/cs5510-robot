from fer import FER
import cv2

img = cv2.imread("images/test.jpg")
detector = FER()
result = detector.detect_emotions(img)

print(result)
