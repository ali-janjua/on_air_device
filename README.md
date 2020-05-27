# MS Teams On-Air device

An Arduino device consists of a red LED ligt that indicates if
someone is on-air / using microphone. User can mute/unmute either 
in MS teams and the device will show the correct state or user can 
use on device physical button to do the mute/unmute.

## Instructions
* Start the python3 script (on_air.py). If you are running for first
time then you need to install following python 3 libraries:
```
pip3 install pyautogui
pip3 install pyserial
```

* Connect the device to your computer. Script will wait for and will
  show that the device is connected.
* Start some MS teams conversation (on display #1 of you have
  multiple monitors) to verify.

## How to build the hardware
You need following things to build the hardware...
- Arduino (UNO or any other)
- Red LED light
- Push button
- Wires
- Bread board (optional)

Use any arduino board for this project. For example Arduino UNO.
- Connect a red LED to pin #13.
- Connect one pin of push button to pin #2 and other pin to ground.
- Connect the arduino to computer and upload the sketch.


## Limitations
- It only works on Dislpay #1. It means if someone has two monitors
and MS teams is running ofn Display #2, it will not work, so you have
to move the MS teams to Display #1 or change the order that your big screen
is Dislpay #1 in settings.
