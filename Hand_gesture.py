import cv2
import mediapipe as mp
import pyautogui
import time

# Setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

FINGER_TIPS = [4, 8, 12, 16, 20]  # Thumb, Index, Middle, Ring, Pinky
current_state = None  # 'accelerate', 'brake', 'neutral'

def fingers_up(hand):
    finger_states = []

    # Thumb (horizontal check)
    if hand.landmark[FINGER_TIPS[0]].x < hand.landmark[FINGER_TIPS[0] - 1].x:
        finger_states.append(1)
    else:
        finger_states.append(0)

    # Index to pinky (vertical check)
    for tip in FINGER_TIPS[1:]:
        if hand.landmark[tip].y < hand.landmark[tip - 2].y:
            finger_states.append(1)
        else:
            finger_states.append(0)

    return finger_states

def perform_action(action):
    global current_state

    if action == current_state:
        return  # Avoid repeating the same key
    current_state = action

    if action == "accelerate":
        pyautogui.keyUp("left")    # release brake if held
        pyautogui.keyDown("right") # hold accelerate
        print("Accelerating")

    elif action == "brake":
        pyautogui.keyUp("right")   # release accelerator if held
        pyautogui.keyDown("left")  # hold brake
        print("Braking")

    elif action == "neutral":
        pyautogui.keyUp("right")
        pyautogui.keyUp("left")
        print("Neutral")

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)
            fingers = fingers_up(handLms)
            count = sum(fingers)

            if count == 5:
                perform_action("accelerate")
            elif count == 0:
                perform_action("brake")
            else:
                perform_action("neutral")
    else:
        perform_action("neutral")

    cv2.imshow("Hill Climb Racing Controller", frame)
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()