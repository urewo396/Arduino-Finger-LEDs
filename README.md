# 🖐️ Finger Tracking with Arduino LEDs  

This project uses **MediaPipe** + **OpenCV** in Python to track your fingers through a webcam and light up LEDs on an Arduino based on how many fingers are up.  

## 🔧 How it works  
- Python uses **MediaPipe Hands** to detect finger landmarks in real time.  
- The number of raised fingers is sent over **Serial (USB)** to the Arduino.  
- Arduino lights up LEDs (`D8–D12`) to match the number of fingers shown.  

Example:  
- ✊ 0 fingers → no LEDs  
- ☝️ 1 finger → LED on pin 8  
- ✌️ 2 fingers → LEDs on pin 8–9  
- …and so on, up to 5 LEDs.  

## 📦 Requirements  
### Python side  
- `opencv-python`  
- `mediapipe`  
- `pyserial`  

Install with:  
```bash
pip install opencv-python mediapipe pyserial
```  

### Arduino side  
- Any board (Uno, Nano, etc.)  
- 5 LEDs + 5 resistors (e.g. 220Ω)  

## ▶️ Usage  
1. Connect Arduino and upload the provided `.ino` sketch.  
2. Run the Python script:  
   ```bash
   python finger_tracking.py
   ```  
3. Show your hand to the camera → LEDs light up depending on fingers raised.  

