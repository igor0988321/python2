import cv2
import mediapipe as mp
import pyautogui


mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

cap = cv2.VideoCapture(0)
space_pressed = False

while True:
    success, img = cap.read()

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            index_tip = hand_landmarks.landmark[0]
            index_pip = hand_landmarks.landmark[1]

            if index_tip.y < index_pip.y:
                if not space_pressed:
                    pyautogui.press('space')
                    space_pressed = True
                else:
                    space_pressed = False