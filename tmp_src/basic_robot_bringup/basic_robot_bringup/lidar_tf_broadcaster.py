#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TransformStamped
import tf2_ros

class LiDARFramePublisher(Node):
  def __init__(self):
    super().__init__('lidar_tf_publisher')
    self.tf_broadcaster = tf2_ros.TransformBroadcaster(self)
    self.timer = self.create_timer(0.1, self.broadcast_transform)
   
  def broadcast_transform(self):
    t = TransformStamped()    
    t.header.stamp = self.get_clock().now().to_msg()
    t.header.frame_id = "base_link"
    t.child_frame_id = "lidar_frame"

    # Position of lidar relative to base_link
    t.transform.translation.x = 0.0
    t.transform.translation.y = 0.0
    t.transform.translation.z = 0.225

    # Orientation (no rotation in this case)
    t.transform.rotation.x = 0.0
    t.transform.rotation.y = 0.0
    t.transform.rotation.z = 0.0
    t.transform.rotation.w = 1.0

    # publish
    self.tf_broadcaster.sendTransform(t) 
    
def main(args=None):
  rclpy.init(args=args)
  node = LiDARFramePublisher()
  rclpy.spin(node)
  rclpy.shutdown()
  
if __name__ == '__main__':
  main()