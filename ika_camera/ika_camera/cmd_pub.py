#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist
from tf2_ros import TransformListener, Buffer, tf2_ros

class MyNode(Node):

    def __init__(self):
        super().__init__('cmd_pub')
        # self.listener_ = self.create_subscription(Twist, 'cmd_vel', self.callback, 1)
        # self.pub_ = self.create_publisher(Twist, 'diff_cont/cmd_vel_unstamped', 10)
        self.timer_ = self.create_timer(0.01, self.callback)
        self.get_logger().info('cmd_pub node initialized')

    def callback(self):
        # self.pub_.publish(msg)
        # transform_stamped = TransformListener.lookupTransform(target_frame_, cloud_msg->header.frame_id, tf2::TimePointZero)
        tf2_ = Buffer()
        a = tf2_.lookup_transform('camera_link_optical', 'camera_link')
        print(a)


def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
