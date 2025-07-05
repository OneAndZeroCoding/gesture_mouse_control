import time
import math

def get_fps(prev_time, frame_count=1):
    curr_time = time.time()
    time_diff = curr_time - prev_time

    if time_diff > 0:
        fps = frame_count / time_diff
    else:
        fps = 0

    return math.floor(fps), curr_time
