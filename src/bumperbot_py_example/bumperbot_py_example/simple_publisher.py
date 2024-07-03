import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SimplePublisher(Node):
    def __init__(self):
        super().__init__("simple_publisher")

        self.pub_ = self.create_publisher(String, "chatter", 10)

        self.couter_ = 0
        self.frequency_ = 1.0

        self.timmer_ = self.create_timer(self.frequency_, self.timerCallback)

        self.get_logger().info(f"Publishing at {self.frequency_} Hz")
    
    def timerCallback(self):
        msg = String()
        msg.data = f"Hello ROS2 : {self.couter_}"

        self.pub_.publish(msg)
        self.couter_ += 1

def main():
    rclpy.init()
    simple_Publisher = SimplePublisher()
    rclpy.spin(simple_Publisher)
    simple_Publisher.destroy_node()
    rclpy.shutdown()

    
if __name__=="__main__":
    main()