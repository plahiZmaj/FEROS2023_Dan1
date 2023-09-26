#!/usr/bin/env python

import rospy

if __name__ == '__main__':
  rospy.init_node('my_first_python_node', anonymous=True)                 # inicializacija noda
  rospy.loginfo('This node has been started.')            # pogledamo node info
  rospy.sleep(100)
  print('Exit now')