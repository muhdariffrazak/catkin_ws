#!/usr/bin/env python3

import rospy
import subprocess
import signal
from assignments.srv import MapFilePath
from geometry_msgs.msg import PoseWithCovarianceStamped
import math

map_server = None

def set_map(req):
    global map_server
    if map_server is not None:
        map_server.send_signal(signal.SIGINT)
    map_server = subprocess.Popen(['rosrun', 'map_server', 'map_server', req.map_file_path])
    return True

def amcl_callback(msg):
    # Get the robot's current position from the AMCL pose message
    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y

    # Check if the robot is near a certain position where you want to switch maps
    if should_switch_map(x, y):
        perform_map_switch('/home/ariff/catkin_ws/src/assignments/maps/house_part2.yaml')

def should_switch_map(x, y):
    # Define the coordinates where you want to switch the map
    switch_x = 4.0
    switch_y = 3.5

    # Calculate the distance between the robot's position and the switch point
    distance_to_switch = math.sqrt((x - switch_x)**2 + (y - switch_y)**2)

    # Return True if the robot is within a certain threshold of the switch point
    return distance_to_switch < 0.5

def perform_map_switch(new_map_path):
    try:
        switch_map_service = rospy.ServiceProxy('/multimap_server/set_map', MapFilePath)
        response = switch_map_service(new_map_path)
        if response:
            rospy.loginfo('Map switch successful')
        else:
            rospy.logwarn('Map switch failed')
    except rospy.ServiceException as e:
        rospy.logerr('Failed to call map switch service: %s' % e)

if __name__ == '__main__':
    rospy.init_node('multimap_server_node')
    rospy.Service('/multimap_server/set_map', MapFilePath, set_map)
    rospy.Subscriber('amcl_pose', PoseWithCovarianceStamped, amcl_callback)  # Subscribe to the AMCL pose topic
    rospy.loginfo('Multimap server node started')
    rospy.spin()
