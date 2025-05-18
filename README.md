# FingerTable: Finger-Based Multiplication Table Speaker

## Overview
This project allows you to use your hand gestures to get the multiplication table of numbers 1 to 5. It uses **MediaPipe** and **OpenCV** to detect finger gestures and speaks the multiplication table corresponding to the number of fingers raised.

### Key Features:
- Detects the number of fingers raised using **MediaPipe**.
- Speaks out the multiplication table for numbers 1-5 based on the fingers raised.
- Fun and interactive way to learn multiplication!

## How It Works:
1. **Hand Gesture Detection**: The system detects hand landmarks in real-time using **MediaPipe**.
2. **Finger Counting**: It counts the number of fingers raised.
3. **Speaks the Multiplication Table**: Based on the number of fingers raised, the system speaks the corresponding multiplication table.

## Requirements:
- Python 3.x
- **MediaPipe** (for gesture recognition)
- **OpenCV** (for camera handling)

## How to Run:
1. Clone this repository to your local machine.
2. Install the required dependencies:
   ```bash
   pip install mediapipe opencv-python
