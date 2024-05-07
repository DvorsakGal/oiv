import cv2      #opencv-python installi
import numpy as np
import pyautogui
import time
import os



def record(duration_seconds=10):
    if not os.path.exists("./videos"):
        os.makedirs("./videos")

    SCREEN_SIZE=(1920,1080)
    fps = 30
    prev=0


    fourcc=cv2.VideoWriter_fourcc(*"XVID")
    out= cv2.VideoWriter(f"./videos/output-{str(time.time())}.avi", fourcc, 15.0, (SCREEN_SIZE))


    start_time=time.time()

    while time.time()-start_time<duration_seconds:
        time_elapsed=time.time()-prev
        img = pyautogui.screenshot()

        if time_elapsed>1/fps:
            prev=time.time()
            frame= np.array(img)
            frame= cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            out.write(frame)

    cv2.destroyAllWindows()
    out.release()
    print(time.time())

if __name__ == '__main__':
    record(20)