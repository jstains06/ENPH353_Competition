#!/usr/bin/env python3

import rclpy
import time
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import String

class Driver_Node(Node):
    def __init__(self):
        super().__init__(node_name='driver_node')
        START_TIMER_MSG = String(data = "Team6ix,multi21,0,nothing")
        STOP_TIMER_MSG = String(data = "Team6ix,multi21,-1,nothing")

        self.score_pub_ = self.create_publisher(msg_type=String, topic='/score_tracker', qos_profile=10)
        self.cmd_vel_pub_ = self.create_publisher(msg_type=Twist, topic='/cmd_vel', qos_profile=10)
        time.sleep(2.0)

        self.score_pub_.publish(msg=START_TIMER_MSG)

        self.move = Twist()
        self.move.linear.x = 0.5
        self.move.angular.z = 0.0
        self.get_logger().info("Start driving:")
        self.cmd_vel_pub_.publish(msg=self.move)
        time.sleep(4.0)
        self.move.linear.x = 0.0
        self.get_logger().info("Stop driving:")
        self.cmd_vel_pub_.publish(msg=self.move)
        self.score_pub_.publish(msg=STOP_TIMER_MSG)

def main():
    rclpy.init(args=None)
    driver = Driver_Node()
    rclpy.spin(driver)
    rclpy.shutdown()
