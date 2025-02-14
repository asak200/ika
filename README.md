Hello!

Run `ros2 launch ika_robot_bringup ika_gazebo.launch.py enable_traction:=True` to run the simulation.

Set `enable_traction:=False` to spawn the odometry-friendly version.

Don't forget `ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r /cmd_vel:=/diff_cont/cmd_vel_unstamped`
