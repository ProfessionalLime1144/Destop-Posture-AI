# Posture Checker for Desktop Workers
'''
1) MediaPipe pose landmark detection uses pose to determine 333
'''
from flask import Flask
import cv2
import mediapipe as mp
from mediapipe.tasks.python import vision
import numpy as np
# np are array on ndimensions, ndarray

app = Flask(__name__)

def checkPosture(landmarks):
  # Get key points for posture
  shoulder_right = landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value]
  shoulder_left = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value]
  ear_right = landmarks[mp_pose.PoseLandmark.RIGHT_EAR.value]
  hip_right = landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value]
  
  # Check if head is forward
  head_forward_angle = calculate_angle(
    [shoulder_right.x, shoulder_right.y],
    [ear_right.x, ear_right.y],
    [ear_right.x, ear_right.y - 0.5]  # Virtual point above ear
  )

    # Check if slouching
  back_angle = calculate_angle(
    [ear_right.x, ear_right.y],
    [shoulder_right.x, shoulder_right.y],
    [hip_right.x, hip_right.y]
  )

  warnings = []
  if head_forward_angle < 70:
    warnings.append("Head too far forward!")
  if back_angle < 150:
    warnings.append("You're slouching!")
      
  return warnings


# Initialize MediaPipe


'''
So now that I have this function, I need to figure out what and how checkPosture
works
'''