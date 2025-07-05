import pyautogui as pag
import cv2
import time


screenW, screenH = pag.size()
last_click_time = 0
CLICK_COOLDOWN = 0.5
prev_mouse_x, prev_mouse_y = 0,0
MOTION_THRESHOLD = 7

#function to return list of 1/0 - 1=up, 0=down 
def get_fingers_up(hand_landmarks, frame_shape):
    fingers = []
    h, w, _ = frame_shape
    lm = hand_landmarks.landmark

    #thumb - since bends sideways
    if lm[4].x > lm[2].x:
        fingers.append(1)
    else:
        fingers.append(0)
    
    tips = [8,12,16,20]
    pips = [6,10,14,18]
    #other four fingers
    for tip, pip in zip(tips, pips):
        if lm[tip].y < lm[pip].y:
            fingers.append(1)
        else:
            fingers.append(0)

    return fingers


def move_mouse(hand_landmarks, fingers_up, frame_shape, frame):

    global prev_mouse_x, prev_mouse_y

    if fingers_up[1]==1 and sum(fingers_up)==1:
        index_tip = hand_landmarks.landmark[8]
        h,w,_ = frame_shape
        cx, cy = int(index_tip.x * w), int(index_tip.y * h)
        VISIBLE_X = 0.7
        VISIBLE_Y = 0.6

        #converting to screen coords
        mappedX, mappedY = min(index_tip.x/VISIBLE_X,1.0), min(index_tip.y/VISIBLE_Y, 1.0)
        screenX, screenY = mappedX * screenW, mappedY * screenH

        dx = abs(screenX - prev_mouse_x)
        dy = abs(screenY - prev_mouse_y)

        if dx > MOTION_THRESHOLD or dy > MOTION_THRESHOLD:
            pag.moveTo(screenX, screenY)
            prev_mouse_x, prev_mouse_y = screenX, screenY

        #feedback
        cv2.circle(frame, (cx, cy), 10, (255,0,0), cv2.FILLED)
    return None

def left_click_mouse(fingers_up, frame, frame_shape, hand_landmarks):

    global last_click_time
    current_time = time.time()

    if fingers_up == [0,1,1,0,0]:
        if current_time - last_click_time > CLICK_COOLDOWN:
            pag.click(button='left')
            print("Left click")
            last_click_time = current_time

        #feedback
        middle_tip = hand_landmarks.landmark[12]
        h,w,_ = frame_shape
        cx, cy = int(middle_tip.x * w), int(middle_tip.y * h)
        cv2.circle(frame, (cx, cy), 10, (0,0,225),cv2.FILLED)