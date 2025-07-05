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