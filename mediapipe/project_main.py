import cv2
import mediapipe as mp
import time
from hand_detection import detect_hands, determine_hand_ok, determine_hand_gesture

mp_hands = mp.solutions.hands # Mediapipe初始化
cap = cv2.VideoCapture(0)  # 開啟攝像頭
fontFace = cv2.FONT_HERSHEY_SIMPLEX  # 字體
lineType = cv2.LINE_AA  # 字體類型

if not cap.isOpened():
    print("Cannot open camera")
    exit()

w, h = 1080, 720
center_x = w // 2
game_times = 1  # 遊戲次數

while True:
    with mp_hands.Hands( # Mediapipe 手勢追蹤
            model_complexity=0, # 模型複雜度，較低的複雜度可能速度較快但精度較低
            min_detection_confidence=0.7, # 手部偵測的門檻值
            min_tracking_confidence=0.7) as hands: # 手部追蹤的門檻值
        players_ready = False
        while not players_ready: # 直到兩位玩家都偵測到ok
            ret, img = cap.read()
            img = cv2.resize(img, (w, h))
            if not ret:
                print("Cannot receive frame")
                break

            img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            results = detect_hands(hands, img2) # 偵測手掌

            cv2.line(img, (center_x - 10, 0), (center_x - 10, h), (255, 255, 255), 10)
            cv2.putText(img, "Player 1", (200, 100), fontFace, 1, (255, 0, 0), 2, lineType)
            cv2.putText(img, "Player 2", (740, 100), fontFace, 1, (255, 0, 0), 2, lineType)
            cv2.putText(img, "Show 'ok' to start the game", (340, 320), fontFace, 1, (144, 238, 144), 2, lineType)
            cv2.putText(img, "Press 'e' to close the game", (340, 360), fontFace, 1, (144, 238, 144), 2, lineType)
            if game_times >= 2:
                cv2.putText(img, "Press 'q' to close the 'result' window", (240, 400), fontFace, 1, (144, 238, 144), 2, lineType)
                if cv2.waitKey(5) == ord('q'): # 按下q可以關閉result視窗
                    cv2.destroyWindow('result')
            if results.multi_hand_landmarks: # 偵測到手
                players_ready = determine_hand_ok(img, results, center_x, fontFace, lineType)
            if players_ready:
                game_times = game_times + 1
                
            cv2.imshow('game', img)
            
            if cv2.waitKey(5) == ord('e'): # 按下e可以結束
                cap.release()
                cv2.destroyAllWindows()

        start_time = time.time()
        start = False

        while True:
            ret, img = cap.read()
            img = cv2.resize(img, (w, h))
            if not ret:
                print("Cannot receive frame")
                break
            img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            results = detect_hands(hands, img2)
            cv2.line(img, (center_x - 10, 0), (center_x - 10, h), (255, 255, 255), 10)
            cv2.putText(img, "Player 1", (200, 100), fontFace, 1, (255, 0, 0), 2, lineType)
            cv2.putText(img, "Player 2", (740, 100), fontFace, 1, (255, 0, 0), 2, lineType)

            if not start: # 倒數計時器
                elapsed_time = time.time() - start_time # ex: 10 - 10, 11 - 10, 12 - 10, 13 - 10
                countdown = max(3 - int(elapsed_time), 0) # ex: 3 - 0, 3 - 1  , 3 - 2  , 3 - 3
                if countdown > 0:
                    cv2.putText(img, f"{countdown}", (420, 480), fontFace, 10, (144, 32, 208), 5, lineType)
                else:
                    start = True
            if start:
                cv2.putText(img, "Start", (450, 250), fontFace, 2, (0, 0, 255), 2, lineType)

            if results.multi_hand_landmarks and start: # 偵測到手部關鍵點並且遊戲開始
                p1_H, p2_H, result = determine_hand_gesture(img, results, center_x, fontFace, lineType)
                if p1_H and p2_H:
                    if "wins" in result:
                        cv2.putText(img, "Player 1", (200, 100), fontFace, 1, (255, 0, 0), 2, lineType)
                        cv2.putText(img, "Player 2", (740, 100), fontFace, 1, (255, 0, 0), 2, lineType)
                        cv2.putText(img, result, (320, 360), fontFace, 2, (0, 255, 255), 5, lineType)
                        cv2.imshow('result', img)
                        break
                    else: 
                        cv2.putText(img, "Player 1", (200, 100), fontFace, 1, (255, 0, 0), 2, lineType)
                        cv2.putText(img, "Player 2", (740, 100), fontFace, 1, (255, 0, 0), 2, lineType)
                        cv2.putText(img, result, (350, 360), fontFace, 2, (0, 127, 255), 5, lineType)
                        cv2.imshow('result', img)
                        break 
                
            cv2.imshow('game', img)
            if cv2.waitKey(5) == ord('e'):
                cap.release()
                cv2.destroyAllWindows()