#!/usr/bin/env python

import rospy
from control_msgs.msg import FollowJointTrajectoryActionGoal
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from std_msgs.msg import Header
from actionlib_msgs.msg import GoalID
from rospy import Duration

def publish_trajectory():
    rospy.init_node('trajectory_publisher', anonymous=True)
    pub = rospy.Publisher('/arm_controller/follow_joint_trajectory/goal', FollowJointTrajectoryActionGoal, queue_size=10)
    rate = rospy.Rate(10)  # 10 Hz

    # Create the message
    msg = FollowJointTrajectoryActionGoal()

    # Set the header
    msg.header = Header()
    msg.header.stamp = rospy.Time.now()
    msg.header.frame_id = "base_link"

    # Set the goal ID
    msg.goal_id = GoalID()
    msg.goal_id.stamp = rospy.Time.now()
    msg.goal_id.id = "goal_id"

    # Set the trajectory
    msg.goal = FollowJointTrajectoryActionGoal().goal
    msg.goal.trajectory = JointTrajectory()

    # Set the joint names
    msg.goal.trajectory.joint_names = ['J1', 'J2', 'J3', 'J4', 'J5', 'J6']

    # Set the trajectory points
    point1 = JointTrajectoryPoint()
    point1.positions = [1.0, 0.5, 0.2, 0.0, 0.0, 0.0]
    point1.velocities = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    point1.accelerations = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    point1.effort = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    point1.time_from_start = Duration(0)

    point2 = JointTrajectoryPoint()
    point2.positions = [-2, 0.2, 0.1, 0.0, 0.0, 0.0]
    point2.velocities = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    point2.accelerations = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    point2.effort = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    point2.time_from_start = Duration(1)

    msg.goal.trajectory.points = [point1, point2]

    # Set the path tolerances
    msg.goal.path_tolerance = []
    # Set the goal tolerances
    msg.goal.goal_tolerance = []

    # Set the goal time tolerance
    msg.goal.goal_time_tolerance = Duration(2)

    while not rospy.is_shutdown():
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        publish_trajectory()
    except rospy.ROSInterruptException:
        pass

