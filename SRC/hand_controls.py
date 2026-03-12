import cvzone
from SRC.utils import clamp
from SRC.config import LEFT_BAT_X, RIGHT_BAT_X

def handle_hands(img, hands, img_bat1, img_bat2, ball_pos, speed_x):
    if not hands:
        return img, speed_x, ball_pos

    h1, w1, _ = img_bat1.shape

    for hand in hands:
        x, y, w, h = hand['bbox']
        y1 = y - h1 // 2
        y1 = clamp(y1, 20, 415)

        if hand['type'] == "Left":
            img = cvzone.overlayPNG(img, img_bat1, (LEFT_BAT_X, y1))

            if LEFT_BAT_X < ball_pos[0] < LEFT_BAT_X + w1 and y1 < ball_pos[1] < y1 + h1:
                speed_x = int(-speed_x * 1.5)
                ball_pos[0] += 30

        elif hand['type'] == "Right":
            img = cvzone.overlayPNG(img, img_bat2, (RIGHT_BAT_X, y1))

            if RIGHT_BAT_X - 50 < ball_pos[0] < RIGHT_BAT_X and y1 < ball_pos[1] < y1 + h1:
                speed_x = int(-speed_x * 1.5)
                ball_pos[0] -= 30

    return img, speed_x, ball_pos
