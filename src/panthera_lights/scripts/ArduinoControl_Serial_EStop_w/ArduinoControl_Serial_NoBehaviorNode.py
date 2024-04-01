#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from std_msgs.msg import Bool
from geometry_msgs.msg import Twist
from visualization_msgs.msg import Marker
from nav_msgs.msg import Odometry
from serial import Serial
import time

status='' #variable to store incoming status
prev_status = ''#variable to store the previous status
changed=True #flag to indicate if the status has changed
Estop = False
EstopData='*110000101*'
Brake= False
HazardLight = False
SignalRight = False
SignalLeft = False
Autonomous = False
TeleOp = False
Beacon = True
Night = False
Day = True
GlobalPoseY = 0

class LS_Core:
    
    def __init__(self, _serial_port, _baudrate):
            #----------------Serial functions------------------
            self.counter = 0
            self.ser = Serial()
            self.ser.baudrate = _baudrate
            self.ser.baudrate = 115200
            self.ser.port = _serial_port
            self.ser.timeout = 0.5

            while not self.ser.is_open:
                try:
                    self.ser.open()
                except:
                    rospy.logerr("Unable to open %s, retrying", _serial_port)
                    print("Unable to open %s, retrying", _serial_port)
                    time.sleep(1.0)
                    
            if self.ser.is_open:
                self.ser.reset_input_buffer
                self.ser.reset_output_buffer
                self.ser.flush()
                rospy.loginfo("Serial port %s opened", _serial_port)
                rospy.Subscriber('/sutd001/err_msg', String, LS_Core.callback)
                rospy.Subscriber('cmd_vel',Twist,LS_Core.callback1)
                rospy.Subscriber('/purepur/enabled',Bool,LS_Core.callback2)
                rospy.Subscriber('/odometry/filtered/global',Odometry,LS_Core.callback3)
                rospy.Subscriber('/pure_pursuit/path_marker',Marker,LS_Core.callback4)
                rospy.Subscriber('autonomy_mode',Bool,LS_Core.callback5)
                self.Run()


    def callback(String):
        global Estop , changed, EstopData
        if String.data == 'W01':
            Estop = True 
            changed = True
        else:
            Estop = False
            changed = True

    def callback1(Twist):
        global Brake 
        if Twist.linear.x <= 0.05 :
            Brake=True
        else:
            Brake=False
    

    def callback2(Bool):
        global HazardLight
        if Bool.data == True:
            HazardLight = True
        else:
            HazardLight = False

    def callback3(Odometry):
        global GlobalPoseY
        GlobalPoseY = Odometry.pose.pose.position.y


    def callback4(Marker): #check this
        global SignalLeft ,SignalRight
        if (Marker.pose.position.y - GlobalPoseY)>1:
            SignalRight=True
        elif (Marker.pose.position.y - GlobalPoseY)<-1:
            SignalLeft=True
        else:
            SignalLeft=False
            SignalRight=False
    

    def callback5(Bool):
        global Autonomous, TeleOp
        if Bool.data == True:
            Autonomous = True
            TeleOp = False 
        else:
            Autonomous = False
            TeleOp = True

    
    def ParseData():
        global prev_status, status, changed #import global variables



        #-------------------Parse incoming data:----------------------
        status+='*'

        if Brake == True:
            status+='1'
        else:
            status+='0'

        if HazardLight == True:
            status+= '1'
        else:
            status+= '0'

        if (SignalRight == True)and(SignalLeft == False):
            status+= '1'
        else:
            status+= '0'

        if (SignalLeft == True)and(SignalRight == False):
            status+= '1'
        else:
            status+= '0'

        if Autonomous == True:
            status+= '1'
        else:
            status+= '0'
        
        if TeleOp  == True:
            status+= '1'
        else:
            status+= '0'
        
        if Beacon == True:
            status+= '1'
        else:
            status+= '0'
            
        if Night == True:
            status+= '1'
        else:
            status+= '0'
            

        if Day == True:
            status+= '1'
        else:
            status+= '0'

        
        
        status+='*'

        rospy.loginfo(status)#print out parsed data
        if status != prev_status:#Change data if flag is diff
            changed=True
        time.sleep(0.4)
    

    def Run(self):
        global changed, prev_status, status, Estop, EstopData

        try:
            while not rospy.is_shutdown():
                LS_Core.ParseData()
                if changed == True and Estop == False:
                    data = bytes(status,'ascii')
                    self.ser.write(data)
                    time.sleep(0.4)
                    prev_status=status
                    status=''
                    changed=False

                elif Estop == True and changed == True:
                    data = bytes(EstopData,'ascii')
                    self.ser.write(data)
                    time.sleep(0.4)
                    prev_status=status
                    status=''
                    changed=False
                    
                else:
                    receive=self.ser.readline().decode('ascii').strip('\r\n')
                    if len(receive) > 10:
                        print(receive)

            
        except rospy.ROSInterruptException:
            pass




if __name__ == '__main__':
    rospy.init_node('Arduino_control', anonymous=True)
    LS_Core('/dev/ttyACM0', 115200)
    rospy.spin()

