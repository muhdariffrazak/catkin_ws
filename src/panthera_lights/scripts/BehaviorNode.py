#!/usr/bin/env python3
# license removed for brevity
import rospy
from std_msgs.msg import String
from panthera_lights.msg import LightStatus

if __name__ == '__main__':
    rospy.init_node('BehaviorNode', anonymous=True)
    pub = rospy.Publisher('Panthera_LightStatus', LightStatus, queue_size=10)
    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():
        lightStatus = LightStatus()
        lightStatus.Brake = 0
        lightStatus.HazardLight = 0
        lightStatus.SignalRight = 0
        lightStatus.SignalLeft = 0
        lightStatus.Autonomous = 0
        lightStatus.TeleOp  = 0
        lightStatus.Beacon  = 0
        lightStatus.Day = 0
        lightStatus.Night = 0
        pub.publish(lightStatus)
        rate.sleep()
