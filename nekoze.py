import cv2
import mediapipe as mp
import numpy as np
import time
import pygame
from pathlib import Path

pygame.mixer.init()

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

def point_line_distance(point, line_start, line_end):
    x0, y0 = point
    x1, y1 = line_start
    x2, y2 = line_end

    numerator = abs((y2 - y1) * x0 - (x2 - x1) * y0 + x2 * y1 - y2 * x1)
    denominator = np.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)
    return numerator / denominator

def calculate_swing(landmarks):
    if landmarks:
        nose = landmarks[mp_pose.PoseLandmark.NOSE.value]
        left_shoulder = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value]
        right_shoulder = landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value]

        if left_shoulder and right_shoulder:
            shoulder_line_start = (left_shoulder.x, left_shoulder.y)
            shoulder_line_end = (right_shoulder.x, right_shoulder.y)

            nose_position = (nose.x, nose.y)
            distance = point_line_distance(nose_position, shoulder_line_start, shoulder_line_end)

            return distance
    return 0

last_checked_time = time.time()

distance = 1.0

sound_path = Path(__file__).with_name("be.mp3")
bad_posture_sound = None
if sound_path.exists():
    bad_posture_sound = pygame.mixer.Sound(str(sound_path))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(frame_rgb)

    if results.pose_landmarks:
        mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        distance = calculate_swing(results.pose_landmarks.landmark)

        text = f"Distance: {distance:.3f}"
        cv2.putText(frame, text, (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        if distance > 0.05:
            cv2.putText(frame, "Good Posture", (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        else:
            cv2.putText(frame, "Bad Posture", (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    current_time = time.time()
    if current_time - last_checked_time >= 1:
        if distance <= 0.05 and bad_posture_sound is not None:
            bad_posture_sound.play()
        last_checked_time = current_time

    cv2.imshow("Posture Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
