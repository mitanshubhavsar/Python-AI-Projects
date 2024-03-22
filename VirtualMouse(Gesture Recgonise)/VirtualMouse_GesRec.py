import cv2
import mediapipe as mp
import pyautogui
import datetime
cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
index_y = 0
time_stamp = datetime.datetime.now().strftime('%H-%M-%S')
file_name = f'{time_stamp}.PNG'
while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x*frame_width)
                y = int(landmark.y*frame_height)
                #print(x,y)
                if id  == 8:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 255))
                    index_x = screen_width/frame_width*x
                    index_y = screen_height/frame_height*y
                    pyautogui.moveTo(index_x, index_y)
                if id  == 4:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 0))
                    thumb_x = screen_width/frame_width*x
                    thumb_y = screen_height/frame_height*y
                    print('outside', abs(index_y - thumb_y))
                    if abs(index_y - thumb_y) < 20:
                        #print('click')
                        pyautogui.click()
                        pyautogui.sleep(1)
                    #cv2.line(frame, (index_y), (thumb_y), (0, 255, 0),3)
                if id == 12:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(255, 255, 0))
                    mid_x = screen_width/frame_width*x
                    mid_y = screen_height/frame_height*y
                    if abs(index_y - mid_y) < 10:
                        #print('scroll')
                        pyautogui.scroll(10)
                if id == 20:
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(255, 0, 0))
                    ring_x = screen_width/frame_width*x
                    ring_y = screen_height/frame_height*y
                    if abs(index_y - ring_y) > 100:
                        screenshot = pyautogui.screenshot()
                        captured_screenshot = pyautogui.screenshot(imageFilename=file_name)
                        print('Screenshot time 🤟')

    #print(hands)
    cv2.imshow('MYVirtualMouseGR', frame)
    #cv2.waitKey(1)
    if cv2.waitKey(10) == ord('q'):
        break