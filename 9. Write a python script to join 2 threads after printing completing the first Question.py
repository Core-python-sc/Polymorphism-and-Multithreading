import threading
import time

# First Question Task
def first_question():
    print("Starting First Question...")
    time.sleep(3)  # simulate work
    print("First Question Completed ✅")


# Thread Task 1
def thread_task1():
    print("Thread 1 is running...")
    time.sleep(2)
    print("Thread 1 finished")


# Thread Task 2
def thread_task2():
    print("Thread 2 is running...")
    time.sleep(2)
    print("Thread 2 finished")


# Step 1: Run first question
first_question()

# Step 2: Create threads AFTER first task completes
t1 = threading.Thread(target=thread_task1)
t2 = threading.Thread(target=thread_task2)

# Step 3: Start both threads
t1.start()
t2.start()

# Step 4: Join both threads (wait until both complete)
t1.join()
t2.join()

print("Both threads completed execution 🎉")