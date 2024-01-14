
/*
write  a Ros node in cpp that publihes to the topic "/velocity", (where messages of types geometry_msgs::Twist are pubblished). The node periodically pubblishes the same message with a frequency of 5 hz
*/

#include "ros/ros.h"
#include "geometry_msgs/Twist.h"

int main(int argc, char **argv)
{
    // Initialize the ROS node
    ros::init(argc, argv, "velocity_publisher");
    ros::NodeHandle nh;

    // Create a publisher for the "/velocity" topic
    ros::Publisher velocity_pub = nh.advertise<geometry_msgs::Twist>("/velocity", 10);

    // Set the loop rate to 5 Hz
    ros::Rate loop_rate(5);

    while (ros::ok())
    {
        // Create a Twist message and set its values
        geometry_msgs::Twist velocity_msg;
        velocity_msg.linear.x = 1.0; // Set linear velocity to 1 m/s
        velocity_msg.angular.z = 0.5; // Set angular velocity to 0.5 rad/s

        // Publish the message
        velocity_pub.publish(velocity_msg);

        // Log for demonstration purposes
        ROS_INFO("Published Twist message: linear.x = %f, angular.z = %f", velocity_msg.linear.x, velocity_msg.angular.z);

        // Spin once to handle callbacks and maintain the rate
        ros::spinOnce();

        // Sleep to maintain the desired loop rate
        loop_rate.sleep();
    }

    return 0;
}

