import os

from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command, LaunchConfiguration
from launch_ros.parameter_descriptions import ParameterValue
from ament_index_python.packages import get_package_share_path, get_package_share_directory

def generate_launch_description():
    ld = LaunchDescription()

    use_sim_time = LaunchConfiguration('use_sim_time', default=True)
    use_ros2_control = LaunchConfiguration('use_ros2_control', default=True)
    enable_traction = LaunchConfiguration('enable_traction', default=True)

    urdf_file = os.path.join(get_package_share_path('ika_robot_description'),
                             'urdf', 'robot.xacro')

    robot_localization_param = os.path.join(get_package_share_directory('ika_robot_description'),
                                            'config', 'ekf.yaml')

    gazebo_pkg = get_package_share_directory('gazebo_ros')

    world = os.path.join(get_package_share_directory('ika_robot_description'),
                         'worlds', 'new_section6.world')

    rviz_config = '/home/asak/ika/src/ika_robot_description/config/test_diffdrive.rviz'


    robot_description = ParameterValue(Command(['xacro ', urdf_file, ' use_ros2_control:=', use_ros2_control, ' enable_traction:=', enable_traction]), value_type=str)
    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[
            {"robot_description": robot_description}
        ]
    )

    robot_localization = Node(
        package='robot_localization',
        executable='ekf_node',
        name='ekf_node',
        parameters=[
            robot_localization_param,
            {'use_sim_time': use_sim_time},
        ]
    )

    depth_to_laser = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('ika_robot_bringup'), 'launch', 'depth_to_laser.launch.py')
        ),
    )

    dummy_pclaud_listener = Node(
        package='ika_camera',
        executable='dummy_pclaud_listener',
    )

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(gazebo_pkg, 'launch', 'gazebo.launch.py')
        ),
        launch_arguments={'world': world}.items()
    )

    spawner = Node(
        package='gazebo_ros',
        executable='spawn_entity.py', 
        arguments=['-entity', 'aa', 
                   '-topic', 'robot_description',
                #    '-x', '12', '-y', '-8.5', '-z', '1.5',
                   '-x', '5', '-y', '1.5', '-z', '1.5',
                   '-Y', '3.1416'
                   ],
        output='screen'
    )

    if use_ros2_control:
        diff_cont_spawner = Node(
            package='controller_manager',
            executable='spawner',
            arguments=['diff_cont'],
        )
        joint_broad_spawner = Node(
            package='controller_manager',
            executable='spawner',
            arguments=['joint_broad']
        )
        ld.add_action(diff_cont_spawner)
        ld.add_action(joint_broad_spawner)

    rviz2 = Node(
        package='rviz2',
        executable='rviz2',
        arguments=['-d', rviz_config]
    )

    ld.add_action(robot_state_publisher)
    # ld.add_action(robot_localization)
    # ld.add_action(depth_to_laser)
    # ld.add_action(dummy_pclaud_listener)
    ld.add_action(gazebo)
    ld.add_action(spawner)
    ld.add_action(rviz2)

    return ld
