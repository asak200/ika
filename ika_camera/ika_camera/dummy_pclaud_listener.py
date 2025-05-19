#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from sensor_msgs.msg import PointCloud2, LaserScan, Imu
from geometry_msgs.msg import Twist
from rclpy.qos import QoSProfile, QoSReliabilityPolicy, QoSHistoryPolicy, QoSDurabilityPolicy

from scipy.spatial.transform import Rotation as R


class MyNode(Node):

    def __init__(self):
        super().__init__('dummy_pclaud_listener')
        
        qos_profile = QoSProfile(
            reliability=QoSReliabilityPolicy.BEST_EFFORT,
            durability=QoSDurabilityPolicy.VOLATILE,
            history=QoSHistoryPolicy.KEEP_LAST,
            depth=5
        )
        self.laser_len = []

        listener_ = self.create_subscription(LaserScan, 'camera_scan', self.laser_callback, qos_profile)
        self.listener_ = self.create_subscription(Twist, 'cmd_vel', self.cmd_vel_callback, 10)
        listener_2 = self.create_subscription(PointCloud2, 'camera/points', self.points_callback, 10)
        listener_3 = self.create_subscription(Imu, 'imu', self.imu_callback, 10)
        self.pub_ = self.create_publisher(Twist, 'diff_cont/cmd_vel_unstamped', 10)

        # self.create_timer(0.1, self.timer_callback)

        self.laser: list[float] = None
        self.imu = 0.
        self.get_logger().info('dummy_pclaud_listener node initialized')

    def imu_callback(self, msg: Imu):
        q = msg.orientation
        q = [q.x, q.y, q.z, q.w]
        r = R.from_quat(q)
        self.imu = r.as_euler('xyz', degrees=True)[0]


    def laser_callback(self, msg: LaserScan):
        self.laser_len = msg.ranges

    def points_callback(self, msg: PointCloud2):
        self.point_len = msg.row_step // msg.point_step
        self.point_len = len(msg.data)

    def cmd_vel_callback(self, msg):
        self.pub_.publish(msg)
        pass

    def timer_callback(self):
        self.get_logger().info(str(len(self.laser_len)))
        


def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
