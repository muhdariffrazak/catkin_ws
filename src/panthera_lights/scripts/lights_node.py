#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from std_msgs.msg import Bool
from geometry_msgs.msg import Twist
from visualization_msgs.msg import Marker
from nav_msgs.msg import Odometry
from serial import Serial
import time


from serial import Serial
import time

class LightsState: #Flags to actuate the lights
        
    def __init__(self):

        self.Estop = False
        self.Brake= False
        self.HazardLight = False
        self.SignalRight = False
        self.SignalLeft = False
        self.Autonomous = False
        self.TeleOp = False
        self.Beacon = True
        self.Night = False
        self.Day = True
    
    def clear(self):
        self.Estop = False
        self.Brake= False
        self.HazardLight = False
        self.SignalRight = False
        self.SignalLeft = False
        self.Autonomous = False
        self.TeleOp = False
        self.Beacon = True
        self.Night = False
        self.Day = True
        


class SerialInterface: #Class for serial communication and data parsing
    
    def __init__(self, _serial_port, _baudrate):


        self.GlobalPoseY = 0

        self.status = ''
        self.prev_status = ''#variable to store the previous status
        self.changed=True #flag to indicate if the status has changed
        self.prev_status, self.status, self.changed #import global variables
        #----------------Serial functions------------------
        self.counter = 0
        self.ser = Serial()
        self.ser.baudrate = _baudrate
        self.ser.baudrate = 115200
        self.ser.port = _serial_port
        self.ser.timeout = 0.5

        



        attempt = 1

        while not self.ser.is_open:
            try:
                self.ser.open()
            except:
                print("Unable to open %s, retrying for", str(attempt), "/5", _serial_port, )
                time.sleep(1.0)
                attempt += 1
                if attempt > 5:
                    print("Unable to open %s, exiting", _serial_port)
                    exit(1)
        
        if self.ser.is_open:
            self.ser.reset_input_buffer
            self.ser.reset_output_buffer
            self.ser.flush()



    
    def ParseData(self, state): #Function to parse the data to be sent to the serial device

        Brake_ = '0'
        HazardLight_ = '0'
        RigtSignal_= '0'
        LeftSignal_ = '0'
        Autonomous_ = '0'
        TeleOp_ = '0'
        Beacon_ = '0'
        Night_ = '0'
        Day_ = '0'

        if state.Brake:
            Brake_ = '1'
        if state.HazardLight:
            HazardLight_ = '1'
        if state.SignalRight:
            RigtSignal_= '1'
        if state.SignalLeft:
            LeftSignal_ = '1'
        if state.Autonomous:
            Autonomous_ = '1'
        if state.TeleOp:
            TeleOp_ = '1'
        if state.Beacon:
            Beacon_ = '1'
        if state.Night:
            Night_ = '1'
        if state.Day:
            Day_ = '1'
        
        status = "*" + Brake_ + HazardLight_ + RigtSignal_ + LeftSignal_ + Autonomous_ + TeleOp_ + Beacon_ + Night_ + Day_ + "*"

        time.sleep(0.4)
        rospy.loginfo("Generating data packet %s", status)
        return status
    
    def SendData(self, status):
        #-------------------Send data:----------------------
        data = bytes(status,'ascii')
        self.ser.write(data)
        time.sleep(0.4)
        return


    def ReceiveData(self):
        return self.ser.readline().decode('ascii').strip('\r\n')


class RosInterface: #Class for ROS interface
    def __init__(self):
        self.counter = 0

        #rosparam gets the parameters from the previous state to generate the string to be sent to the serial device
        self.error_msg_topic        = rospy.get_param('error_msg_topic', '/sutd001/err_msg')
        self.cmd_vel_topic          = rospy.get_param('cmd_vel_topic', 'cmd_vel')
        self.purpur_marker_topic    = rospy.get_param('purpur_marker_topic', '/pure_pursuit/path_marker')
        self.odom_topic             = rospy.get_param('odom_topic', '/odometry/filtered/global')
        self.autonomy_mode_topic    = rospy.get_param('autonomy_mode_topic', 'autonomy_mode')
        self.serialtimer            = rospy.get_param('serialtimer', 1.0)

        self.serial_port            = rospy.get_param('serial_port', '/dev/ttyACM0' )
        self.baudrate               = rospy.get_param('baudrate', 115200)

        self.serialdevice           = SerialInterface(self.serial_port, self.baudrate)

        self.EstopData              ='*110000101*'

        self.GlobalPoseY            = 0.0

        self.changed                = False

        self.is_first_time = True

        self.robot_state = LightsState()
        self.robot_state.clear()

        self.prev_data = ''

        rospy.Subscriber(self.error_msg_topic, String, self.errorCB)
        rospy.Subscriber(self.cmd_vel_topic,Twist,self.cmdVelCB)
        rospy.Subscriber(self.odom_topic,Odometry,self.odomCb)
        rospy.Subscriber(self.purpur_marker_topic,Marker,self.markerCB)
        rospy.Subscriber(self.autonomy_mode_topic,Bool,self.autonomyModeCB)
        rospy.Timer(rospy.Duration(self.serialtimer), self.timerCB) #Timer to send data to serial device at a fixed rate

    def timerCB(self, event): #Function to send data to serial device at a fixed rate

        try:

            if not self.robot_state.Estop:
                
                data = self.serialdevice.ParseData(self.robot_state)
                if self.prev_data != data:
                    self.prev_data = data
                    self.serialdevice.SendData(data)
                    rospy.loginfo("Sending data to serial device @ %s", self.serial_port)
                    
            else:
                # data = bytes(self.EstopData,'ascii')
                self.serialdevice.SendData(self.EstopData)
                self.prev_data = self.EstopData
                rospy.loginfo("Sending Estop data to serial device @ %s", self.serial_port)

            receive =   self.serialdevice.ReceiveData()
            rospy.loginfo("Received data from serial device @ %s, %s", self.serial_port, receive)

            
        except rospy.ROSInterruptException:
            pass


#-------------------Callbacks functions for subcribers----------------------
    def errorCB(self, msg):

        if msg.data == '000':
            self.robot_state.Estop = False
            self.changed = True
            rospy.loginfo("Estop is off")
        else:
            self.robot_state.Estop = True 
            self.changed = True

    def cmdVelCB(self, msg):
   
        if msg.linear.x <= 0.05 :
            self.robot_state.Brake=True
        else:
            self.robot_state.Brake=False


    def odomCb(self, msg):

        self.GlobalPoseY = msg.pose.pose.position.y

    
    def markerCB(self,msg): #check this

        if (msg.pose.position.y - self.GlobalPoseY)>0.5:
            self.robot_state.SignalRight=True
        elif (msg.pose.position.y - self.GlobalPoseY)<-0.5:
            self.robot_state.SignalLeft=True
        else:
            self.SignalLeft=False
            self.SignalRight=False
    

    def autonomyModeCB(self, msg):

        if msg.data == True:
            self.robot_state.Autonomous = False
            self.robot_state.TeleOp = True
            rospy.loginfo("Autonomous mode is on")
        else:
            self.robot_state.Autonomous = True
            self.robot_state.TeleOp = False
            rospy.loginfo("Teleop mode is on")


if __name__ == '__main__':
    rospy.init_node('panthera_lights')
    RosInterface()
    rospy.spin()