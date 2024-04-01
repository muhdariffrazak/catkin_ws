#!/usr/bin/env python3
# license removed for brevity
import rospy
from std_msgs.msg import String
from panthera_lights.msg import LightStatus

if __name__ == '__main__':
    rospy.init_node('EStopNode', anonymous=True)
    pub = rospy.Publisher('/sutd001/err_msg', String, queue_size=10)
    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():
        msg = String()
        msg.data = ''
        pub.publish(msg)
        rate.sleep()
