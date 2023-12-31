#!/usr/bin/env python2

import rospy
from sensor_msgs.msg import JointState
import moveit_commander
import numpy as np
import tf2_ros
from geometry_msgs.msg import Pose
from copy import deepcopy

JOINT_NAMES = [
    'shoulder_pan_joint',
    'shoulder_lift_joint',
    'elbow_joint',
    'wrist_1_joint',
    'wrist_2_joint',
    'wrist_3_joint'
]

HOME_JOINTS = [0.0, -1.57, -1.57, 0, 0.0, 0.0]

if __name__ == '__main__':
    rospy.init_node('moveit_programmer')

    joint_pub = rospy.Publisher('/move_group/fake_controller_joint_states', JointState, queue_size=10)
    rospy.sleep(0.1)

    N_MOTIONS = 5

    init_joints = JointState()
    init_joints.header.stamp = rospy.Time.now()
    init_joints.name = JOINT_NAMES
    init_joints.position = HOME_JOINTS
    joint_pub.publish(init_joints)
    #########################
    ##### STUDENT WRITES ####
    #########################
    moveit_interface = moveit_commander.MoveGroupCommander('manipulator')
    joint_goal = moveit_interface.get_current_joint_values()#definicija tarce
    rospy.loginfo(joint_goal)

    joint_goal = HOME_JOINTS
    rospy.loginfo(joint_goal)

    #moveit_interface.go(joint_goal, wait=True)

    #for i in range(N_MOTIONS):
    #    rospy.loginfo("Preforming "+ str(i) +  " out of " + str(N_MOTIONS + 1))
    #    joint_goal = np.random.rand(6).tolist()

    #    moveit_interface.set_max_velocity_scaling_factor(np.random.random())
    #    moveit_interface.set_max_acceleration_scaling_factor(np.random.random())
    #    rospy.loginfo("Target: " + str(joint_goal))
    #    moveit_interface.go(joint_goal, wait=True)


    # Move in Cartesian space
    tf_buffer = tf2_ros.Buffer()
    tf_listener = tf2_ros.TransformListener(tf_buffer)
    tf_broadcaster = tf2_ros.StaticTransformBroadcaster()

    rospy.sleep(0.5)

    current_transform = tf_buffer.lookup_transform(
        'base_link',
        'tool0',
        rospy.Time(0)
    )

    print(current_transform.transform)
    raw_input("Press Enter")
    pose_goal = Pose(
        position=current_transform.transform.translation, orientation=current_transform.transform.rotation)
    #pose_goal.position.z += 0.1
    #moveit_interface.go(pose_goal, wait=True)

    target_transform = tf_buffer.lookup_transform(
    'base_link',
    'target_1',
    rospy.Time(0)
    )

    # premakni se 15cm nad target 1
    target_transform.transform.translation.z += 0.15
    target_transform.child_frame_id = 'target_offset'

    # Publish the frame and give the broadcaster some time
    tf_broadcaster.sendTransform(target_transform)
    rospy.sleep(0.5)

    # Now lookup the transform from the robot's base to the target offset
    offset_transform = tf_buffer.lookup_transform(
        'base_link',
        'target_offset',
        rospy.Time(0)
    )

    # Convert it to pose and send it to the robot
    pose_goal = Pose(
    position=offset_transform.transform.translation, orientation=offset_transform.transform.rotation)
    moveit_interface.go(pose_goal, wait=True)

    moveit_interface.shift_pose_target(2 ,-0.20)
    rospy.sleep(0.5)
    moveit_interface.execute(moveit_interface.plan(),wait=True)


    moveit_interface.shift_pose_target(2 ,+0.4)
    rospy.sleep(0.5)
    moveit_interface.execute(moveit_interface.plan(),wait=True)
    

    




    #########################