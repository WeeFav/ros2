from setuptools import find_packages, setup

package_name = 'basic_robot_bringup'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (f'share/{package_name}/launch', ['launch/basic_robot_gazebo.py']),
        (f'share/{package_name}/worlds', ['worlds/lidar.world']),
        (f'share/{package_name}/maps', ['maps/my_map.pgm', 'maps/my_map.yaml']),
        (f'share/{package_name}/rviz', ['rviz/nav2_default_view.rviz', 'rviz/urdf.rviz']),
        (f'share/{package_name}/rviz', ['rviz/nav2_default_view.rviz', 'rviz/urdf.rviz']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='marvin',
    maintainer_email='marvin@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
          "lidar_tf_broadcaster = basic_robot_bringup.lidar_tf_broadcaster:main",
          "lidar_tf_broadcaster_go2 = basic_robot_bringup.lidar_tf_broadcaster_go2:main",
        ],
    },
)
