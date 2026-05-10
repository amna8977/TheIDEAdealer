# TheIDEAdealer
===============

The Idea Dealer is a button-powered card table that gives random coding project ideas.
Press the robot button, and the computer or website speaks an idea out loud.


What You Need
-------------

- Arduino Uno
- Push button
- Breadboard and jumper wires
- USB cable for the Arduino
- Laptop or computer
- Speaker or Bluetooth speaker
- Chrome or Edge if you want to use the website version


Project Files
-------------

- robot_ideaman.py
  Python version. Reads the Arduino button and speaks using pyttsx3.

- robot_voice.html
  Website voice version. Uses the browser voice and can connect to Arduino in Chrome or Edge.

- arduino_button/arduino_button.ino
  Arduino code. Sends the word "idea" over USB Serial when the button is pressed.

- index.html
  Visual website version of The Idea Dealer.

- voice_test.py
  Small test file for checking Python voice output.


Button Wiring
-------------

The Arduino code uses INPUT_PULLUP, so you do not need a resistor.

Wire it like this:

- One side of the button goes to Arduino pin 2.
- The opposite side of the button goes to Arduino GND.

On a breadboard:

1. Put the button across the middle gap of the breadboard.
2. Connect one button side to Arduino D2.
3. Connect the opposite button side to Arduino GND.
4. If the button does not work, rotate it 90 degrees or move the wires to the other two legs.


Upload The Arduino Code
-----------------------

1. Open arduino_button/arduino_button.ino in the Arduino IDE.
2. Plug in the Arduino Uno.
3. Choose Tools > Board > Arduino Uno.
4. Choose Tools > Port and remember the COM port, like COM3 or COM4.
5. Click Upload.
6. Close Serial Monitor before using Python or the website.


Option 1: Run With Python
-------------------------

Install the Python packages:

    pip install pyserial pyttsx3

Run the robot program:

    cd C:\Users\sguls\world\robot-ideaman
    python .\robot_ideaman.py

When it asks for mode, type:

    arduino

Then type your Arduino port, for example:

    COM3

Press the physical button. The Idea Dealer should speak a random idea.

You can also type:

    keyboard

Keyboard mode lets you test the voice without Arduino. Press any key for an idea. Press q or Esc to quit.


Option 2: Run From The Website
------------------------------

This is usually easier for browser voice and Bluetooth speakers.

Start a local web server:

    cd C:\Users\sguls\world\robot-ideaman
    python -m http.server 8000

Open this in Chrome or Edge:

    http://localhost:8000/robot_voice.html

Then:

1. Click Connect Arduino.
2. Pick the Arduino COM port.
3. Press the robot button.

The website will read "idea" from the Arduino and speak a random idea.


Bluetooth Speaker Notes
-----------------------

The sound comes from the computer or browser, not directly from the Arduino.

To use Bluetooth:

1. Connect the Bluetooth speaker in Windows.
2. Go to Settings > System > Sound.
3. Set Output to the Bluetooth speaker.
4. Restart the Python program or refresh the website.

If Python still uses the wrong speaker, open Volume Mixer and set Python or Windows Console Host to the Bluetooth output.


Troubleshooting
---------------

Access denied on COM port:

- Close Arduino IDE Serial Monitor.
- Close any browser tab connected to the Arduino.
- Stop robot_ideaman.py if it is already running.
- Unplug the Arduino, wait a few seconds, and plug it back in.
- Check Tools > Port again in Arduino IDE.

Button does nothing:

- Make sure one button side goes to D2 and the opposite side goes to GND.
- Try rotating the button 90 degrees on the breadboard.
- Make sure the Arduino sketch was uploaded.

Website cannot connect to Arduino:

- Use Chrome or Edge.
- Open the page from http://localhost:8000/robot_voice.html.
- Close Python and Arduino Serial Monitor first.

No voice:

- Turn up Windows volume.
- Check the selected output speaker.
- For Python mode, run:

    pip install pyttsx3


How It Works
------------

1. The button is pressed.
2. Arduino pin 2 connects to GND.
3. The Arduino sends "idea" over USB Serial.
4. Python or the website receives the message.
5. The Idea Dealer chooses a random project idea and speaks it.

<img width="1888" height="966" alt="image" src="https://github.com/user-attachments/assets/baf40b04-5c46-4485-b7cf-e6c82963f873" />
