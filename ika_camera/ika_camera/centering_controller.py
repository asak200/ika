#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist, Quaternion
from sensor_msgs.msg import Image, Imu

import cv2
from cv_bridge import CvBridge
import numpy as np
import math
from tf_transformations import euler_from_quaternion

class MyNode(Node):
    def __init__(self):
        super().__init__('centering_controller')

        self.declare_parameter('edit_img', True)
        self.declare_parameter('pub_cmd_vel', True)
        self.edit_img = self.get_parameter('edit_img').value
        self.pub_cmd_vel = self.get_parameter('pub_cmd_vel').value
        
        self.cv_bridge = CvBridge()
        self.kp = .3
        self.angle_x = 0

        self.cmd_vel_publisher_ = self.create_publisher(Twist, 'diff_cont/cmd_vel_unstamped', 10)
        self.imu_subscriber_ = self.create_subscription(Imu, 'imu', self.imu_callback, 10)

        self.depth_subscriber_ = self.create_subscription(Image, 'camera/depth/image_raw', self.depth_image_callback, 10)
        # self.image_subscriber_ = self.create_subscription(Image, 'camera/image_raw', self.image_callback, 10)
        self.depth_publisher_ = self.create_publisher(Image, 'camera/depth/edited_image', 10)
        # self.image_publisher_ = self.create_publisher(Image, 'camera/edited_image', 10)

        self.get_logger().info("centering_controller node initialized")

    def depth_image_callback(self, msg: Image):
        img = self.cv_bridge.imgmsg_to_cv2(msg, desired_encoding='32FC1')

        y = 240 + round(math.sin((self.angle_x)) * (img.shape[1]/2-10))
        x = 320 - round(math.cos((self.angle_x)) * (img.shape[1]/2-10))

        # Calculate error
        left = img[y + 30, x] 
        right = img[abs(y-img.shape[0])+30, img.shape[1] - x]
        front = img[270, 320] / 8.
        sum_ = left + right
        error = (left - right)

        # self.get_logger().info('left = ' + str(left))
        # self.get_logger().info('right = ' + str(right))
        # self.get_logger().info(str(error))
        # self.get_logger().info(str(img.shape[0]))
        # self.get_logger().info('x= ' + str(x))
        # self.get_logger().info('y= ' + str(y))
        
        # Publish velocity
        cmd_vel = Twist()
        cmd_vel.linear.x = 1.2
        if left < 1.5 or right < 1.5:
            angular_z = error * self.kp
            cmd_vel.angular.z = angular_z
        if self.pub_cmd_vel:
            self.cmd_vel_publisher_.publish(cmd_vel)

        # Draw a square on the areas you're comparing
        if not self.edit_img:
            return
        img = self.draw_square(img, (y + 30, x))
        img = self.draw_square(img, (abs(y-img.shape[0])+30, img.shape[1] - x))

        new_msg = self.cv_bridge.cv2_to_imgmsg(img, encoding="32FC1") 

        new_msg.header.stamp = self.get_clock().now().to_msg()
        new_msg.header.frame_id = 'camera_link_optical'
        self.depth_publisher_.publish(new_msg)

    def draw_square(self, mat_like: np.ndarray, cinter: tuple[int]):
        for i in range(10):
            for j in range(10):
                mat_like[cinter[0]-5 + i, cinter[1]-5 + j] = 8.
        return mat_like

    def image_callback(self, img_msg: Image):
        img = self.cv_bridge.imgmsg_to_cv2(img_msg, desired_encoding='bgr8')
        # self.get_logger().info(str(len(img[0, 0])))

        cv2.circle(img, (10, 270), 10, (255,0,0), -1)
        cv2.circle(img, (640-10, 270), 10, (255,0,0), -1)

        new_msg = self.cv_bridge.cv2_to_imgmsg(img, encoding="rgb8") 

        new_msg.header.stamp = self.get_clock().now().to_msg()
        new_msg.header.frame_id = 'camera_link_optical'

        self.image_publisher_.publish(new_msg)

    def imu_callback(self, msg: Imu):
        q: Quaternion = msg.orientation
        angles = euler_from_quaternion([q.x, q.y, q.z, q.w])
        self.angle_x = angles[0]
        print(math.degrees(angles[2]))


def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
