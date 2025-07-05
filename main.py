import cv2
import time #to show fps

prev_time = 0
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error opening cam")
    exit()
while True:
    curr_time = time.time()
    fps = 1/(curr_time - prev_time)
    prev_time = curr_time

    success, frame = cap.read()

    if not success:
        print("Failed to capture image.")
        break

    frame = cv2.flip(frame, 1)
    cv2.putText(frame, f'FPS: {int(fps)}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    cv2.imshow("Webcam", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    

cap.release()
cv2.destroyAllWindows()