import os
from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription, actions, conditions
from launch.substitutions.launch_configuration import LaunchConfiguration
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.substitutions import PythonExpression
from launch.launch_description_sources import PythonLaunchDescriptionSource

pkg_hyperion_interrogator = get_package_share_directory('hyperion_interrogator')
pkg_needle_shape_publisher = get_package_share_directory('needle_shape_publisher')


def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            "sim_level_needle_sensing",
            default_value="1",
            description="Simulation level: 1 - hyperrion demo, " +
                "2 - real sensors"
                
        ),
        DeclareLaunchArgument( 'needleParamFile',
                                             description="The shape-sensing needle parameter json file." ),
        IncludeLaunchDescription( # needle shape publisher
             PythonLaunchDescriptionSource(
                os.path.join(pkg_needle_shape_publisher, 'sensorized_shapesensing_needle_decomposed.launch.py')),
                launch_arguments = {'needleParamFile': LaunchConfiguration( 'needleParamFile')}.items()
            ),
        IncludeLaunchDescription( # hyperion demo
            PythonLaunchDescriptionSource(
                os.path.join(pkg_hyperion_interrogator, 'hyperion_demo.launch.py')
                ),
                condition=conditions.IfCondition(
               PythonExpression([LaunchConfiguration('sim_level_needle_sensing'), " == 1"]))
            ),
        IncludeLaunchDescription( # hyperion streamer
            PythonLaunchDescriptionSource(
                os.path.join(pkg_hyperion_interrogator, 'hyperion_streamer.launch.py')
                ),
                condition=conditions.IfCondition(
               PythonExpression([LaunchConfiguration('sim_level_needle_sensing'), " == 2"]))
            ),
       ]) 

# generate_launch_description
