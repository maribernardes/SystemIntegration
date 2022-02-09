System Architecture
===================

System Diagram
--------------

![alternative text](http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.github.com/SmartNeedle/SystemIntegration/main/Documents/system_diagram.txt)

Old diagram can be found on [Miro](https://miro.com/welcomeonboard/MEpValZOZnhVNVEzejczRWxhb0hpWUJZbVVZQThjS1Qxa0llTnRRdUVpM0ZudG5nc2ROakY0ZzFqemxSRjdQN3wzMDc0NDU3MzQ5OTI1NjQwNzA3?invite_link_id=26421202184)


List of ROS Messages
--------------------

|Component   |Topic                        |Message  Type              |Description                                                                                                                                                                    |Coordinate Frame|
|------------|-----------------------------|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|
|UI          |/subject/state/skin_entry    |geometry_msgs/msg/Point    |The needle entry point on the skin; measured by intraoperative images.                                                                                                         |Stage           |
|            |/subject/state/target        |geometry_msgs/msg/Point    |The target point in the subject; defined on intraoperative images.                                                                                                             |Stage           |
|            |/stage/cmd/parameters        |std_msgs/msg/String        |TBD                                                                                                                                                                            |                |
|            |/stage/cmd/control           |std_msgs/msg/String        |TBD                                                                                                                                                                            |                |
|            |/needle/state/skin_entry     |geometry_msgs/msg/Point    |The needle entry point on the skin in the needle coordinate frame                                                                                                              |Needle          |
|Compensation|/move_stage - This is not a topic but an Action message              |stage_control_interfaces/action/MoveStage     |The desired stage pose in the stage coordinate frame. In this implementation, the pose is defined only by x- and z- translations, while y-translation (insertion depth) and rotations are zero.      |Stage           |
|Shape model |/needle/state/predicted_shape|geometry_msgs/msg/PoseArray|The predicted needle shape as an array of positions and directions (i.e., poses) of needle sections (5-mm increment).                                                          |Needle          |
|            |/needle/state/shape          |geometry_msgs/msg/PoseArray|The estimated needle shape as an array of positions and directions (i.e., poses) of needle sections (5-mm increment).                                                          |Needle          |
|            |/sensor/state/raw            |TBD                        |Raw FBG sensor data                                                                                                                                                            |N/A             |
|            |/sensor/state/raw            |TBD                        |Processed FBG sensor data                                                                                                                                                      |N/A             |
|Stage       |/needle/state/pose           |geometry_msgs/msg/Pose     |The needle pose. In this implementation, the pose is defined only by the needle insertion length (z) and the rotation about the z-axis.                                        |Needle          |
|            |/stage/state/needle_pose     |geometry_msgs/msg/Pose     |The needle pose in the stage coordinate frame. In this implementation, the pose is defined only by the needle insertion length (z) and the rotation about the z-axis.          |Stage           |
|            |/stage/state/pose            |geometry_msgs/msg/Pose     |The pose of the stage. In this implementation, the pose is defined only by x- and y- translations. (z-translation and rotations are zero).                                     |Stage           |


Coordinate Systems
------------------


