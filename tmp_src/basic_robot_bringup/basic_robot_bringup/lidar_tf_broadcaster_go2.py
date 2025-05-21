#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TransformStamped
import tf2_ros

class LiDARFramePublisher(Node):
  def __init__(self):
    super().__init__('lidar_tf_publisher_go2')
    self.tf_broadcaster = tf2_ros.TransformBroadcaster(self)
    self.timer = self.create_timer(0.001, self.broadcast_transform)
   
  def broadcast_transform(self):
    t = TransformStamped()    
    t.header.stamp = self.get_clock().now().to_msg()
    t.header.frame_id = "base_link"
    t.child_frame_id = "velodyne_base_link"

    # Position of lidar relative to base_link
    t.transform.translation.x = 0.2
    t.transform.translation.y = 0.0
    t.transform.translation.z = 0.08

    # Orientation (no rotation in this case)
    t.transform.rotation.x = 0.0
    t.transform.rotation.y = 0.0
    t.transform.rotation.z = 0.0
    t.transform.rotation.w = 1.0
    
    t2 = TransformStamped()    
    t2.header.stamp = self.get_clock().now().to_msg()
    t2.header.frame_id = "velodyne_base_link"
    t2.child_frame_id = "velodyne"

    # Position of lidar relative to base_link
    t2.transform.translation.x = 0.0
    t2.transform.translation.y = 0.0
    t2.transform.translation.z = 0.0377

    # Orientation (no rotation in this case)
    t2.transform.rotation.x = 0.0
    t2.transform.rotation.y = 0.0
    t2.transform.rotation.z = 0.0
    t2.transform.rotation.w = 1.0

    # publish
    self.tf_broadcaster.sendTransform(t) 
    self.tf_broadcaster.sendTransform(t2) 
    
def main(args=None):
  rclpy.init(args=args)
  node = LiDARFramePublisher()
  rclpy.spin(node)
  rclpy.shutdown()
  
if __name__ == '__main__':
  main()