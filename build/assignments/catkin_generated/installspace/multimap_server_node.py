#!/usr/bin/env python3

import rospy
import subprocess
import signal
from assignments.srv import MapFilePath

map_server = None

def set_map(req):
    global map_server
    if map_server is not None:
        map_server.send_signal(signal.SIGINT)
    map_server = subprocess.Popen(['rosrun', 'map_server', 'map_server', req.map_file_path])
    return True

if __name__ == '__main__':
    rospy.init_node('multimap_server_node')
    rospy.Service('/multimap_server/set_map', MapFilePath, set_map)
    rospy.loginfo('Multimap server node started')
    rospy.spin()

"""
#alternative code for multimap_server_node.py
#!/usr/bin/env python3


import rospy
import subprocess
import signal
from multimap_server.srv import MapFilePath

map_server = None

def set_map(req):
    global map_server
    if map_server is not None:
        # Terminate the existing map_server process gracefully
        map_server.send_signal(signal.SIGINT)
        map_server.wait()  # Wait for the process to complete before proceeding

    # Validate the map file path
    if not req.map_file_path:
        rospy.logerr('Invalid map file path provided. Aborting map switch.')
        return False

    try:
        # Start the new map_server process with the requested map file
        map_server = subprocess.Popen(['rosrun', 'map_server', 'map_server', req.map_file_path])
        rospy.loginfo('Switched to new map: {}'.format(req.map_file_path))
        return True
    except subprocess.CalledProcessError as e:
        rospy.logerr('Failed to start map_server process: {}'.format(e))
        return False

if __name__ == '__main__':
    rospy.init_node('multimap_server_node')
    rospy.Service('/multimap_server/set_map', MapFilePath, set_map)
    rospy.loginfo('Multimap server node started')
    rospy.spin()

# Ensure to stop the map_server process gracefully on node shutdown
if map_server is not None:
    map_server.send_signal(signal.SIGINT)
    map_server.wait()
"""