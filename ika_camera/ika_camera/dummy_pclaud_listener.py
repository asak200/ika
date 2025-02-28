#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from sensor_msgs.msg import PointCloud2

class MyNode(Node):

    def __init__(self):
        super().__init__('dummy_pclaud_listener')
        listener_ = self.create_subscription(PointCloud2, 'camera/points', self.callback, 1)
        self.get_logger().info('dummy_pclaud_listener node initialized')

    def callback(self, msg):
        pass


def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
