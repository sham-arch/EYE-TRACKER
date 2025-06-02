# Blink to Text – Eye Tracking Communication System

Overview
Blink to Text is a Python-based assistive communication system designed for individuals with Locked-in Syndrome (LIS) and other severe mobility impairments. It uses real-time eye blink detection to convert blinks into meaningful text, allowing users to communicate independently using only a webcam.

Key Features
-Blink-based input system with real-time detection
-Predictive text suggestions using language modeling
-Text-to-speech output (TTS) using pyttsx3
-Live webcam GUI with PyQt5
-SMS integration with Twilio (optional)
-Runs on low-end Windows machines

System Workflow
-Detect face and eyes using Haar cascades
-Identify blinks via facial landmarks and frame differencing
-Convert detected blinks to text.
-Predict next word using autocomplete
-Output text via GUI, voice, or SMS

Tech Stack
-Language: Python
-Libraries: OpenCV, PyQt5, pyttsx3, Twilio (optional)
-Platform: Windows 10
-Tools: Haar cascades for face and eye detection

How to Run:
Clone the repo
Install dependencies:
pip install opencv-python pyqt5 pyttsx3 twilio
Make sure haarcascade_frontalface_default.xml and haarcascade_eye_tree_eyeglasses.xml are present in the haarCascades/ directory.
python blink_to_text.py
