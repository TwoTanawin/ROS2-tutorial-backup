import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose

class SimpleTurtlesimKinematics(Node):
    def __init__(self):
        super().__init__("simple_turtlesim_kinematics")

        self.turtle_pose_pub_ = self.create_subscription(Pose, "/turtle1/pose", self.turtle1PoseCallback, 10)
        self.turtle_pose_sub_ = self.create_subscription(Pose, "/turtle2/pose", self.turtle2PoseCallback, 10)

        self.last_turtle1_pose_ = Pose()
        self.last_turtle2_pose_ = Pose()

    def turtle1PoseCallback(self, msg):
        self.last_turtle1_pose_ = msg

    def turtle2PoseCallback(self, msg):
        self.last_turtle2_pose_ = msg

        Tx = self.last_turtle2_pose_.x - self.last_turtle1_pose_.x
        Ty = self.last_turtle2_pose_.y - self.last_turtle1_pose_.y

        self.get_logger().info(f"""\n
                            Translation Vector turtle -> turtle2 \n
                               Tx: {Tx}\n
                               Ty: {Ty}\n""")
        
def main():
    rclpy.init()

    Simple_TurtlesimKinematics = SimpleTurtlesimKinematics()
    rclpy.spin(Simple_TurtlesimKinematics)
    
    Simple_TurtlesimKinematics.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()