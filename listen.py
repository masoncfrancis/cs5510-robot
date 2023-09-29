# from pynput import keyboard
# from pynput.keyboard import Key
from sshkeyboard import listen_keyboard

from Car import Car
import time

class keyTracker:
    #drive_vector usage: first value indicates forward (+) or backward (-), second indicates left (-) or right (+)
    #purpose: more natural driving - forward and backward cancel each other, as do left and right, and releasing one key doesn't simply stop the whole car from any and all action. Additionally, allows for simultaneous turning and moving
    drive_vector = [0, 0]
    braking = False
    speed = 100
    car = Car()

    def drive(self):
        if self.drive_vector[0] > 0:
            if self.drive_vector[1] == 0:
                #directly forward
                car.control_car(self.speed, self.speed)
            elif self.drive_vector[1] > 0:
                #forward and right
                car.control_car(self.speed, 0)
            else:
                #forward and left
                car.control_car(0, self.speed)
        elif self.drive_vector[0] < 0:
            if self.drive_vector[1] == 0:
                #directly backward
                car.control_car(-self.speed, -self.speed)
            elif self.drive_vector[1] > 0:
                #backward and right
                car.control_car(-self.speed, 0)
            else:
                #backward and left
                car.control_car(0, -self.speed)
        else:
            if self.drive_vector[1] == 0:
                #no motion
                car.control_car(0, 0)
            elif self.drive_vector[1] > 0:
                #only right
                car.control_car(self.speed, -self.speed)
            else:
                #only left
                car.control_car(-self.speed, self.speed)


    def press_callback(self, key):
        if self.braking:
            return
        
        if key == 'w' or key == 'up':
            #forward
            self.drive_vector[0] += 1
        elif key == 'a' or key == 'left':
            #left
            self.drive_vector[1] -= 1
        elif key == 's'or key == 'down':
            #backward
            self.drive_vector[0] -= 1
        elif key == 'd'or key == 'right':
            #right
            self.drive_vector[1] += 1
        elif key == 'space':
            #force stop
            self.braking = True
            self.drive_vector = [0,0]
        self.drive()

    def release_callback(self, key):
        if key == 'space':
            self.braking = False
        elif self.braking:
            return
        
        if key == 'w' or key == 'up':
            #stop forward
            self.drive_vector[0] -= 1
        elif key == 'a'or key == 'left':
            #stop left
            self.drive_vector[1] += 1
        elif key == 's'or key == 'down':
            #stop backward
            self.drive_vector[0] += 1
        elif key == 'd' or key == 'right':
            #stop right
            self.drive_vector[1] -= 1
        self.drive()

k = keyTracker()
listen_keyboard(on_press=k.press_callback,on_release=k.release_callback)