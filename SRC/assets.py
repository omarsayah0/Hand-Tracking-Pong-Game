import cv2
import pygame
from SRC.config import (
    BACKGROUND_IMAGE,
    GAME_OVER_IMAGE,
    BALL_IMAGE,
    BAT1_IMAGE,
    BAT2_IMAGE,
    MUSIC_FILE
)

def init_audio():
    pygame.mixer.init()
    pygame.mixer.music.load(MUSIC_FILE)
    pygame.mixer.music.play(-1)

def load_images():
    assets = {
        "background": cv2.imread(BACKGROUND_IMAGE),
        "game_over": cv2.imread(GAME_OVER_IMAGE),
        "ball": cv2.imread(BALL_IMAGE, cv2.IMREAD_UNCHANGED),
        "bat1": cv2.imread(BAT1_IMAGE, cv2.IMREAD_UNCHANGED),
        "bat2": cv2.imread(BAT2_IMAGE, cv2.IMREAD_UNCHANGED),
    }
    return assets
