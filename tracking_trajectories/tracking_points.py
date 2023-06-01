import actionlib
from control_msgs.msg import FollowJointTrajectoryAction, FollowJointTrajectoryGoal
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
import rospy
import os
from sensor_msgs.msg import JointState
from std_msgs.msg import Header

def getTrajectory():
    trajectory = JointTrajectory()
    trajectory.header = Header()
    trajectory.joint_names = ['J1', 'J2', 'J3', 'J4', 'J5', 'J6']
    # Create a trajectory point
    point = JointTrajectoryPoint()
    point.positions = [0.0 , 0.0, 0.0 , 0.0, 0.0 , 0.0]
    point.time_from_start = rospy.Duration(0.0)  # Time to reach this point (in seconds)
    trajectory.points.append(point)

    return trajectory.points