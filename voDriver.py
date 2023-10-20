from Car import Car
from Photographer import Photographer
from drive import keyTracker
# from sshkeyboard import listen_keyboard_manual
import time
import math

last_frame = 0
max_fps = 15
## Constant values
speed = 100
drive_time = 2
turn_time = 0.95
pause_time = 0.1


class PoseTracker:
    ## Constant values
    speed = 0.5 #m/s
    turn_speed = 2 #rad/s
    
    #convention: [x_pos, y_pos, z_pos, yaw in rads]
    current_pose = [0, 0, 0, 0]
    last_update = time.time_ns()
    
    def updatePose(self, drive_vector):
        delta_time = time.time_ns() - self.last_update
        self.last_update = time.time_ns()
        
        #update position and angle based on drive_vector
        self.current_pose[0] += self.speed * (delta_time / 1_000_000_000) * math.cos(self.current_pose[3])
        self.current_pose[2] += self.speed * (delta_time / 1_000_000_000) * math.sin(self.current_pose[3])
        #z_pos assumed to not change
        
        self.current_pose[3] += self.turn_speed * (delta_time / 1_000_000_000)
    
    def writePose(self):
        f = open("poses/001.txt", "a")
        f.write("x x x {} x x x {} x x x {}".format(self.current_pose[0], self.current_pose[1], self.current_pose[2]))
        f.close()
        
   
  def trackingSleep(time, FPS, pt, pg, drive_vector):
    entered = time.time_ns()
    while time.time_ns() - entered < (1_000_000_000 * time):
        try:
            pt.updatePose(drive_vector)
            print("updated the pose")
            if (time.time_ns() - last_frame) > (1_000_000_000 // max_fps):
                print("Taking a picture!")
                pg.takePicture()
                pt.writePose()
                last_frame = time.time_ns()
                
        except KeyboardInterrupt:
            print("Exiting...")
            # Release the camera
            sys.exit()
    return
    
    
if __name__ == '__main__':

    pt = PoseTracker()
    pg = Photographer()
    

    car = Car()
    
    ## Navigate in a square
    for i in range(4):
        ## Move Forward
        car.control_car(speed, speed)
        trackingSleep(drive_time, max_fps, pt, pg, [1, 0])
        car.control_car(0, 0)
        # time.sleep(pause_time)
        ## Turn Left
        car.control_car(-speed, speed)
        trackingSleep(turn_time, max_fps, pt, pg, [0, -1])
        car.control_car(0, 0)
        # time.sleep(pause_time)
    
    ## Extra stop just in case
    car.control_car(0, 0)