import cv2
import mediapipe as mp
import serial
import time

# === SERIAL SETUP ===
# Change COM3 to whatever your Arduino shows up as
ser = serial.Serial("COM3", 9600, timeout=1)
time.sleep(2)  # wait for Arduino reset

# === MEDIAPIPE SETUP ===
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

cap = cv2.VideoCapture(0)

def count_fingers(hand_landmarks):
    tips = [4, 8, 12, 16, 20]
    fingers = 0

    lm = hand_landmarks.landmark

    if lm[tips[0]].x < lm[tips[0] - 1].x:
        fingers += 1

    for tip in tips[1:]:
        if lm[tip].y < lm[tip - 2].y:
            fingers += 1

    return fingers

while True:
    ret, frame = cap.read()
    if not ret:
        break


    frame = cv2.flip(frame, 1)


    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            num_fingers = count_fingers(hand_landmarks)

            ser.write(f"{num_fingers}\n".encode())
            print("Fingers:", num_fingers)

    cv2.imshow("Finger Tracking", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
ser.close()
