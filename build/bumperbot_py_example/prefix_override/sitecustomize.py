import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/two-asus/ros2_ws/install/bumperbot_py_example'
