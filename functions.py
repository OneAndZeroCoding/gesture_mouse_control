import time
import math
import cv2
import psutil as psu
import os

def get_fps(prev_time, frame_count=1):
    curr_time = time.time()
    time_diff = curr_time - prev_time

    if time_diff > 0:
        fps = frame_count / time_diff
    else:
        fps = 0

    return math.floor(fps), curr_time


def no_hand_text(frame, frame_shape):
    h,w,_ = frame_shape
    cv2.putText(frame, "NO HAND FOUND", (w-200, 30),cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,225), 2)


#accurate calculation.
process = psu.Process(os.getpid())
last_sample_time = time.time()
last_cpu_percent = 0.0

def show_process_info(frame):

    global last_sample_time, last_cpu_percent
    now = time.time()

    if now - last_sample_time > 1.0:
        last_cpu_percent = process.cpu_percent(interval=None)
        last_sample_time = now
    mem = process.memory_info().rss / (1024*1024)
    cv2.putText(frame, f"CPU%: {round(last_cpu_percent,2)}% | Memory: {round(mem,2)}MB", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0),1)