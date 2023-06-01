#!/usr/bin/env python3

import rospy
from fanuc_msgs.srv import SetPayloadNum, SetPayloadNumRequest

def set_payload_num_client(payload_num):
    rospy.wait_for_service('/set_payload_num')
    try:
        set_payload_num = rospy.ServiceProxy('/set_payload_num', SetPayloadNum)
        request = SetPayloadNumRequest()
        request.num = int(payload_num)
        response = set_payload_num(request)
        return response.success
    except rospy.ServiceException as e:
        rospy.logerr("Service call failed: %s" % e)

if __name__ == '__main__':
    rospy.init_node('payload_num_client')
    payload_num = input("Enter the payload number: ")
    success = set_payload_num_client(float(payload_num))
    if success:
        rospy.loginfo("Payload number successfully set.")
    else:
        rospy.logerr("Failed to set payload number.")

