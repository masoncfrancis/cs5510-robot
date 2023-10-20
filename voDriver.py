# from Car import Car
from Photographer import Photographer
from drive import keyTracker
from sshkeyboard import listen_keyboard
import time

class PoseTracker:
    ## Constant values
    speed = 0.5 #m/s
    turn_speed = 2 #rad/s
    
    #convention: [x_pos, y_pos, z_pos, yaw in rads]
    current_pose = [0, 0, 0, 0]
    last_update = time.time_ns()
    
    def updatePose(self, drive_vector):
        delta_time = time.time_ns() - last_update
        last_update = time.time_ns()
        
        #update position and angle based on drive_vector
        current_pose[0] += self.speed * (delta_time / 1_000_000_000) * math.cos(current_pose[3])
        current_pose[2] += self.speed * (delta_time / 1_000_000_000) * math.sin(current_pose[3])
        #z_pos assumed to not change
        
        current_pose[3] += self.turn_speed * (delta_time / 1_000_000_000)
    
    def writePose():
        f = open("poses/001.txt", "a")
        f.write("x x x {} x x x {} x x x {}".format(current_pose[0], current_pose[1], current_pose[2]))
        f.close()
        
    
    
if __name__ == '__main__':
    k = keyTracker()
    print("Printing does work, right?")
    listen_keyboard(on_press=k.press_callback,on_release=k.release_callback)
    print("I made it this far")
    pt = PoseTracker()
    pg = Photographer()
    
    max_fps = 20
    
    #take pictures at max rate of max_fps
    last_frame = 0
    while True:
        try:
            pt.updatePose(k.drive_vector)
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