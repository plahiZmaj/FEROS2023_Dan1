#! /usr/bin/env python

import rospy
import pickle
import os
import tf2_ros

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

    trans = tf_buffer.lookup_transform('world','frame_1',rospy.Time(0))
    trans2 = tf_buffer.lookup_transform('frame_1','frame_2',rospy.Time(0))

    tx = trans.transform.translation.x
    ty = trans.transform.translation.y
    tz = trans.transform.translation.z
    rx = trans.transform.rotation.x
    ry = trans.transform.rotation.y
    rz = trans.transform.rotation.z

    tx2 = trans2.transform.translation.x
    ty2 = trans2.transform.translation.y
    tz2 = trans2.transform.translation.z
    rx2 = trans2.transform.rotation.x
    ry2 = trans2.transform.rotation.y
    rz2 = trans2.transform.rotation.z

    saved_data["Frame1"] = trans
    saved_data["Frame2"] = trans2

    rospy.loginfo("tx: %d, ty: %d, tz: %d, rx: %d, ry: %d, rz: %d", tx, ty, tz, rx, ry, rz)
    rospy.loginfo("2tx: %d, ty: %d, tz: %d, rx: %d, ry: %d, rz: %d", tx2, ty2, tz2, rx2, ry2, rz2)

    
    pickle.dump(saved_data, outfile)
    outfile.close()
        




    
    


    # Hint - Use the tf_buffer.lookup_transform() method to retrieve the transform.
    # Example:
    # transformation = tf_buffer.lookup_transform(from_frame, to_frame, rospy.Time(0))
    # Note - from_frame and to_frame need to be defined!


    #########################

    


    