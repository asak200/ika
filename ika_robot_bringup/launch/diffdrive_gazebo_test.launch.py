import os

from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command, LaunchConfiguration
from launch_ros.parameter_descriptions import ParameterValue
from ament_index_python.packages import get_package_share_path, get_package_share_directory

def generate_launch_description():
    ld = LaunchDescription()

    use_sim_time = LaunchConfiguration('use_sim_time')
    use_ros2_control = LaunchConfiguration('use_ros2_control')

    urdf_file = os.path.join(get_package_share_path('ika_robot_description'),
                             'test_robot_urdf', 'robot.xacro')
    
    gazebo_param_file = os.path.join(get_package_share_path('ika_robot_description'),
                             'config', 'gazebo_params.yaml')
    print("aaa")
    print(urdf_file)
    print("asak")

    gazebo_pkg = get_package_share_directory('gazebo_ros')
    ika_robot_description_dir = get_package_share_directory('ika_robot_description')

    rviz_config = '/home/asak/ika/src/ika_robot_description/config/test_diffdrive.rviz'


    robot_description = ParameterValue(Command(['xacro ', urdf_file, ' use_ros2_control:=', use_ros2_control]), value_type=str)
    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[
            {"robot_description": robot_description}
        ]
    )

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(gazebo_pkg, 'launch', 'gazebo.launch.py')
        ),
        # launch_arguments={'world': os.path.join("path to world share dir")}
        launch_arguments={'extra_gazebo_args': '--ros-args --params-file ' + gazebo_param_file}.items()
    )

    spawner = Node(
        package='gazebo_ros',
        executable='spawn_entity.py', 
        arguments=['-entity', 'my_robot', '-topic', 'robot_description'],
        output='screen'
    )

    diff_drive_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["diff_cont"],
    )
    
    joint_broad_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["joint_broad"],
    )

    rviz2 = Node(
        package='rviz2',
        executable='rviz2',
        arguments=['-d', rviz_config]
    )

    ld.add_action(
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='use sim time if true'
        )
    )
    ld.add_action(
        DeclareLaunchArgument(
            'use_ros2_control',
            default_value='true',
            description='use ros2_control if true'
        )
    )
    ld.add_action(robot_state_publisher)
    ld.add_action(gazebo)
    ld.add_action(spawner)
    ld.add_action(diff_drive_spawner)
    ld.add_action(joint_broad_spawner)
    ld.add_action(rviz2)

    return ld