import threading
import time

# The function that will be executed in the thread
def thread_func():
    print("Thread is running...")
    time.sleep(2)  # Simulating some work
    print("Thread has finished.")

# Create a thread object with the target function and a name
t = threading.Thread(target=thread_func, name="MyThread")

# Output before starting the thread
print("Before starting thread.")

# Start the thread's execution
t.start()

# Check if the thread is still running
if t.is_alive():
    print("Thread is still running.")

# Wait for the thread to finish
t.join()

# Output after joining the thread
print("After joining thread.")

# Print thread-related information
print(f"Thread name: {t.name}")
print(f"Thread ID: {t.ident}")
print(f"Thread is daemon: {t.daemon}")
