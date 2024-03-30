from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, Key
import time
import random

x_coordinate_min = 780
x_coordinate_max = 830
y_coordinate = 600

mouse = Controller()

active = True

def on_press(key):
    global active
    if key == Key.esc:
        active = False
        return False
    elif key == Key.space:
        print("کلید Space فشرده شد.")
        if active:
            print("برنامه متوقف می‌شود.")
            active = False
        else:
            print("برنامه دوباره شروع به کار می‌کند.")
            active = True
        return False

def on_release(key):
    pass

with Listener(on_press=on_press, on_release=on_release) as listener:
    try:
        while active:
            x_coordinate = random.uniform(x_coordinate_min, x_coordinate_max)
            y_noise = random.randint(-5, 5)
            
            mouse.position = (x_coordinate, y_coordinate + y_noise)
            mouse.click(Button.left, 1)
            
            time.sleep(0.01)
            
    except KeyboardInterrupt:
        print("برنامه متوقف شد")
    finally:
        listener.stop()
