import math

def vector_2d_angle(v1, v2): # 計算2D向量角度
    v1_x = v1[0]
    v1_y = v1[1]
    v2_x = v2[0]
    v2_y = v2[1]
    try:
        angle_ = math.degrees(math.acos( # math.acos 將餘弦值轉為弧度, math.degrees 將弧度轉為角度
            (v1_x * v2_x + v1_y * v2_y) / (((v1_x ** 2 + v1_y ** 2) ** 0.5) * ((v2_x ** 2 + v2_y ** 2) ** 0.5)))) # 兩向量夾角公式求餘弦
    except:
        angle_ = 180
    return angle_

def hand_angle(hand_): # 計算每根手指的角度
    angle_list = []
    angle_ = vector_2d_angle( # 大拇指角度
        ((int(hand_[0][0]) - int(hand_[2][0])), (int(hand_[0][1]) - int(hand_[2][1]))),
        ((int(hand_[3][0]) - int(hand_[4][0])), (int(hand_[3][1]) - int(hand_[4][1])))
    )
    angle_list.append(angle_)
    angle_ = vector_2d_angle( # 食指角度
        ((int(hand_[0][0]) - int(hand_[6][0])), (int(hand_[0][1]) - int(hand_[6][1]))),
        ((int(hand_[7][0]) - int(hand_[8][0])), (int(hand_[7][1]) - int(hand_[8][1])))
    )
    angle_list.append(angle_)
    angle_ = vector_2d_angle( # 中指角度
        ((int(hand_[0][0]) - int(hand_[10][0])), (int(hand_[0][1]) - int(hand_[10][1]))),
        ((int(hand_[11][0]) - int(hand_[12][0])), (int(hand_[11][1]) - int(hand_[12][1])))
    )
    angle_list.append(angle_)
    angle_ = vector_2d_angle( # 無名指角度
        ((int(hand_[0][0]) - int(hand_[14][0])), (int(hand_[0][1]) - int(hand_[14][1]))),
        ((int(hand_[15][0]) - int(hand_[16][0])), (int(hand_[15][1]) - int(hand_[16][1])))
    )
    angle_list.append(angle_)
    angle_ = vector_2d_angle( # 小姆指角度
        ((int(hand_[0][0]) - int(hand_[18][0])), (int(hand_[0][1]) - int(hand_[18][1]))),
        ((int(hand_[19][0]) - int(hand_[20][0])), (int(hand_[19][1]) - int(hand_[20][1])))
    )
    angle_list.append(angle_)
    return angle_list

def hand_pos(finger_angle): # 根據手指角度判斷手勢
    f1 = finger_angle[0] # 大拇指
    f2 = finger_angle[1] # 食指
    f3 = finger_angle[2] # 中指
    f4 = finger_angle[3] # 無名指
    f5 = finger_angle[4] # 小姆指
    # < 50 伸直, >= 50 彎曲
    if f1 >= 50 and f2 >= 50 and f3 >= 50 and f4 >= 50 and f5 >= 50: 
        return 2 # 石頭
    elif f1 >= 50 and f2 < 50 and f3 < 50 and f4 >= 50 and f5 >= 50: 
        return 1 # 剪刀
    elif f1 < 50 and f2 < 50 and f3 < 50 and f4 < 50 and f5 < 50: 
        return 0 # 布
    else:
        return 3 # ok

def int2hand(x): # 將整數轉換為手勢名稱
    int2hand = ['Paper', 'Scissor', 'Stone', 'ok'] # 布、剪刀、石頭、開始
    return int2hand[x]

def determine_winner(p1, p2): # 判斷勝負 ex: p1 = 1 (剪刀), p2 = 0 (布)
    win = [1, 2, 0] # 剪刀，石頭，布
    lose = [2, 0, 1] # 石頭，布，剪刀
    if (p1 == win[p2]):  # 1 == win[0], win[0] = 1, True
        return "Player 1 wins !"
    elif (p1 == lose[p2]): # 1 == lose[0], lose[0] = 2, False
        return "Player 2 wins !"
    else: # ex: p1 = 1, p2 = 1
        return "it is a draw !" # 1 == win[1] False, 1 == lose[1] False