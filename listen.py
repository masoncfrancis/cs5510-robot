# from pynput import keyboard
# from pynput.keyboard import Key
from sshkeyboard import listen_keyboard

from Car import Car
import time

#usage: first value indicates forward (+) or backward (-), second indicates left (-) or right (+)
#purpose: more natural driving - forward and backward cancel each other, as do left and right, and releasing one key doesn't simply stop the whole car from any and all action. Additionally, allows for simultaneous turning and moving
drive_vector = [0, 0]

# braking = False

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
    # if braking:
        # return
    
    if key == 'w' or key == 'up':
        #forward
        drive_vector[0] += 1
    elif key == 'a' or key == 'left':
        #left
        drive_vector[1] -= 1
    elif key == 's'or key == 'down':
        #backward
        drive_vector[0] -= 1
    elif key == 'd'or key == 'right':
        #right
        drive_vector[1] += 1
    elif key == 'space':
        #force stop
        braking = True
        drive_vector = [0,0]
    drive()

def release_callback(key):
    # if key == 'space':
        # braking = False
    # elif braking:
        # return
    
    if key == 'w' or key == 'up':
        #stop forward
        drive_vector[0] -= 1
    elif key == 'a'or key == 'left':
        #stop left
        drive_vector[1] += 1
    elif key == 's'or key == 'down':
        #stop backward
        drive_vector[0] += 1
    elif key == 'd' or key == 'right':
        #stop right
        drive_vector[1] -= 1
    drive()

# l = keyboard.Listener(on_press=press_callback, on_release=release_callback)
listen_keyboard(on_press=press_callback,on_release=release_callback)
# l.start()
# l.join()