colcon build --symlink-install --base-paths src/

source install/setup.bash

# ros2 launch basic_robot_bringup basic_robot_gazebo.py