#!/usr/bin/env python3

import csv
from geometry_msgs.msg import PoseWithCovarianceStamped
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

# Custom Action Server Class
class MyActionServer(object):

    def __init__(self):
        # Initialize the action server
        self._as = actionlib.SimpleActionServer('move_turtlebot', MoveBaseAction, self.execute, False)
        self._as.start()

        self.current_goal = None
        self.goal_canceled = False

        # Create a ROS subscriber for amcl_pose
        rospy.Subscriber('amcl_pose', PoseWithCovarianceStamped, self.amcl_pose_callback)

    def execute(self, goal):
        # Check if action has been preempted
        if self._as.is_preempt_requested():
            rospy.loginfo('Action preempted')
            self._as.set_preempted()
            self.goal_canceled = True
            return

        # Get the goal position from the action goal
        x = goal.target_pose.pose.position.x
        y = goal.target_pose.pose.position.y
        z = goal.target_pose.pose.position.z
        w = goal.target_pose.pose.orientation.w
        rospy.loginfo('Moving to position: ({0}, {1}, {2}, {3})'.format(x, y, z, w))

        # Set orientation tolerance through ROS parameter
        orientation_tolerance = 0.1
        rospy.set_param('/move_base/DWAPlannerROS/yaw_goal_tolerance', orientation_tolerance)

        # Perform the action (e.g., send the goal to move_base)
        # Replace the following code with your desired implementation
        move_base_client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
        move_base_client.wait_for_server()

        move_base_goal = MoveBaseGoal()
        move_base_goal.target_pose = goal.target_pose
        move_base_goal.target_pose.header.frame_id = 'map'

        self.current_goal = goal
        move_base_client.send_goal(move_base_goal)
        
        # Wait for the current goal to complete or get canceled
        move_base_client.wait_for_result()

        # If the goal is canceled due to being near, don't wait for the result
        if not self.goal_canceled:
            rospy.loginfo('Action completed')
        else:
            rospy.loginfo('Action canceled')

        self.current_goal = None
        self.goal_canceled = False

    def amcl_pose_callback(self, msg):
        rospy.loginfo('Received AMCL pose message')
        if self.current_goal is not None:
            # Calculate the distance between the robot's current position and the goal position
            x_diff = msg.pose.pose.position.x - self.current_goal.target_pose.pose.position.x
            y_diff = msg.pose.pose.position.y - self.current_goal.target_pose.pose.position.y
            distance_to_goal = ((x_diff)**2 + (y_diff)**2)**0.5

            # Print out the values for debugging
            rospy.loginfo("Current goal position: x={}, y={}".format(self.current_goal.target_pose.pose.position.x,
                                                                    self.current_goal.target_pose.pose.position.y))
            rospy.loginfo("Robot's current position: x={}, y={}".format(msg.pose.pose.position.x,
                                                                        msg.pose.pose.position.y))
            rospy.loginfo("Distance to goal: {}".format(distance_to_goal))

            # If the robot is near the goal (you can adjust the threshold as needed)
            if distance_to_goal < 0.5:
                # Cancel the current goal
                rospy.loginfo('Near the goal. Cancelling the current goal.')
                self.goal_canceled = True
                self._as.set_preempted()
                self.current_goal = None
        else:
            # Perform a different action when no goal is being executed
            rospy.loginfo('No current goal. Performing a different action.')

# Main code
if __name__ == '__main__':
    # Initialize the ROS node and the action server
    rospy.init_node('my_action_server_node')
    server = MyActionServer()
    
    # Keep the node running
    rospy.spin()
