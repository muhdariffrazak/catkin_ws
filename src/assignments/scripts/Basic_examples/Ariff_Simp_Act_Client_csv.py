#!/usr/bin/env python3

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import csv

read_loc = {}

def ReadLocation():
    with open('/home/ariff/catkin_ws/src/assignments/scripts/waypoints.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        line_count = 0

        for row in reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            print(f'\t{row["waypoint"]} is {row["x"]} , {row["y"]},{row["z"]},{row["w"]}')
            line_count += 1
            read_loc[row["waypoint"]] = [row["x"], row["y"], row["z"], row["w"]]
        print(f'Processed {line_count} lines.')
        
    return read_loc

def turtlebot_action_client():
    rospy.init_node('turtlebot_action_client')
    client = actionlib.SimpleActionClient('move_turtlebot', MoveBaseAction)
    rospy.loginfo("Waiting for action server...")
    client.wait_for_server()
    rospy.loginfo("Connected to action server")

    goal_positions = ReadLocation()

    while True:

        for position in goal_positions:
            print(position)
            print(read_loc[position])
            goal = MoveBaseGoal()
            goal.target_pose.header.frame_id = "map"
            goal.target_pose.pose.position.x = float(read_loc[position][0])
            goal.target_pose.pose.position.y = float(read_loc[position][1])
            goal.target_pose.pose.orientation.z = float(read_loc[position][2])
            goal.target_pose.pose.orientation.w = float(read_loc[position][3])

            rospy.loginfo(f"Sending goal position: {read_loc[position][0]}, {read_loc[position][1]}, {read_loc[position][2]}, {read_loc[position][3]}")
            client.send_goal(goal)
            client.wait_for_result()
            
            if client.get_state() == actionlib.GoalStatus.SUCCEEDED:
                rospy.loginfo("Goal reached successfully")
            else:
                rospy.loginfo("Failed to reach the goal")

if __name__ == '__main__':
    try:
        turtlebot_action_client()
    except rospy.ROSInterruptException:
        pass
