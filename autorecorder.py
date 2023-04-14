from pynput import keyboard
from pynput.keyboard import KeyCode, Key, Controller
from threading import Thread
import time
import _thread as thread

from TimeStampClass import *
from timeconvert import *

is_ready = False
controller = Controller()

def create_stamp(val):
    match len(val):
        case 1:
            rtn = TimeStamp(second=val[0])
        case 2:
            rtn = TimeStamp(minute=val[0], second=val[1])
        case _:
            rtn = TimeStamp(hour=val[0], minute=val[1], second=val[2])
    rtn.showtime()
    return rtn

def main():
    global t, is_ready
    rtn = input("Enter time: ")
    val = rtn.split(" ")
    stamp = create_stamp(val)
    t = to_second(stamp)
    is_ready = True
    print("Timer set up. Press record key to being recording.")
    
main()

#Pynput methods
def on_release(key):
    global is_ready
    if key == Key.f1:
        main()
    if is_ready and key == Key.space:
        controller.tap(Key.backspace)
        controller.press(Key.f2)
        print("Start recording...")
        time.sleep(0.5)
        controller.release(Key.f2)
        time.sleep(t)
        controller.press(Key.f4)
        print("Stopped recording.")
        print("Press F1 to restart...")
        time.sleep(0.1)
        controller.release(Key.f4)
        is_ready = False
        thread.start_new_thread(main, ())
    return True

def on_press(key):
    return True

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
