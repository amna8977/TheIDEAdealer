No-Screen Talking The Idea Dealer
==========================

This folder is the no-screen robot version of The Idea Dealer.
The Arduino Uno reads a physical button, and Python makes the computer or hidden speaker talk.

Basic setup:
- Button on robot
- Arduino Uno inside or behind robot
- USB cable from Arduino Uno to laptop/computer
- Laptop/computer runs robot_ideaman.py
- Speaker plays the robot voice

Files:
- robot_ideaman.py: Python program that waits for the Arduino Uno button and speaks ideas out loud.
- robot_voice.html: browser voice version that talks like the website and does not need pyttsx3.
- arduino_button/arduino_button.ino: Arduino Uno button code.
- index.html: optional website version if you ever want a screen again.
- images.jpg and Untitled design.ico: optional website assets.

Button wiring:
- One side of the button goes to Arduino pin 2.
- The other side of the button goes to Arduino GND.

Arduino setup:
1. Open arduino_button/arduino_button.ino in the Arduino IDE.
2. Connect the Arduino Uno.
3. Choose Tools > Board > Arduino Uno.
4. Choose Tools > Port and remember the COM port, like COM3.
5. Upload the sketch.

Python setup:
1. Install pyserial and pyttsx3:
   pip install pyserial pyttsx3

2. Run the robot program:
   cd C:\Users\sguls\world\robot-ideaman
   python .\robot_ideaman.py

3. Choose an input mode:
   - Type arduino to use the Arduino Uno button.
   - Type keyboard to use normal keyboard keys.

4. If you choose arduino, type the Arduino COM port when it asks.
5. Press the physical robot button or a keyboard key and The Idea Dealer will speak an idea.

Keyboard mode:
- Any normal key makes an idea.
- Press q or Esc to quit.
- This is good for testing before the Arduino button is ready.

Speaker ideas:
- Use the laptop speaker.
- Hide a Bluetooth speaker inside the robot.
- Hide a small wired USB or aux speaker inside the robot.

No monitor needed:
- The robot does not need a screen.
- The laptop/computer can sit nearby or be hidden.
- The Arduino Uno is only the button controller.
- The Python program is what makes the voice happen.

To quit the Python program, press Ctrl+C.

Browser voice option:
1. Open robot_voice.html in Chrome or Edge.
2. Click Reveal my card once so the browser allows sound.
3. Press any normal key to hear an idea.
4. Press q or Esc to stop the voice.

This option uses the browser voice, so it does not need pyttsx3.

Arduino + browser voice option:
1. Upload arduino_button/arduino_button.ino to the Arduino Uno.
2. Open robot_voice.html in Chrome or Edge.
3. Click Connect Arduino.
4. Pick the Arduino Uno serial port.
5. Press the physical robot button.

The Arduino sends "idea" over USB Serial, and the browser speaks the idea.
