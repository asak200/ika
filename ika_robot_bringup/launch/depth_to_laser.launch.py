from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    ptcl_to_laser = Node(
            package='pointcloud_to_laserscan', executable='pointcloud_to_laserscan_node',
            remappings=[('cloud_in', '/camera/points'),
                        ('scan', 'camera_scan')],
            parameters=[{
                "target_frame": "camera_link",
                "transform_tolerance": 0.01,
                "min_height": -0.9,
                "max_height": .9,
                "angle_min": -0.76,
                "angle_max": 0.76,
                "angle_increment": 0.002371,
                # "angle_increment": 0.00316,
                "scan_time": 0.1,
                "range_min": 0.1,
                "range_max": 8.,
                "use_inf": True,
                "inf_epsilon": 1.0
            }],
            name='pointcloud_to_laserscan',
            # arguments=['--ros-args', '--log-level', 'DEBUG'],
        )
    ld.add_action(ptcl_to_laser)
    return ld