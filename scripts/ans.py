#!/usr/bin/env python3
#-*- conding: utf-8 -*-
import rospy
import time
from std_msgs.msg import String

def cb(message):
    if message.data == '欲しいものは?':
        print ('単位')
    if message.data == 'なんでも願いが叶うなら?':
        print('単位がほしい')

if __name__ == '__main__':
    print('質問の答えです')
    rospy.init_node('ans')
    sub = rospy.Subscriber('question',String,cb)
    rospy.spin()
