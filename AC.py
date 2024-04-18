import time
import random
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, Key

# Define the range for x-coordinate
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
        print("press space")
        if active:
            print("stop")
            active = False
            
        else:
            print("running")
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
        print("stop")
        
    finally:
        listener.stop()
