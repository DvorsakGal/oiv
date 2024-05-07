import tkinter as tk
from subprocess import Popen

import sys
print(sys.executable)

import os
print("Current Working Directory:", os.getcwd())

# Global variable to hold the process
process_screenshot_saver = None
process_keylogger = None
process_screen_recorder = None

def run_keylogger():
    global process_keylogger
    # Ensure no previous process is running
    if process_keylogger is not None:
        process_keylogger.terminate()
    process_keylogger = Popen([sys.executable, "C:/FERI/2.letnik/OIV/OIV_Projekt/main.py"])

def stop_keylogger():
    global process_keylogger
    if process_keylogger is not None:
        process_keylogger.terminate()
        process_keylogger = None
    print("Keylogger stopped")

def run_clipboard_manager():
    # Run your clipboard manager Python script
    Popen([sys.executable, "C:/FERI/2.letnik/OIV/OIV_Projekt/ClipManager.py"])

def run_screenshot_saver():
    global process_screenshot_saver
    # Ensure no previous process is running
    if process_screenshot_saver is not None:
        process_screenshot_saver.terminate()
    process_screenshot_saver = Popen([sys.executable, "C:/FERI/2.letnik/OIV/OIV_Projekt/ScreenshotSaver.py"])

def stop_screenshot_saver():
    global process_screenshot_saver
    if process_screenshot_saver is not None:
        process_screenshot_saver.terminate()
        process_screenshot_saver = None
    print("Screenshot Saver stopped")

def run_screen_recorder():
    global process_screen_recorder
    # Ensure no previous process is running
    if process_screen_recorder is not None:
        process_screen_recorder.terminate()
    process_screen_recorder = Popen([sys.executable, "C:/FERI/2.letnik/OIV/OIV_Projekt/ScreenRecorder.py"])
    print("Running screen recorder")

def stop_screen_recorder():
    global process_screen_recorder
    if process_screen_recorder is not None:
        process_screen_recorder.terminate()
        process_screen_recorder = None
    print("Screen Recorder stopped")


# Create the main window
root = tk.Tk()
root.title("Cybersecurity Tools")

# Create a button to run the keylogger
btn_keylogger = tk.Button(root, text="Start Keylogger", command=run_keylogger)
btn_keylogger.pack(pady=20)

# Create a button to stop the keylogger
btn_stop_keylogger = tk.Button(root, text="Stop Keylogger", command=stop_keylogger)
btn_stop_keylogger.pack(pady=20)

# Create a button to run the clipboard manager
btn_clipboard_manager = tk.Button(root, text="Start Clipboard Manager", command=run_clipboard_manager)
btn_clipboard_manager.pack(pady=20)

# Create a button to run the screenshot saver
btn_screenshot_saver = tk.Button(root, text="Start Screenshot Saver", command=run_screenshot_saver)
btn_screenshot_saver.pack(pady=20)

# Create a button to stop the screenshot saver
btn_stop_screenshot_saver = tk.Button(root, text="Stop Screenshot Saver", command=stop_screenshot_saver)
btn_stop_screenshot_saver.pack(pady=20)

# Create a button to run the screen recorder
btn_screenshot_saver = tk.Button(root, text="Start Screen Recorder", command=run_screen_recorder)
btn_screenshot_saver.pack(pady=20)

# Create a button to stop the screen recorder
btn_stop_screenshot_saver = tk.Button(root, text="Stop Screen Recorder", command=stop_screen_recorder)
btn_stop_screenshot_saver.pack(pady=20)

# Start the GUI event loop
root.mainloop()
