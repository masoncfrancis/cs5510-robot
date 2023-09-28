from pynput import keyboard
from pynput.keyboard import Key

from Car import Car
import time

#usage: first value indicates forward (+) or backward (-), second indicates left (-) or right (+)
#purpose: more natural driving - forward and backward cancel each other, as do left and right, and releasing one key doesn't simply stop the whole car from any and all action. Additionally, allows for simultaneous turning and moving
drive_vector = [0, 0]

speed = 100

def drive():
    if drive_vector[0] > 0:
        if drive_vector[1] == 0:
            #directly forward
            car.control_car(speed, speed)
        elif drive_vector[1] > 0:
            #forward and right
            car.control_car(speed, 0)
        else:
            #forward and left
            car.control_car(0, speed)
    elif drive_vector[0] < 0:
        if drive_vector[1] == 0:
            #directly backward
            car.control_car(-speed, -speed)
        elif drive_vector[1] > 0:
            #backward and right
            car.control_car(-speed, 0)
        else:
            #backward and left
            car.control_car(0, -speed)
    else:
        if drive_vector[1] == 0:
            #no motion
            car.control_car(0, 0)
        elif drive_vector[1] > 0:
            #only right
            car.control_car(speed, -speed)
        else:
            #only left
            car.control_car(-speed, speed)


def press_callback(key):
    try:
        # print('alphanumeric key {} pressed'.format(key.char))
        if key.char == 'w':
            #forward
            drive_vector[0] += 1
        elif key.char == 'a':
            #left
            drive_vector[1] -= 1
        elif key.char == 's':
            #backward
            drive_vector[0] -= 1
        elif key.char == 'd':
            #right
            drive_vector[1] += 1
        else:
            print("invalid action")
    except AttributeError:
        if key == Key.up:
            #forward
            drive_vector[0] += 1
        elif key == Key.down:
            #backward
            drive_vector[0] -= 1
        elif key == Key.right:
            #right
            drive_vector[1] += 1
        elif key == Key.left:
            #left
            drive_vector[1] -= 1
        elif key == Key.esc:
            #stop the car
            drive_vector = [0, 0]
            print('quiting...')
        else:
            print("invalid action")
    drive()

def release_callback(key):
    # print('{} released'.format(key))
    try:
        if key.char in ['w','a','s','d']:
            if key.char == 'w':
            #stop forward
            drive_vector[0] -= 1
        elif key.char == 'a':
            #stop left
            drive_vector[1] += 1
        elif key.char == 's':
            #stop backward
            drive_vector[0] += 1
        elif key.char == 'd':
            #stop right
            drive_vector[1] -= 1
    except AttributeError:
        if key == Key.up:
            #stop forward
            drive_vector[0] -= 1
        elif key == Key.down:
            #stop backward
            drive_vector[0] += 1
        elif key == Key.right:
            #stop right
            drive_vector[1] -= 1
        elif key == Key.left:
            #stop left
            drive_vector[1] += 1
    drive()
    if key == Key.esc:
        return False

l = keyboard.Listener(on_press=press_callback, on_release=release_callback)
l.start()
l.join()