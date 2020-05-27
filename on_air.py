import pyautogui
import time
import serial
import _thread
import serial.tools.list_ports

on_air_device = None #Serial communication device

# Find which port the device is connected to
def find_device():
    print("Searching for On-Air device...")
    while(True):
        for p in list(serial.tools.list_ports.comports()):
            if "Arduino" in p.description:
                print("Found On-Air device on",p.device)
                return(p.device)
        print("Please connect the device to USB port")
        time.sleep(5)

def init_serial_com():
    global on_air_device
    on_air_device = serial.Serial(find_device(),9600)
    print("Initalizing serial communication..")
    time.sleep(5) # serial connection takes time to establish
    print("Done")

def turn_led_on():
    on_air_device.write(b'1')

def turn_led_off():
    on_air_device.write(b'0')

def do_mute_unmute(loc):
    buttonx, buttony = pyautogui.center(loc)
    pyautogui.click(buttonx, buttony)

# Listen to mute button from device
def t_read(n, d):
    while(True):
        if on_air_device.read().decode() == '1':
            pyautogui.hotkey('ctrl')  # do some activity to show hidden buttons
            time.sleep(0.1) # wait for buttons/bar to appear
            location_hangup = pyautogui.locateOnScreen('templates/hang_up.png')
            if location_hangup: # MS Teams application is in focus
                pyautogui.hotkey('ctrl', 'shift', 'm') # Mute/ Unmute

def t_main(n, d):
    while(True):
        location_hangup = pyautogui.locateOnScreen('templates/hang_up.png')
        location_muted = pyautogui.locateOnScreen('templates/muted.png')
        location_on_air = pyautogui.locateOnScreen('templates/on_air.png')

        if location_hangup: # MS Teams application is in focus
            if location_on_air:
                turn_led_on()
            elif location_muted:
                turn_led_off()

init_serial_com()

_thread.start_new_thread(t_read, ("Read", 0))
_thread.start_new_thread(t_main, ("Main", 0))

while 1:
    pass