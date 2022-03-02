import cv2
from time import sleep
from utils import Functions
from config import *


"""

デバイスマネージャでCOMを確認してください

Arduinoの使用ピン
+ : 13
- : GND

Config.pyファイル内でフレームレートなどの定数を変更可能

"""

# ***********************************************
# ****************** 初期設定 ********************
# ***********************************************
print("[*] 初期設定中...")
Shinji_SP = Functions()

capture = cv2.VideoCapture(USB_CAMERA)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, CAMERA_WIDTH)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, CAMERA_HEIGHT)
capture.set(cv2.CAP_PROP_FPS, CAMERA_FPS)
_, _ = capture.read()


fmt = cv2.VideoWriter_fourcc('m', 'p', '4', 'v') 
writer = cv2.VideoWriter('./result/outtest.mp4', fmt, VIDEO_RATE, VIDEO_SIZE)
print("[*] 初期設定終了!")




# ***********************************************
# ******************   接続  ********************
# ***********************************************
print("[*] 接続中...")
Shinji_SP.KODAMA_connect()
print("[*] 接続終了!")
sleep(1)





# ***********************************************
# ****************** 計測準備 ********************
# ***********************************************
print("[*] 計測準備中...")
Shinji_SP.KODAMA_prepare()
print("[*] 計測準備終了!")
sleep(1)





# ***********************************************
# ****************** 計測開始 ********************
# ***********************************************
print("[*] 計測開始")
frame_list = []
Shinji_SP.KODAMA_start()

while(True):
    _, frame = capture.read()
    frame_list.append(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break





# ***********************************************
# ****************** 計測終了 ********************
# ***********************************************
print("[*] 計測終了")
Shinji_SP.KODAMA_stop()
print("[*] データ書き込み中...")
_ = [writer.write(frame) for frame in frame_list]
capture.release()
cv2.destroyAllWindows()