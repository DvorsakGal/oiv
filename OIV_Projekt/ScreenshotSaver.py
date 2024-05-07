import pyscreenshot as imagegrab
import schedule
from datetime import datetime
import time
import os


def take_screenshot():
    print("Taking screenshot...")
    # Format the name of the screenshot with a timestamp
    image_name = f"screenshot-{datetime.now().strftime('%Y-%m-%d_%H-%M-%S.%f')}.png"

    # Set the new path for the screenshot
    filepath_moja = f"./screenshots/{image_name}.png"
    #new_path = r"C:\FERI\2.letnik\OIV\Screenshots"
    #filepath = os.path.join(new_path, image_name)

    # Take the screenshot
    screenshot = imagegrab.grab()

    # Save the screenshot to the specified path
    screenshot.save(filepath_moja)

    print("Screenshot taken and saved to:", filepath_moja)

    return filepath_moja


def main():

    # Schedule the screenshot task
    schedule.every(5).seconds.do(take_screenshot)

    # Run the scheduler in a loop
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()