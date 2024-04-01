#!/usr/bin/env python3

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

# Custom Action Server Class
class MyActionServer(object):

    def __init__(self):
        # Initialize the action server
        self._as = actionlib.SimpleActionServer('move_turtlebot', MoveBaseAction, self.execute, False)
        self._as.start()

    def execute(self, goal):
        # Check if action has been preempted
        if self._as.is_preempt_requested():
            rospy.loginfo('Action preempted')
            self._as.set_preempted()
            return

        # Get the goal position from the action goal
        goal_position = goal
        result = goal
        rospy.loginfo('Moving to position: {0}'.format(goal_position))

        # Perform the action (e.g., send the goal to move_base)
        # Replace the following code with your desired implementation
        move_base_client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
        move_base_client.wait_for_server()

        move_base_goal = MoveBaseGoal()
        move_base_goal.target_pose.pose.position.x = goal.target_pose.pose.position.x
        move_base_goal.target_pose.pose.position.y = goal.target_pose.pose.position.y
        move_base_goal.target_pose.pose.orientation.z = goal.target_pose.pose.orientation.z
        move_base_goal.target_pose.pose.orientation.w = goal.target_pose.pose.orientation.w
        move_base_goal.target_pose.header.frame_id = 'map'

        move_base_client.send_goal(move_base_goal)
        move_base_client.wait_for_result()

        # Check if the action has been preempted during execution
        if self._as.is_preempt_requested():
            rospy.loginfo('Action preempted')
            move_base_client.cancel_goal()
            self._as.set_preempted()
            return

        # Provide feedback and result
        #self._as.publish_feedback(self._feedback)

        rospy.loginfo('Action completed')
        self._as.set_succeeded(result)

# Main code
if __name__ == '__main__':
    rospy.init_node('my_action_server_node')
    server = MyActionServer()
    rospy.spin()
