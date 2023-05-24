# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import String


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        timer_period = 0.5  # seconds
        timer_run = 0.01
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.kick = self.create_timer(timer_run, self.kickball)
        self.i = 0
        self.velocity_publisher = self.create_publisher(Twist,'cmd_vel',10)
        self.get_logger().info('Prepare to kick')
        self.velocity = 0.0
        
    def kickball(self):
        vel_msg = Twist()

        if(self.i > 4.5):
            self.velocity = 0.0
            vel_msg.linear.x = self.velocity
            self.velocity_publisher.publish(vel_msg) 
            self.get_logger().info('Change Velocity to "%f"' % self.velocity)
            rclpy.shutdown()
        elif(self.i > 2.0):
            self.velocity = 0.2
             
        elif(self.i > 0):
            self.velocity = -0.05
            
        vel_msg.linear.x = self.velocity
        self.velocity_publisher.publish(vel_msg) 
        self.get_logger().info('Change Velocity to "%f"' % self.velocity)



    def timer_callback(self):
        msg = String()
        msg.data = 'Timer: %f' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 0.5

        


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
