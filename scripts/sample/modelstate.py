#!/usr/bin/env python

import time
import rospy
##import rospkg 
##from std_msgs.msg import String
from geometry_msgs.msg import Pose
from gazebo_msgs.msg import ModelStates, ModelState
##from gazebo_msgs.srv import SetModelState


def main():

    rospy.init_node('modelstatetest')

    pub = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size =1)

##    models = ['unit_sphere','unit_cylinder']

##    newPose_1 = Pose()
##    newPose_2 = Pose()
##
##    
##    newPose_1.position.x = 0
##    newPose_1.position.y = 0
##    newPose_2.position.x = 0.3
##    newPose_2.position.y = 0.5
##    newPose_2.position.z = 0
##    newPose_2.orientation.z = 1
##
##    newPose = [newPose_1, newPose_2]
##
##    newState = ModelStates()
##    newState.name = models
##    newState.pose = newPose

    newState = ModelState()
    newState.model_name = 'unit_box'
    newState.reference_frame = 'world'

##    rospy.wait_for_service('/gazebo/set_model_state')
##    set_state = rospy.ServiceProxy('/gazebo/set_model_state', SetModelState)

##    for i in range(len(newState.name)):
##        an_state = ModelState()
##        an_state.model_name = newState.name[i]
##        an_state.pose = newState.pose[i]
##        set_state(an_state)
##        print(an_state)
    r = rospy.Rate(100) # 100hz

    count = 0
    limit = 5
    step = 0.1

    while not rospy.is_shutdown():
        x = count
        newState.pose.position.x = x
##        print(x)
        pub.publish(newState)
        count = count + step
        if count >= limit :
            step = -step
        elif count <= 0:
            step = -step
        r.sleep()
        



if __name__ == '__main__':

    try:
        # Main Method
        main()

    except rospy.ROSInterruptException:
        pass
    
