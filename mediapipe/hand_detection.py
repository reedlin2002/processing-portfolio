import cv2
from hand_gesture import determine_winner, hand_angle, hand_pos, int2hand

def detect_hands(hands, img2):
    return hands.process(img2)

def determine_hand_ok(img, results, center_x, fontFace, lineType):
    p1 = False
    p2 = False
    players_ready = False
    for hand_landmarks in results.multi_hand_landmarks: 
        finger_points = []
        for i in hand_landmarks.landmark: # 手的每個特徵點
            xPosition = i.x * 1080 # 相對座標轉絕對座標
            yPosition = i.y * 720 # 相對座標為標準化後的值[0, 1]之間
            finger_points.append((xPosition, yPosition))
        if finger_points: # 如果有偵測到特徵點
            finger_angle = hand_angle(finger_points) # 計算手指角度
            hand_position = hand_pos(finger_angle) # 判斷手勢
            hand_center_x = finger_points[0][0] # 取得手掌中心的 x 座標
            if hand_center_x < center_x: # 左半邊偵測
                if hand_position == 3: # 偵測到ok
                    cv2.putText(img, "ok", (200, 190), fontFace, 3, (147, 20, 255), 2, lineType)
                    p1 = True
            else: # 右半邊偵測
                if hand_position == 3: # 偵測到ok
                    cv2.putText(img, "ok", (750, 190), fontFace, 3, (147, 20, 255), 2, lineType)
                    p2 = True
    if p1 and p2:  
        players_ready = True
    return players_ready

def determine_hand_gesture(img, results, center_x, fontFace, lineType):
    left_hand_positions = [] # 左手的位置
    right_hand_positions = [] # 右手的位置
    p1_H = False
    p2_H = False
    result = ''
    for hand_landmarks in results.multi_hand_landmarks: # 取得手指關節的 x, y 座標
        finger_points = []
        for i in hand_landmarks.landmark: # 手的每個特徵點
            xPosition = i.x * 1080 # 相對座標轉絕對座標
            yPosition = i.y * 720 # 相對座標為標準化後的值[0, 1]之間
            finger_points.append((xPosition, yPosition))
        if finger_points: # 如果有偵測到特徵點
            finger_angle = hand_angle(finger_points) # 計算手指角度
            hand_position = hand_pos(finger_angle) # 判斷手勢
            hand_center_x = finger_points[0][0] # 取得手掌中心的 x 座標
            if hand_center_x < center_x: # 左半邊偵測
                left_hand_positions.append((finger_points[0], hand_position))
                p1_pos, p1_hand = left_hand_positions[0]
                if p1_hand <= 2:
                    cv2.putText(img, int2hand(p1_hand), (200, 150), fontFace, 1, (19, 69, 139), 2, lineType)
                    p1_H = True    
            elif hand_center_x >= center_x: # 右半邊偵測
                right_hand_positions.append((finger_points[0], hand_position))
                p2_pos, p2_hand = right_hand_positions[0]
                if p2_hand <= 2:
                    cv2.putText(img, int2hand(p2_hand), (750, 150), fontFace, 1, (122, 160, 255), 2, lineType)
                    p2_H = True
    if p1_H and p2_H:
        result = determine_winner(p1_hand, p2_hand)
    return p1_H, p2_H, result