#!/usr/bin/env python3

import csv
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

read_loc = {}


def ReadLocation():
    with open('/home/ariff/catkin_ws/src/assignments/scripts/waypoints_prac.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            read_loc[row["waypoint"]] = [row["x"], row["y"], row["z"], row["w"]]
    return read_loc


class GoalLoopNode(object):
    def __init__(self):
        rospy.init_node('goal_loop_node')

        # Create an action client to send goals to move_base
        self.move_base_client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
        self.move_base_client.wait_for_server()

        # Initialize the list of waypoints
        self.waypoints = []

    def send_next_goal(self):
        if len(self.waypoints) > 0:
            next_goal = self.waypoints.pop(0)
            rospy.loginfo('Sending next goal: ({0}, {1}, {2}, {3})'.format(
                next_goal.target_pose.pose.position.x,
                next_goal.target_pose.pose.position.y,
                next_goal.target_pose.pose.position.z,
                next_goal.target_pose.pose.orientation.w
            ))
            next_goal.target_pose.header.frame_id = 'map'
            
            # Set orientation tolerance (adjust the value as needed)
            orientation_tolerance = 0.1
            rospy.set_param('/move_base/DWAPlannerROS/yaw_goal_tolerance', orientation_tolerance)
            
            self.move_base_client.send_goal(next_goal)

    def run(self):
        # Loop through waypoints continuously
        while not rospy.is_shutdown():
            goal_positions = ReadLocation()

            # Create MoveBaseGoal objects for each waypoint and add them to the waypoints list
            for position in goal_positions:
                goal = MoveBaseGoal()
                goal.target_pose.pose.position.x = float(read_loc[position][0])
                goal.target_pose.pose.position.y = float(read_loc[position][1])
                goal.target_pose.pose.position.z = float(read_loc[position][2])
                goal.target_pose.pose.orientation.w = float(read_loc[position][3])
                self.waypoints.append(goal)

            # Send the goals sequentially
            while self.waypoints:
                self.send_next_goal()
                self.move_base_client.wait_for_result()
                rospy.loginfo('Goal reached. Waiting for next goal...')
                rospy.sleep(1.0)  # Wait for 1 second before sending the next goal


if __name__ == '__main__':
    try:
        goal_loop_node = GoalLoopNode()
        goal_loop_node.run()
    except rospy.ROSInterruptException:
        pass
