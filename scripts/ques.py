#!/usr/bin/env python3
#-*- coding:utf-8 -*-
import rospy
from std_msgs.msg import String

if __name__ == '__main__':
    print('質問を書こう')
    rospy.init_node('ques')
    pub = rospy.Publisher('question',String,queue_size = 50)
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        n = input()

        pub.publish(n)
        rate.sleep()
    
