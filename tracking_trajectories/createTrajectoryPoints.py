#!/usr/bin/env python

import rospy
import os
from sensor_msgs.msg import JointState
import time
import csv

i = 0

def joint_states_callback(msg):
    # Callback function to process the received joint states
    rospy.loginfo("Received joint states:\n%s", msg)

    # Save the joint states to a CSV file
    file_path = os.path.expanduser('joint_states.csv')
    
    with open(file_path, 'a') as csv_file:
        writer = csv.writer(csv_file)
        
        # Write the data row
        row = [str(position) for position in msg.position]
        writer.writerow(row)



def track_and_save_joint_states():
    # time to track movements
    
    # Initialize ROS node
    rospy.init_node('joint_states_tracker')

    # Subscribe to the joint_states topic
    rospy.Subscriber('/joint_states', JointState, joint_states_callback)

    rospy.loginfo(f"Tracking joint states for {time_to_track} seconds...")

    # Set the end time
    end_time = rospy.Time.now() + rospy.Duration(time_to_track)

    # Spin while checking the end time
    while not rospy.is_shutdown() and rospy.Time.now() < end_time:
        rospy.sleep(0.05)

    rospy.loginfo("Tracking ended.")
    

        
if __name__ == '__main__':
    try:
        file_path = os.path.expanduser('joint_states.csv')
        with open(file_path, 'w') as file:
            file.write("")

        time_to_track = 90
        track_and_save_joint_states()

    except rospy.ROSInterruptException:
        rospy.logerr("Interrupted by user")


	

