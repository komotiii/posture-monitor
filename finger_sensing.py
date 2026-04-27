import cv2
import mediapipe as mp

# MediaPipe のセットアップ
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# 手指検出の設定（静止画像=False, 最大2つの手, 検出信頼度0.5, 追跡信頼度0.5）
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Webカメラの起動
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # BGR → RGB（MediaPipeはRGBを使用）
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # 手の検出
    results = hands.process(rgb_frame)

    # 検出された手を描画
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # 映像を表示
    cv2.imshow('Hand Tracking', frame)

    # 'q'キーで終了
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 終了処理
cap.release()
cv2.destroyAllWindows()
