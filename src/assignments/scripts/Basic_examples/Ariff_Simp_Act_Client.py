#!/usr/bin/env python3

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

Pos1=(6.3, -3.0, -0.05, 1.0)
Pos2=(4.8, 2.6, -0.05, 1.0)
Pos3=(0.9, 3.0, -0.05, 1.0)


def turtlebot_action_client():
    rospy.init_node('turtlebot_action_client')
    client = actionlib.SimpleActionClient('move_turtlebot', MoveBaseAction)
    rospy.loginfo("Waiting for action server...")
    client.wait_for_server()
    rospy.loginfo("Connected to action server")

    goal_positions = [Pos1, Pos2, Pos3]

    while True:
        for goal_position in goal_positions:
            goal = MoveBaseGoal()
            goal.target_pose.header.frame_id = "map"
            goal.target_pose.pose.position.x = goal_position[0]
            goal.target_pose.pose.position.y = goal_position[1]
            goal.target_pose.pose.orientation.z = goal_position[2]
            goal.target_pose.pose.orientation.w = goal_position[3]

            rospy.loginfo(f"Sending goal position: {goal_position}")
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
