#! /usr/bin/env python

import rospy
import pickle
import os
import tf2_ros
from sensor_msgs.msg import JointState

if __name__ == '__main__':

    rospy.init_node('tf_saver')
    rospy.loginfo("TF saver started!")

    tf_buffer = tf2_ros.Buffer()
    tf_listener = tf2_ros.TransformListener(tf_buffer)

    rospy.sleep(1)
    stored_data = {}


    ##### FILL IN THE APPROPRIATE FILENAME. HINT: USE `raw_input()`
    file_name = raw_input("Vnesi ime datoteke: ")
    outfile = open(file_name,'wb')
    saved_data = {}

    from_frame = 'base_link'
    to_frame = 'tool0'
    
    while not rospy.is_shutdown():
        entry_name = raw_input("Vnesi key: ")
        if entry_name.lower() == "exit":
            break
        frame = tf_buffer.lookup_transform(from_frame, to_frame, rospy.Time(0))
        frame.child_frame_id = entry_name
        joints = rospy.wait_for_message('/joint_states', JointState, rospy.Duration(1))
        saved_data[entry_name] = [joints, frame]
    
    pickle.dump(saved_data, outfile)
    outfile.close()
        




    
    


    # Hint - Use the tf_buffer.lookup_transform() method to retrieve the transform.
    # Example:
    # transformation = tf_buffer.lookup_transform(from_frame, to_frame, rospy.Time(0))
    # Note - from_frame and to_frame need to be defined!


    #########################

    


    