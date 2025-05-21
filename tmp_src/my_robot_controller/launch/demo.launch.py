from launch import LaunchDescription
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription

def generate_launch_description():
  ld = LaunchDescription()
  pkg_path = FindPackageShare('my_robot_controller')
  default_model_path = PathJoinSubstitution(['urdf', 'my_robot.urdf.xacro'])
  default_rviz_config_path = PathJoinSubstitution([pkg_path, 'rviz', 'urdf.rviz'])
  
  # arguments to the launch file
  gui_arg = DeclareLaunchArgument(name='gui', default_value='true', choices=['true', 'false'],
                                      description='Flag to enable joint_state_publisher_gui')
  ld.add_action(gui_arg)
  
  rviz_arg = DeclareLaunchArgument(name='rvizconfig', default_value=default_rviz_config_path,
                                     description='Absolute path to rviz config file')
  ld.add_action(rviz_arg)
  
  ld.add_action(DeclareLaunchArgument(name='model', default_value=default_model_path,
                                        description='Path to robot urdf file relative to the package'))
  # Include Another Launch File
  ld.add_action(IncludeLaunchDescription(
        PathJoinSubstitution([FindPackageShare('urdf_launch'), 'launch', 'display.launch.py']),
        launch_arguments={
            'urdf_package': 'my_robot_controller',
            'urdf_package_path': LaunchConfiguration('model'),
            'rviz_config': LaunchConfiguration('rvizconfig'),
            'jsp_gui': LaunchConfiguration('gui')}.items()
    ))

  return ld