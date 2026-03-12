import cv2
from cvzone.HandTrackingModule import HandDetector

from SRC.config import CAMERA_WIDTH, CAMERA_HEIGHT
from SRC.assets import load_images, init_audio
from SRC.utils import blend_background, draw_ball, draw_preview
from SRC.hand_controls import handle_hands
from SRC.game_logic import (
    create_initial_state,
    update_ball_position,
    check_goal,
    check_winner,
    draw_score,
    draw_game_over,
    reset_game
)

def setup_camera():
    cap = cv2.VideoCapture(0)
    cap.set(3, CAMERA_WIDTH)
    cap.set(4, CAMERA_HEIGHT)
    return cap

def setup_hand_detector():
    return HandDetector(detectionCon=0.8, maxHands=2)

def process_frame(cap, detector, assets, state):
    success, img = cap.read()
    if not success:
        return None

    img = cv2.flip(img, 1)
    img_raw = img.copy()

    hands, img = detector.findHands(img, flipType=False)

    img = blend_background(img, assets["background"])

    img, state["speed_x"], state["ball_pos"] = handle_hands(
        img,
        hands,
        assets["bat1"],
        assets["bat2"],
        state["ball_pos"],
        state["speed_x"]
    )

    if state["game_over"]:
        img = assets["game_over"].copy()
        img = draw_game_over(img, state["winner"])
    else:
        update_ball_position(state)
        check_goal(state)
        check_winner(state)

        if not state["game_over"]:
            img = draw_ball(img, assets["ball"], state["ball_pos"])
            img = draw_score(img, state["score"])
        else:
            img = assets["game_over"].copy()
            img = draw_game_over(img, state["winner"])

    img = draw_preview(img, img_raw)
    return img

def main():
    init_audio()
    assets = load_images()
    cap = setup_camera()
    detector = setup_hand_detector()
    state = create_initial_state()

    while True:
        img = process_frame(cap, detector, assets, state)
        if img is None:
            break

        cv2.imshow("Image", img)
        key = cv2.waitKey(1)

        if key == ord('r'):
            state = reset_game()

        elif key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
    