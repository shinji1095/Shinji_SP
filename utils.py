import cv2
# import RPi.GPIO as GPIO
import serial
import socket
from config import *

class Functions:
    def __init__(self):
        self.cap     = None
        self.writer  = None
        self.comport = None
        self.socket  = None
        self.arduino_comport = None

        self.alert_message = ""
        self.MODE = "KODAMA_SP" # "KODAMA_SP", "SHINJI_SP", "TEST"のいずれか

        self.prepare_command = [
                                0x55, 0x55, 0x62, 0xFF, 0xFF, 0x1F, 0x00, 0x00,0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
                                0x00, 0x00, 0x00, 0x00, 0x42, 0x01, 0x00, 0x00, 0x00, 0x5C, 0x31, 0x30, 0x30, 0x30, 0x30, 0x00, 
                                0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
                                0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
                                0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
                                0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 
                                0x00, 0x00, 0x00,0x30, 0xAA
                            ]

        self.start_command = [0x55, 0x55, 0x0B, 0xFF, 0xFF, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00, 0x42, 0x40, 0xAA]
        self.stop_command  = [0x55, 0x55, 0x05, 0xFF, 0xFF, 0x04, 0x04, 0xAA]


    def connect_sensor(self):# 接続
        if self.MODE == "KODAMA_SP":
            self.KODAMA_connect()
        elif self.MODE == "SHINJI_SP":
            self.SHINJI_connect()
        elif self.MODE == "TEST":
            pass
        else:
            print("Something wrong...")


    def KODAMA_connect(self):
        """
        Motive：LEDの点灯
        無線機：無線機の接続
        """
        # ---------------無線機の設定--------------------------------
        try:
            self.comport = serial.Serial(PORT_NAME, baudrate=BAUD_RATE, parity=serial.PARITY_NONE)
        except serial.SerialException:
            print(f"{PORT_NAME}が開いていません\n接続を確認してください")

        # ---------------Arduinoの設定--------------------------------
        try:
            self.arduino_comport = serial.Serial(ARUDUINO_PORT, baudrate=ARUDUINO_BAUD_RATE, parity=serial.PARITY_NONE)
        except serial.SerialException:
            print(f"{ARUDUINO_PORT}が開いていません\n接続を確認してください")


    def SHINJI_connect(self):
        """
        Motive　 ： LEDの点灯
        無線機　　： 無線機の接続
        Bluetooth： カメラの撮影を開始
        """
        try:
            self.comport = serial.Serial(PORT_NAME, baudrate=BAUD_RATE, parity=serial.PARITY_NONE)
        except serial.SerialException:
            print(f"{PORT_NAME}が開いていません\n接続を確認してください")

        # ---------------Arduinoの設定--------------------------------
        try:
            self.arduino_comport = serial.Serial(ARUDUINO_PORT, baudrate=ARUDUINO_BAUD_RATE, parity=serial.PARITY_NONE)
        except serial.SerialException:
            print(f"{ARUDUINO_PORT}が開いていません\n接続を確認してください")

        # ---------------Socket通信の設定--------------------------------
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((SOCKET_HOST_ADDORESS, SOCKET_PORT))
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        print("connecting start")
        print(f"open port {SOCKET_PORT}")

    def prepare_measurment(self):# 計測準備

        if self.MODE == "KODAMA_SP":
            self.KODAMA_prepare()
        elif self.MODE == "SHINJI_SP":
            self.SHINJI_prepare()
        elif self.MODE == "TEST":
            pass
        else:
            print("Something wrong...")

        print("prepare")

    def KODAMA_prepare(self):
        # ---------------無線機の計測準備--------------------------------
        self.comport.write(self.prepare_command)

        # ---------------Motiveの準備(LEDの点灯)--------------------------------
        self.arduino_comport.write("1".encode())

    def SHINJI_prepare(self):
        # ---------------無線機の計測準備--------------------------------
        self.comport.write(self.prepare_command)

        # ---------------Motiveの準備(LEDの点灯)--------------------------------
        self.arduino_comport.write("1".encode())

        # ---------------カメラの準備(Bluetooth)--------------------------------
        self.socket.send(bytes("prepare", "utf-8"))


    def start_measuerment(self):# 計測開始
        print("start")

        if self.MODE == "KODAMA_SP":
            self.KODAMA_start()
        elif self.MODE == "SHINJI_SP":
            self.SHINJI_start()
        elif self.MODE == "TEST":
            pass
        else:
            print("Something wrong...")


        

    def KODAMA_start(self):
        # ---------------無線機の計測開始--------------------------------
        self.comport.write(self.start_command)

        # ---------------Motiveの計測準開始--------------------------------
        self.arduino_comport.write("0".encode())

    def SHINJI_start(self):
        # ---------------無線機の計測開始--------------------------------
        self.comport.write(self.start_command)

        # ---------------Motiveの計測準開始--------------------------------
        self.arduino_comport.write("0".encode())

        # ---------------カメラの計測開始(Socket)--------------------------------
        self.socket.send(bytes("start", "utf-8"))


        command = self.socket.recv(1024).decode("utf-8")
        self.SHINJI_stop()

        if command == "finish":
            print("system stop properly")
        elif command == "error":
            print("Error is occured in Raspy!")
        else:
            print("Something wrong in SHINJI_start")


    def stop_measurement(self):# 計測終了

        if self.MODE == "KODAMA_SP":
            self.KODAMA_stop()
        elif self.MODE == "SHINJI_SP":
            self.SHINJI_stop()
        elif self.MODE == "TEST":
            pass
        else:
            print("Something wrong...")

        print("stop")     

    def KODAMA_stop(self):
          # ---------------無線機の計測終了--------------------------------
        self.comport.write(self.stop_command)
        self.arduino_comport.write("1".encode())

        self.comport.close()
        self.arduino_comport.close()

    def SHINJI_stop(self):
        self.comport.write(self.stop_command)
        self.arduino_comport.write("1".encode())

        self.comport.close()
        self.arduino_comport.close()
        self.socket.close()
