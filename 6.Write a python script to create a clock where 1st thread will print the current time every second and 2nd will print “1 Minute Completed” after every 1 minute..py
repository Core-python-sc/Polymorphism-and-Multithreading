import threading
import time
from datetime import datetime

# Thread 1: Print current time every second
def show_time():
    while True:
        current_time = datetime.now().strftime("%H:%M:%S")
        print(f"Current Time: {current_time}")
        time.sleep(1)

# Thread 2: Print message every 1 minute
def minute_message():
    while True:
        time.sleep(60)
        print("⏱️ 1 Minute Completed")

# Creating threads
t1 = threading.Thread(target=show_time)
t2 = threading.Thread(target=minute_message)

# Start threads
t1.start()
t2.start()

# Optional: Keep main thread alive
t1.join()
t2.join()