#!/usr/bin/env python

import rospy
from diagnostic_msgs.srv import AddDiagnostics, AddDiagnosticsRequest

def main():
    # Initialize the ROS node
    rospy.init_node('diagnostics_client_node')

    # Wait for the "/diagnostics" service to become available
    rospy.wait_for_service('/diagnostics')


        # Create a service proxy for the "/diagnostics" service
    add_diagnostics = rospy.ServiceProxy('/diagnostics', AddDiagnostics)

        # Create a request message
    request = AddDiagnosticsRequest()
    request.load_namespace = "robot"

        # Send the request to the service
    response = add_diagnostics(request)

        # Check the success field of the response
    if response.success:
            # Print the message field on the terminal
            rospy.loginfo("Diagnostics request successful. Message: %s", response.message)
    else:
            rospy.logerr("Diagnostics request failed. Error message: %s", response.message)

 
if __name__ == "__main__":
    main()

