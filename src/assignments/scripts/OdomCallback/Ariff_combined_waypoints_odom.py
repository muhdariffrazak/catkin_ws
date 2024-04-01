#!/usr/bin/env python

import csv
import rospy
import actionlib
from nav_msgs.msg import Odometry
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

read_loc = {}


# Function to read waypoint locations from a CSV file
def ReadLocation():
    with open('/home/ariff/catkin_ws/src/assignments/scripts/waypoints.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            waypoint = row["waypoint"]
            x, y, z, w = row["x"], row["y"], row["z"], row["w"]
            read_loc[waypoint] = [x, y, z, w]
            rospy.loginfo("Read waypoint: {0}, X: {1}, Y: {2}, Z: {3}, W: {4}".format(waypoint, x, y, z, w))
    return read_loc

# GoalCancelerNode class to manage goal cancellation and navigation
class GoalCancelerNode(object):
    def __init__(self):
        rospy.init_node('goal_canceler_node')
        self.max_linear_velocity = 0.2  # Adjust this value as needed for linear speed (e.g., 0.3 m/s)
        self.max_angular_velocity = 0.15  # Adjust this value as needed for angular speed (e.g., 1.0 rad/s)
        self.oscillation_distance = 0.1  # Default oscillation distance is 0.2

        # Subscribe to robot's odometry
        rospy.Subscriber('odom', Odometry, self.odom_callback)

        # Create an action client to send goals to move_base
        self.move_base_client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
        self.move_base_client.wait_for_server()

        # Initialize variables to track the current goal and waypoints
        self.current_goal = None
        self.waypoints = []  # Add your list of waypoints here
        self.waypoints_completed = 0

    """
    Odom_callback function to cancel the current goal and send the next goal
    when the robot is near the current goal
    """
    def odom_callback(self, msg):
        if self.current_goal is not None:
            # Calculate the distance between the robot's current position and the goal position
            x_diff = msg.pose.pose.position.x - self.current_goal.target_pose.pose.position.x
            y_diff = msg.pose.pose.position.y - self.current_goal.target_pose.pose.position.y
            distance_to_goal = ((x_diff)**2 + (y_diff)**2)**0.5

            # If the robot is near the goal (you can adjust the threshold as needed)
            if distance_to_goal < 0.4:
                # Cancel the current goal
                rospy.loginfo('Near the goal. Cancelling the current goal.')
                self.move_base_client.cancel_goal()

                # Request the next waypoint as the new goal
                self.send_next_goal()

    """
    send_next_goal function to send the next goal to move_base
    after the current goal has been canceled
    """
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
            
            # Set orientation tolerance
            orientation_tolerance = 0.1
            rospy.set_param('/move_base/DWAPlannerROS/yaw_goal_tolerance', orientation_tolerance)

            # Set the max linear and angular velocity of the robot
            rospy.set_param('/move_base/TrajectoryPlannerROS/max_vel_x', self.max_linear_velocity)
            rospy.set_param('/move_base/TrajectoryPlannerROS/max_vel_theta', self.max_angular_velocity)

            # Set the oscillation distance
            rospy.set_param('/move_base/DWAPlannerROS/oscillation_distance', self.oscillation_distance)

            self.current_goal = next_goal
            self.move_base_client.send_goal(next_goal)

            # Update waypoints_completed counter and log the current count
            self.waypoints_completed += 1
            rospy.loginfo('Waypoints completed: {0}/{1}'.format(self.waypoints_completed, len(self.waypoints)))


    """
    run function to send the next goal and keep the node running
    """
    def run(self):
        # Log the total number of waypoints
        total_waypoints = len(self.waypoints)
        rospy.loginfo('Total number of waypoints: {0}'.format(total_waypoints))
        rospy.loginfo('Waypoints completed: {0}/{1}'.format(self.waypoints_completed, len(self.waypoints)))

        # Send the first goal to start the navigation
        self.send_next_goal()

        # Keep the node running
        rospy.spin()


"""
Main function
"""
if __name__ == '__main__':
    try:
        goal_canceler_node = GoalCancelerNode()
        goal_positions = ReadLocation()

        # Set the oscillation distance before running the node
        goal_canceler_node.oscillation_distance = 0.1  # Set the desired oscillation distance here

        # Create MoveBaseGoal objects for each waypoint and add them to the waypoints list
        for position in goal_positions:
            goal = MoveBaseGoal()
            goal.target_pose.pose.position.x = float(read_loc[position][0])
            goal.target_pose.pose.position.y = float(read_loc[position][1])
            goal.target_pose.pose.position.z = float(read_loc[position][2])
            goal.target_pose.pose.orientation.w = float(read_loc[position][3])
            goal_canceler_node.waypoints.append(goal)

        # Execute the goals sequentially
        goal_canceler_node.run()
    except rospy.ROSInterruptException:
        pass
