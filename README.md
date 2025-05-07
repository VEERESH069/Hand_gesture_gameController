# Hand_gesture_gameController

This project allows you to control a game (such as Hill Climb Racing) using hand gestures, tracked through a webcam. The script detects the position of your fingers and performs actions like accelerating, braking, or setting the car to a neutral position based on the hand gestures.

Features:

Accelerate: When all five fingers are up.
Brake: When no fingers are up (fist).
Neutral: When a combination of fingers is raised, but not all.

This project uses:

OpenCV for webcam access and image processing.
MediaPipe for hand landmark detection.
PyAutoGUI to simulate keyboard inputs.

# install the dependencies, run the following command:
pip install opencv-python mediapipe pyautogui

Install dependencies
Python (Python 3.7 or later is recommended)
OpenCV
MediaPipe
PyAutoGUI

How It Works
1. The script uses the webcam feed to track your hand gestures. Here's how the gestures map to actions:
2. All fingers up (5 fingers): Simulates pressing the "right arrow" key to accelerate.
3. No fingers up (closed fist): Simulates pressing the "left arrow" key to brake.
4. Any other combination: Sets the car to a neutral state by releasing both keys.

# Main components of the code:
1. fingers_up(hand): This function detects which fingers are up (i.e., which are extended) based on the hand landmarks detected by MediaPipe.
2. perform_action(action): This function triggers the action, such as accelerating, braking, or setting the car to neutral, using PyAutoGUI to simulate key presses.

# Usage
* Run the script.
* Make sure your webcam is functioning.
* Position your hand in front of the camera. You will be able to control the car by performing the following gestures:
* 5 fingers up: Accelerate (simulate right arrow key press).
* Fist (no fingers up): Brake (simulate left arrow key press).
* Other combinations: Set the car to a neutral state (release both keys).

Press q to exit the program.