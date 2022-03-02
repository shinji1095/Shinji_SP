# ---------------Socket通信の設定--------------------------------
SOCKET_HOST_ADDORESS = "192.168.11.10"
SOCKET_PORT = 1235

# ---------------無線機の設定--------------------------------
PORT_NAME = "COM7"
BAUD_RATE = 1000000

# ---------------Arduinoの設定--------------------------------
ARUDUINO_PORT = "COM6"
ARUDUINO_BAUD_RATE = 9600

# ---------------USBカメラの設定--------------------------------
"""
PCに内部カメラがある場合: 1
PCに内部カメラがない場合: 0
"""
USB_CAMERA    = 1
CAMERA_WIDTH  = 640
CAMERA_HEIGHT = 640
CAMERA_FPS    = 30

# ---------------VideoWriterの設定--------------------------------
VIDEO_RATE = CAMERA_FPS
VIDEO_SIZE = (CAMERA_WIDTH, CAMERA_HEIGHT)