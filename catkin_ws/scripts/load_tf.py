#! /usr/bin/env python

import rospy
import pickle
import tf2_ros

if __name__ == '__main__':

    # Init the node
    rospy.init_node('tf_loader')
    tf_broad = tf2_ros.StaticTransformBroadcaster()

    ##### FILL IN THE APPROPRIATE FILENAME. HINT: USE `raw_input()`
    file_name = "test"

    infile = open(file_name,'rb')
    stored_poses = pickle.load(infile)
    list1 = []
    
    for key,value in stored_poses.items():
        list1.append(value)

    print(list1)
    infile.close()

    #########################
    ##### STUDENT WRITES ####
    #########################
    
    tf_broad.sendTransform(list1)
    #########################
    rospy.spin()