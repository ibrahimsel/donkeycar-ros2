from launch import LaunchDescription
from launch_ros.actions import Node

# parameters_file_name = 'config.yaml'


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
            output="screen",
            parameters=[
                {'serial_port': '/dev/ttyUSB0'},
                {'serial_baudrate': '115200'},
                {'frame_id': 'laser'},
                {'inverted': 'false'},
                {'angle_compensate': 'true'}
            ]
        )
    ])
