import rclpy
from rclpy.node import Node
from rcl_interfaces.msg import SetParametersResult
from rclpy.parameter import Parameter

class simpleParameter(Node):
    def __init__(self):
        super().__init__("simple_parameter")

        self.declare_parameter("simple_int_param", 69)
        self.declare_parameter("simple_string_param", "Hello ROS2")

        self.add_on_set_parameters_callback(self.paramChangeCallback)
    
    def paramChangeCallback(self, params):
        result = SetParametersResult()

        for param in params:
            if param.name == "simple_int_param" and param.type_ == Parameter.Type.INTEGER:
                self.get_logger().info(f"Param simple_init_param change! new value is {param.value}")
                result.successful = True
            
            if param.name == "simple_string_param" and param.type_ == Parameter.Type.STRING:
                self.get_logger().info(f"Param simple_string_param change! new value is {param.value}")
                result.successful = True
        
        return result

def main():
    rclpy.init()
    simple_Parameter = simpleParameter()
    rclpy.spin(simple_Parameter)
    simple_Parameter.destroy_node()
    rclpy.shutdown()

if __name__=="__main__":
    main()