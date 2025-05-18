import cv2
import mediapipe as mp
import pyttsx3

# Initialize text-to-speech
engine = pyttsx3.init()
engine.setProperty('rate', 150)

# MediaPipe setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

# Open webcam
cap = cv2.VideoCapture(0)

# Helper function to count fingers
def count_fingers(hand_landmarks):
    tips_ids = [4, 8, 12, 16, 20]
    fingers = []

    lm_list = []
    for id, lm in enumerate(hand_landmarks.landmark):
        h, w, _ = img.shape
        cx, cy = int(lm.x * w), int(lm.y * h)
        lm_list.append((cx, cy))

    # Thumb
    if lm_list[4][0] > lm_list[3][0]:
        fingers.append(1)
    else:
        fingers.append(0)

    # Other fingers
    for tip in [8, 12, 16, 20]:
        if lm_list[tip][1] < lm_list[tip - 2][1]:
            fingers.append(1)
        else:
            fingers.append(0)

    return sum(fingers)

# Helper to speak table
def speak_table(n):
    for i in range(1, 11):
        engine.say(f"{n} times {i} is {n * i}")
    engine.runAndWait()

# Initialize counters
prev_count = 0
stable_counter = 0

while True:
    success, img = cap.read()
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        hand_landmarks = results.multi_hand_landmarks[0]
        mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        finger_count = count_fingers(hand_landmarks)

        if finger_count == prev_count:
            stable_counter += 1
        else:
            stable_counter = 0
            prev_count = finger_count

        if stable_counter == 10 and 1 <= finger_count <= 5:
            speak_table(finger_count)
            stable_counter = 0

        cv2.putText(img, f"Fingers: {finger_count}", (20, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("FingerTable", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
