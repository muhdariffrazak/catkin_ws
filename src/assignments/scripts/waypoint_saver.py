#!/usr/bin/env python3

import csv
from geometry_msgs.msg import PoseWithCovarianceStamped
import rospy

def count_rows_in_csv(file_path):
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        num_rows = sum(1 for row in reader)
    return num_rows

def amcl_pose_callback(msg):
    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y
    z = msg.pose.pose.position.z
    w = msg.pose.pose.orientation.w

    # Replace 'YOUR/CSV/FILE/PATH/waypoints.csv' with the actual file path
    file_path = '/home/ariff/catkin_ws/src/assignments/scripts/waypoints.csv'

    # Count the number of rows in the CSV file
    num_existing_rows = count_rows_in_csv(file_path)

    # Append the (x, y, z, w) data to the CSV file
    with open(file_path, 'a') as csvfile:
        writer = csv.writer(csvfile)
        # Write a header row if the file is empty
        writer.writerow([num_existing_rows, float(round(x, 2)), float(round(y, 2)), float(round(z, 2)), float(round(w, 2))])

    # Print the (x, y, z, w) data to the terminal
    rospy.loginfo("x: {0}, y: {1}, z: {2}, w: {3}".format(x, y, z, w))
    rospy.loginfo("Waypoint saved!")

if __name__ == "__main__":
    # Initialize the ROS node with a unique name (e.g., "waypoint_saver")
    rospy.init_node("waypoint_saver", anonymous=True)

    # Create the ROS subscriber to listen to the "amcl_pose" topic
    rospy.Subscriber("amcl_pose", PoseWithCovarianceStamped, amcl_pose_callback)

    # Wait for a short time to allow the callback function to execute
    rospy.sleep(1)

    # After executing the callback once, the node will exit

