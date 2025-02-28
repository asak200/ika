#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist

class MyNode(Node):

    def __init__(self):
        super().__init__('cmd_pub')
        self.listener_ = self.create_subscription(Twist, 'cmd_vel', self.callback, 1)
        self.pub_ = self.create_publisher(Twist, 'diff_cont/cmd_vel_unstamped', 10)
        self.get_logger().info('cmd_pub node initialized')

    def callback(self, msg):
        self.pub_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
