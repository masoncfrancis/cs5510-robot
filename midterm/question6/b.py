from fer import FER
import cv2
from fer.utils import draw_annotations


# Resources to learn how to write this code came from FER documentation and examples

detector = FER()
capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()

    frame = cv2.flip(frame, 1)

    emotions = detector.detect_emotions(frame)
    frame = draw_annotations(frame, emotions)

    cv2.imshow("frame", frame)
    if cv2.waitKey(1) == ord("q"):
        break

capture.release()
cv2.destroyAllWindows()

