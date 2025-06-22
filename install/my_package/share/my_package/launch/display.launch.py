from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, Command, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            name='use_sim_time', default_value='false',
            description='Use simulation (Gazebo) clock if true'),

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            parameters=[{
                'use_sim_time': LaunchConfiguration('use_sim_time'),
                'robot_description': Command([
                    'xacro ',
                    PathJoinSubstitution([
                        FindPackageShare('my_package'),
                        'urdf',
                        'robot_arm.urdf.xacro'
                    ])
                ])
            }]
        ),

        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', PathJoinSubstitution([
                FindPackageShare('my_package'),
                'urdf',
                'view.rviz'  # optional: your RViz config
            ])]
        )
    ])
