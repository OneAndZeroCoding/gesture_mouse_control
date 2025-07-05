print("Program running")

import cv2
import mediapipe as mp
import time #to show fps

prev_time = 0

#Capture video from webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error opening cam")
    exit()

#Initializing mediaPipe hands module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False,
                        max_num_hands=1,
                        min_detection_confidence=0.7,
                        min_tracking_confidence=0.7)

mp_draw = mp.solutions.drawing_utils

while True:

    success, frame = cap.read()

    if not success:
        print("Failed to capture image.")
        break

    curr_time = time.time()
    fps = 1/(curr_time - prev_time)
    prev_time = curr_time

    frame = cv2.flip(frame, 1)

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #converting from BGR to RGB
    cv2.putText(frame, f'FPS: {int(fps)}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 1)

    #processing hands results
    result = hands.process(rgb_frame)
    print(result.multi_hand_landmarks)

    #drawing handLandmarks
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            #print(hand_landmarks)
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("HandTracking", frame)

    if cv2.waitKey(3000) & 0xFF == ord('q'):
        break
    

cap.release()
cv2.destroyAllWindows()


