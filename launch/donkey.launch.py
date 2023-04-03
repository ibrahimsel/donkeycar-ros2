from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='joy',
            node_namespace='joy1',
            node_executable='joy_node',  # type
            name='joy_node'
            # TODO: add respawn= 'true' somehow
        ),
        Node(
            package='tf2_ros',
            node_executable='static_transform_publisher',
            node_name='baselink_to_camera',
            arguments=['0', '0', '0', '0', '0', '0', 'base_link', 'main_camera_optical']
        ),
        Node(
            package='tf2_ros',
            node_executable='static_transform_publisher',
            node_name='baselink_to_laser',
            arguments=['0', '0', '0', '0', '0', '0', 'base_link', 'laser'],
        ),
        Node(
            package='rplidar_ros',
            node_executable='rplidarNode',
            node_name='rplidarNode',
            parameters=''
        )
    ])
