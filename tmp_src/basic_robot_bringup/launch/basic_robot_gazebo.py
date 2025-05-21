from launch import LaunchDescription
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution, Command
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription

def generate_launch_description():
    ld = LaunchDescription()

    # find path to package
    basic_robot_description_pkg_path = FindPackageShare('basic_robot_description')
    basic_robot_bringup_pkg_path = FindPackageShare('basic_robot_bringup')

    # join paths together
    urdf_path = PathJoinSubstitution([basic_robot_description_pkg_path, 'urdf', 'example.urdf.xacro'])

    # publish tf
    robot_state_publisher_node = Node(
            package="robot_state_publisher",
            executable="robot_state_publisher",
            parameters=[{
                "robot_description": Command(['xacro',' ', urdf_path])
            }]
        )
    ld.add_action(robot_state_publisher_node)
    
    # launch gazebo using gazebo launch file
    ld.add_action(IncludeLaunchDescription(
        PathJoinSubstitution([FindPackageShare('gazebo_ros'), 'launch', 'gazebo.launch.py']),
        launch_arguments={
            # "world": PathJoinSubstitution([basic_robot_bringup_pkg_path, 'worlds', 'lidar.world']),
            "use_sim_time": "true"
        }.items()
    ))
    
    # spawn the robot in gazebo
    spawn_entity_node = Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            output='screen',
            arguments=['-topic', 'robot_description', '-entity', 'my_robot']
        )
    ld.add_action(spawn_entity_node)
    
    # launch rviz
    rviz_config_path = PathJoinSubstitution([basic_robot_bringup_pkg_path, 'rviz', 'urdf.rviz'])
    rviz2_node = Node(
            package="rviz2", 
            executable="rviz2",
            output="screen",
            arguments=["-d", rviz_config_path]
        )
    ld.add_action(rviz2_node)
    

    return ld
