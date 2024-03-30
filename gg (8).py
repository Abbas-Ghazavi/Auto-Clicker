from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, Key
import time
import random
x_coordinate = 820
y_coordinate = 600

mouse = Controller()

active = True

def on_press(key):
    global active
    if key == Key.esc:
        active = False
        return False
    elif key == Key.space:
        print("key space")
        if active:
            print("stop")
            active = False
        else:
            print("start")
            active = True
        return False

def on_release(key):
    pass

with Listener(on_press=on_press, on_release=on_release) as listener:
    try:
        while active:
            x_noise = random.randint(-5, 5)
            y_noise = random.randint(-5, 5)
            
            mouse.position = (x_coordinate + x_noise, y_coordinate + y_noise)
            mouse.click(Button.left, 1)
            
            time.sleep(0.01)
            
    except KeyboardInterrupt:
        print("برنامه متوقف شد")
    finally:
        listener.stop()
