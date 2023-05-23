#!/usr/bin/python3
import rclpy
import math
from rclpy.node import Node

from std_msgs.msg import String
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

from rclpy.qos import QoSProfile
from rclpy.qos import qos_profile_sensor_data

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('lidar_detect')
        self.publisher = self.create_publisher(Twist, 'cmd_vel',10)
        self.get_logger().info("Not Close Obstacle, Let move")
        self.timers = self.create_timer(0.1,self.kick)

    def kick(self):
         self.get_logger().info("kick")




def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

 
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()