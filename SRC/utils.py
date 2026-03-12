import cv2
import numpy as np
import cvzone
from SRC.config import PREVIEW_X1, PREVIEW_X2, PREVIEW_Y1, PREVIEW_Y2

def blend_background(camera_img, background_img):
    return cv2.addWeighted(camera_img, 0.2, background_img, 0.8, 0)

def draw_ball(img, ball_img, ball_pos):
    return cvzone.overlayPNG(img, ball_img, ball_pos)

def draw_preview(img, raw_img):
    img[PREVIEW_Y1:PREVIEW_Y2, PREVIEW_X1:PREVIEW_X2] = cv2.resize(raw_img, (213, 120))
    return img

def clamp(value, min_value, max_value):
    return np.clip(value, min_value, max_value)
