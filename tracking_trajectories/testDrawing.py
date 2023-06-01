#!/usr/bin/env python

import sys
import rospy
import actionlib
from control_msgs.msg import FollowJointTrajectoryAction, FollowJointTrajectoryGoal
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from rospy import Duration
import csv

def send_trajectory():
    rospy.init_node('trajectory_controller_node')
    
    # Create an action client for the FollowJointTrajectory action server
    client = actionlib.SimpleActionClient('/arm_controller/follow_joint_trajectory', FollowJointTrajectoryAction)
    rospy.loginfo("Waiting for action server...")
    client.wait_for_server()

    
    trajectory = JointTrajectory()
    trajectory.joint_names = ['J1', 'J2', 'J3', 'J4', 'J5', 'J6']

    """
    # Define points in the trajectory
    point1 = JointTrajectoryPoint()
    point1.positions = [3.3171379566192627, 0.2804395258426666, 0.2298249751329422, -1.8500316143035889, 0.8060803413391113, 1.172529697418213]
    point1.time_from_start = Duration(1.0)

    point2 = JointTrajectoryPoint()
    point2.positions = [3.0, 0.2804395258426666, 0.2298249751329422, -1.8500316143035889, 0.8060803413391113, 1.172529697418213]
    point2.time_from_start = Duration(1.5)
    
    trajectory.points.append(point1)
    trajectory.points.append(point2)
    """
    
    # Create a trajectory message
    #trajectory = getTrajectory()
    
    #-------------------insert points here----------------------
    point1 = JointTrajectoryPoint()
    point1.positions = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    point1.time_from_start = Duration(0.0)
    trajectory.points.append(point1)
    
    file_path = 'joint_states.csv'
    data = read_csv_data(file_path)
    
    for i, row in enumerate (data):
    
        if i%3 == 0:
    	    point = JointTrajectoryPoint()
    	    values = []
    	    for value in row:
    	        values.append(float(value))
    	    point.positions = values
    	    point.time_from_start = Duration(i/100)
    	    trajectory.points.append(point)
    
    #-----------------------------------------
    
    #print(trajectory)

    # Create a goal for the action client
    goal = FollowJointTrajectoryGoal()
    goal.trajectory = trajectory
    goal.goal_time_tolerance = rospy.Duration(0.5)  # Tolerance for goal time (in seconds)

    # Send the goal to the action server and wait for the result
    rospy.loginfo("Sending trajectory goal...")
    client.send_goal(goal)
    client.wait_for_result()

    # Check the result of the action
    result = client.get_result()
    if result.error_code == 0:
        rospy.loginfo("Trajectory execution succeeded!")
    else:
        rospy.logerr("Trajectory execution failed!")
        
        
def read_csv_data(file_path):
    data = []
    
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        
        for row in reader:
            data.append(row)
    
    return data

if __name__ == '__main__':
    try:
        send_trajectory()
    except rospy.ROSInterruptException:
        pass

