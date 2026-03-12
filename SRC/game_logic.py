import cv2
from SRC.config import (
    BALL_START_POS,
    BALL_SPEED_X,
    BALL_SPEED_Y,
    TOP_LIMIT,
    BOTTOM_LIMIT,
    LEFT_GOAL_LIMIT,
    RIGHT_GOAL_LIMIT,
    WIN_SCORE
)

def create_initial_state():
    return {
        "ball_pos": BALL_START_POS.copy(),
        "speed_x": BALL_SPEED_X,
        "speed_y": BALL_SPEED_Y,
        "score": [0, 0],
        "game_over": False,
        "winner": None
    }

def update_ball_position(state):
    if state["ball_pos"][1] >= BOTTOM_LIMIT or state["ball_pos"][1] <= TOP_LIMIT:
        state["speed_y"] = -state["speed_y"]

    state["ball_pos"][0] += state["speed_x"]
    state["ball_pos"][1] += state["speed_y"]

def check_goal(state):
    if state["ball_pos"][0] < LEFT_GOAL_LIMIT:
        state["ball_pos"] = [500, 100]
        state["score"][1] += 1
        state["speed_x"] = int(-state["speed_x"] / 1.3)

    elif state["ball_pos"][0] > RIGHT_GOAL_LIMIT:
        state["ball_pos"] = [500, 100]
        state["score"][0] += 1
        state["speed_x"] = int(-state["speed_x"] / 1.3)

def check_winner(state):
    if state["score"][0] >= WIN_SCORE:
        state["game_over"] = True
        state["winner"] = "left"

    elif state["score"][1] >= WIN_SCORE:
        state["game_over"] = True
        state["winner"] = "right"

def draw_score(img, score):
    cv2.putText(img, str(score[0]), (300, 650), cv2.FONT_HERSHEY_COMPLEX, 3, (255, 0, 0), 5)
    cv2.putText(img, str(score[1]), (900, 650), cv2.FONT_HERSHEY_COMPLEX, 3, (255, 0, 0), 5)
    return img

def draw_game_over(img, winner):
    if winner == "left":
        cv2.putText(img, "left", (585, 360), cv2.FONT_HERSHEY_COMPLEX, 2, (200, 160, 80), 3)
    elif winner == "right":
        cv2.putText(img, "right", (585, 360), cv2.FONT_HERSHEY_COMPLEX, 1.6, (200, 160, 80), 3)

    return img

def reset_game():
    return create_initial_state()
