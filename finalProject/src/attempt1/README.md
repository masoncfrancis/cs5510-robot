To run the camera module, we just used the v4l2 camera node.
It can be run with the following command:

`ros2 run v4l2_camera v4l2_camera_node --ros-args -p image_size:="[640,480]"`

the project doesn't need any dependencies other than those needed for Taylor's guide.

To run everything. Run the following commands from the src folder:
1. `colcon build`
2. `cp -r attempt1/launch/ install/attempt1/share/attempt1/launch/`
3. `ros2 launch attempt1 launch.py`