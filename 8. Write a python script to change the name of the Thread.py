import threading

# Method 1: Set name during creation
def task1():
    print("\n[Method 1] Thread is running")
    
t1 = threading.Thread(target=task1, name="MyThread-1")
t1.start()
t1.join()
print("[Method 1] Thread Name:", t1.name)


# Method 2: Change name after creation
def task2():
    print("\n[Method 2] Thread is running")

t2 = threading.Thread(target=task2)
t2.start()

# Change thread name after starting
t2.name = "UpdatedThread"
t2.join()
print("[Method 2] Thread New Name:", t2.name)


# Method 3: Change name inside the running thread
def task3():
    current = threading.current_thread()
    print("\n[Method 3] Old Name:", current.name)
    
    current.name = "WorkerThread"
    print("[Method 3] New Name:", current.name)

t3 = threading.Thread(target=task3)
t3.start()
t3.join()