#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from panthera_lights.msg import LightStatus

def callback(LightStatus):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', LightStatus)

    status=''
    status+='*'

    if LightStatus.Brake == 1:
        status+='1'
    else:
        status+='0'

    if LightStatus.HazardLight == 1:
        status+= '1'
    else:
        status+= '0'

    if (LightStatus.SignalRight == 1)and(LightStatus.SignalLeft != 1):
        status+= '1'
    else:
        status+= '0'

    if (LightStatus.SignalLeft == 1) and (LightStatus.SignalRight != 1):
        status+= '1'
    else:
        status+= '0'

    if LightStatus.Autonomous == 1:
        status+= '1'
    else:
        status+= '0'
    
    if LightStatus.TeleOp  == 1:
        status+= '1'
    else:
        status+= '0'
    
    if LightStatus.Beacon  == 1:
        status+= '1'
    else:
        status+= '0'

    if (LightStatus.Day == 1)and (LightStatus.Night != 1):
        status+= '1'
    else:
        status+= '0'

    if (LightStatus.Night == 1)and (LightStatus.Day != 1):
        status+= '1'
    else:
        status+= '0'
    
    status+='*'

    rospy.loginfo(status)




def listener():
    rospy.init_node('Arduino_control', anonymous=True)
    rospy.Subscriber('Panthera_LightStatus', LightStatus, callback)
    rospy.spin()




if __name__ == '__main__':
    listener()
