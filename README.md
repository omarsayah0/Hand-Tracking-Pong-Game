# 🏓 Hand-Tracking Pong Game

A computer vision--based Pong game built with Python, OpenCV, and
MediaPipe that allows players to control paddles using their hands in
real time.

The game uses webcam hand-tracking to detect player movement and
interact with the game environment without physical controllers.

------------------------------------------------------------------------

# Introduction

This project demonstrates how computer vision and hand-tracking
technologies can be used to create an interactive game controlled
entirely by hand gestures.

Using a webcam, the system detects both hands and maps their vertical
movement to the paddles in a classic Pong-style game.

Players move their hands up and down to hit the ball and compete against
each other.

The project demonstrates several important concepts:

-   Real-time hand detection
-   Game physics and collision detection
-   Computer vision integration with interactive applications
-   Modular Python project architecture

------------------------------------------------------------------------

# 🧾 Table of Contents
- [Introduction](#Introduction)
- [Project Structure](#-Project-Structure)
- [Features](#Features)
- [Installation](#Installation)
- [Usage](#Usage)
- [System Architecture](#System-Architecture)
- [Configuration](#Configuration)
- [Game Logic](#Game-Logic)
- [Troubleshooting](#Troubleshooting)
- [Dependencies](#-Dependencies)
- [Output Snapshots](#Output-Snapshots)
- [Contributors](#-Contributors)
- [License](#-License)

------------------------------------------------------------------------

# 📁 Project Structure

    .
    ├── SRC/
    │   ├── main.py
    │   ├── config.py
    │   ├── assets.py
    │   ├── game_logic.py
    │   ├── hand_controls.py
    │   └── utils.py
    │
    ├── IMG/
    ├── SOUND/
    │
    ├── pyproject.toml
    └── README.md

------------------------------------------------------------------------

# Features

-   Real-time hand tracking using MediaPipe
-   Interactive Pong-style gameplay
-   Paddle control using hand movement
-   Ball collision detection
-   Scoring system
-   Game over screen with winner display
-   Background music playback
-   Modular Python project architecture
-   Command-line launcher (hand-pong)

------------------------------------------------------------------------

# Installation

## 1. Clone the repository

    git clone https://github.com/omarsayah0/Hand-Tracking-Pong-Game.git
    cd hand-pong

## 2. Create a virtual environment

    python -m venv venv

Activate it:

Windows

    venv\Scripts\activate

Linux / macOS

    source venv/bin/activate

## 3. Install the project

    pip install -e .

------------------------------------------------------------------------

# Usage

Start the game:

    hand-pong

The webcam will open and detect your hands.

### How to Play

-   Stand in front of the webcam
-   Move your **left hand** to control the **left paddle**
-   Move your **right hand** to control the **right paddle**
-   Hit the ball and try to score points
-   The game ends when one player reaches the winning score

------------------------------------------------------------------------

# System Architecture

The system combines computer vision with a simple game engine loop.

### Hand Detection (MediaPipe)

MediaPipe detects hand landmarks and returns bounding boxes for each
hand.

### Game Engine

Handles:

-   Ball physics
-   Paddle collisions
-   Score updates
-   Game state transitions

### Rendering

OpenCV is used to:

-   Display the game window
-   Draw overlays and graphics
-   Combine webcam feed with game visuals

------------------------------------------------------------------------

# Configuration

Game parameters can be adjusted in:

    SRC/config.py

Examples:

-   Ball speed
-   Game resolution
-   Paddle positions
-   Winning score

------------------------------------------------------------------------

# Game Logic

The game loop performs the following steps:

1.  Capture frame from webcam
2.  Detect hands using MediaPipe
3.  Update paddle positions
4.  Move the ball
5.  Detect collisions
6.  Update scores
7.  Render the game scene

This loop runs continuously for real-time gameplay.

------------------------------------------------------------------------

# Troubleshooting

If the webcam does not open:

-   Ensure your camera is connected
-   Ensure no other application is using the camera

If the game runs slowly:

-   Close other camera applications
-   Ensure your system supports OpenCV real-time processing

If dependencies fail to install:

    pip install opencv-python cvzone numpy pygame mediapipe==0.10.5

------------------------------------------------------------------------

# 📦 Dependencies

Main libraries used:

-   OpenCV
-   MediaPipe
-   cvzone
-   NumPy
-   Pygame

These install automatically with:

    pip install -e .

------------------------------------------------------------------------

# Output Snapshots

<img width="1179" height="664" alt="d1f2a7f0-d3dc-467b-9a8b-246426ba1f2d" src="https://github.com/user-attachments/assets/444555e0-45ba-459e-ab79-97ac2648323f" />

Example gameplay screenshots can be added here.

------------------------------------------------------------------------

# 👨‍💻 Contributors

**Omar Alethamat**

Feel free to open issues or pull requests.

------------------------------------------------------------------------

# 📄 License

This project is licensed under the MIT License.
