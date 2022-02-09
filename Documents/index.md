System Architecture
===================

System Diagram
--------------

![alternative text](http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.github.com/SmartNeedle/SystemIntegration/main/Documents/system_diagram.txt)

Old diagram can be found on [Miro](https://miro.com/welcomeonboard/MEpValZOZnhVNVEzejczRWxhb0hpWUJZbVVZQThjS1Qxa0llTnRRdUVpM0ZudG5nc2ROakY0ZzFqemxSRjdQN3wzMDc0NDU3MzQ5OTI1NjQwNzA3?invite_link_id=26421202184)


List of ROS Messages
--------------------

|Component   |Topic                        |Message  Type                 |Description                                                                                                                                                                    |Coordinate Frame|
|------------|-----------------------------|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|
|UI          |/subject/state/skin_entry    |geometry_msgs/msg/Point       |The needle entry point on the skin; measured by intraoperative images.                                                                                                         |Stage           |
|            |/subject/state/target        |geometry_msgs/msg/Point       |The target point in the subject; defined on intraoperative images.                                                                                                             |Stage           |
|            |/stage/cmd/parameters        |std_msgs/msg/String           |TBD                                                                                                                                                                            |                |
|            |/stage/cmd/control           |std_msgs/msg/String           |TBD                                                                                                                                                                            |                |
|Compensation|/needle/state/skin_entry     |geometry_msgs/msg/Point       |The needle entry point on the skin in the needle coordinate frame                                                                                                              |Needle          |
|            |/needle/cmd/pose             |geometry_msgs/msg/Pose        |The desired needle pose in the needle coordinate frame. In this implementation, the pose is defined only by the needle insertion length (Z) and the rotation about the Z-axis. |Needle          |
|            |/stage/cmd/pose              |geometry_msgs/msg/Pose        |The desired stage pose in the stage coordinate frame. In this implementation, the pose is defined only by x- and y- translations. (ztranslation and rotations are zero).       |Stage           |
|            |/needle/compensation/delta   |geometry_msgs/msg/Pose        |The desired shift of the stage to compensate for the current deviation. In this implementation, the shift is defined only by x- and ytranslations.                             |Needle          |
|Shape model |/needle/state/predicted_shape|geometry_msgs/msg/PoseArray   |The predicted needle shape as an array of positions and directions (i.e., poses) of needle sections (0.5-mm increment). **Not Implemented**                                    |Stage          |
|            |/needle/state/current_shape  |geometry_msgs/msg/PoseArray   |The estimated needle shape as an array of positions and directions (i.e., poses) of needle sections (0.5-mm increment).                                                        |Stage          |
|            |/needle/sensor/raw           |std_msgs/msg/Float64MultiArray|Raw FBG sensor data                                                                                                                                                            |Needle             |
|            |/needle/sensor/processed     |std_msgs/msg/Float64MultiArray|Processed FBG sensor data                                                                                                                                                      |Needle           |
|            |/needle/state/curvatures     |std_msgs/msg/Float64MultiArray|Curvatures measured from each of the active areas.                                                                                                                             |Needle
|Stage       |/needle/state/pose           |geometry_msgs/msg/Pose        |The needle pose. In this implementation, the pose is defined only by the needle insertion length (z) and the rotation about the z-axis.                                        |Needle          |
|            |/stage/state/needle_pose     |geometry_msgs/msg/Pose        |The needle pose in the stage coordinate frame. In this implementation, the pose is defined only by the needle insertion length (z) and the rotation about the z-axis.          |Stage           |
|            |/stage/state/pose            |geometry_msgs/msg/Pose        |The pose of the stage. In this implementation, the pose is defined only by x- and y- translations. (z-translation and rotations are zero).                                     |Stage           |


Coordinate Systems
------------------


