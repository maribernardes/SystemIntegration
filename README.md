Smart Needle System Integration
===============================

Overview
--------

This is the main repository of the Smart Needle project. This repository contains:

- Specification of the system (see [System Overview](#overview))
- ROS master launch file (see [Installation](#installation) and [Usage](#usage))

System Overview <a name="overview"></a>
---------------

Please refer to the [System Architecture Page](Documents/index.md) for the detail.


Installation <a name="installation"></a>
------------
The following steps were tested on:
- Ubuntu 20.4 + ROS2 Foxy

First, install ROS 2 following the ROS 2 Documentation and create your ROS2 workspace following the documentation as follows:
```bash
source /opt/ros/foxy/setup.bash
mkdir -p ~/dev_ws/src
cd ~/dev_ws/
rosdep install -i --from-path src --rosdistro foxy -y # Make sure to resolve dependency
```
Then, clone the following repositories into the src folder of your ROS2 workspace: SystemIntegration, NeedleGuide, trajcontrol, ros2_needle_shape_publisher and ros2_hyperion_interrogator. 
```bash
cd ~/dev_ws/src
git clone https://github.com/SmartNeedle/SystemIntegration.git
git clone https://github.com/SmartNeedle/NeedleGuide.git
git clone https://github.com/SmartNeedle/trajcontrol.git
git clone https://github.com/SmartNeedle/ros2_needle_shape_publisher.git
git clone https://github.com/SmartNeedle/ros2_hyperion_interrogator.git
```
You also need to install the potentially missing requirements:
- Download the python requirements in the `ros2_needle_shape_publisher` repo by running the command in the `ros2_needle_shape_publisher` cloned repo directory
```bash
cd ~/dev_ws/src/ros2_needle_shape_publisher
pip install -r ./requirements.txt
```
- You might need to install control-msgs using:
```bash
sudo apt install ros-foxy-control-msgs
```
OR manullay by cloning repository: https://github.com/ros-controls/control_msgs/tree/foxy-devel
into the workspace 

- Install following python dependencies
```bash
python3 -m pip install numpy-quaternion
pip install transforms3d
```

Lastly, build the workspace using: 
```bash
cd ~/dev_ws/
colcon build --symlink-install
```

Usage <a name="usage"></a>
-----

To run simulation:(Put every simulation level to 1)
```bash
ros2 launch system_bringup system.launch.py sim_level:=1 sim_level_needle_sensing:=1 sim_level_trajcontrol:=1 ip:=<demo IP address of the interrogator> numCHs:=<number of FBG channels> numAAs:=<number of FBG active areas per channel> needleParamFile:=<sensorized needle parameter JSON file path>
```
To run with real hardware: (Put every simulation level to 2)
```bash
ros2 launch system_bringup system.launch.py sim_level:=2 sim_level_needle_sensing:=2 sim_level_trajcontrol:=2 ip:=<demo IP address of the interrogator> needleParamFile:=<sensorized needle parameter JSON file path>
```
### Simulation arguments for each module:
Needle Guide:
- *sim_level:=0* : Emulated (dummy nodes) stage and sensors only
- *sim_level:=1* : Virtual stage and sensors, simulated in Gazebo (Not yet fully implemented)
- *sim_level:=2* : Physical stage and sensors (Depth and rotation sensors currently only emulated)
- *sim_level:=3* : Both virtual and physical sensors

Shape-Sensing Needle Node:
- *sim_level_needle_sensing:=1* : Launches the demo node: hyperion_demo.launch.py
- *sim_level_needle_sensing:=2* :Launches the actual hardware interface node: hyperion_streamer.launch.py

Trajectory control:
- *sim_level_trajcontrol:=1* : for system integration demo
- *sim_level_trajcontrol:=2* : for real nodes

### Launching Shape-Sensing Needle Node
First, you need to download the python requirements in the `ros2_needle_shape_publisher` repo by running the command in the `ros2_needle_shape_publisher` cloned repo directory
```
pip install -r ./requirements.txt
```

1. Launch the FBG interrogator node to gather the sensor readings:

For the demo node: 
```bash
ros2 launch hyperion_interrogator hyperion_demo.launch.py ip:=<demo IP address of the interrogator> numCH:=<number of FBG channels> numAA:=<number of FBG active areas per channel> 
```
For the actual hardware interface node
    
```bash
ros2 launch hyperion_interrogator hyperion_streamer.launch.py ip:=<demo IP address of the interrogator> 
```
2. (If connected to hardware) Ensure that the sensorized needle is straight to prepare for sensor calibration
3. Perform sensor calibration by launching the `calibrate_sensors` node

```bash
ros2 run hyperion_interrogator calibrate_sensors --ros-args -r __ns:=/needle
```

4. Launch the (multi-threaded) shape sensing node. (Look at the *ros2_needle_shape_publisher* README for information on the parameters)

```bash
ros2 launch needle_shape_publisher sensorized_shapesensing_needle_decomposed.launch.py needleParamFile:=path/to/needle_params.json numSignals:=200 optimMaxIterations:=15
```

