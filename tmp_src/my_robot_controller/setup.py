from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'my_robot_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/my_robot_controller/launch', ['launch/demo.launch.py']),
        ('share/my_robot_controller/urdf', ['urdf/my_robot.urdf.xacro', 'urdf/common_properties.xacro', 'urdf/mobile_base.xacro']),
        ('share/my_robot_controller/rviz', ['rviz/urdf.rviz']),
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
        ],
    },
)
