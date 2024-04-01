#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from panthera_lights.msg import LightStatus
from serial import Serial
import time

status='' #variable to store incoming status
prev_status = ''#variable to store the previous status
changed=True #flag to indicate if the status has changed

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
                rospy.Subscriber('Panthera_LightStatus', LightStatus, LS_Core.callback)
                self.Run()


    def callback(LightStatus):
        global prev_status, status, changed #import global variables



        #-------------------Parse incoming data:----------------------
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
            
        if (LightStatus.Night == 1)and (LightStatus.Day != 1):
            status+= '1'
        else:
            status+= '0'
            

        if (LightStatus.Day == 1)and (LightStatus.Night != 1):
            status+= '1'
        else:
            status+= '0'

        
        
        status+='*'

        rospy.loginfo(status)#print out parsed data
        if status != prev_status:#Change data if flag is diff
            changed=True



    def Run(self):
        global changed, prev_status, status

        try:
            while not rospy.is_shutdown():
                if changed == True:
                    data = bytes(status,'ascii')
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

