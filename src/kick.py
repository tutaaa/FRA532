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
        self.subscription = self.create_subscription(
            LaserScan,
            'scan',
            self.listener_callback,
            qos_profile=qos_profile_sensor_data)
        self.subscription
        self.publisher = self.create_publisher(Twist, 'cmd_vel',10)
        self.get_logger().info("Not Close Obstacle, Let move")




def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

 
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()