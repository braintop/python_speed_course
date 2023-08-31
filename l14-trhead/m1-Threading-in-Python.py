import threading
import time

# Define a simple function that simulates a time-consuming task
def worker_function(thread_name):
    print(f"{thread_name} started")
    time.sleep(2)  # Simulate some work
    print(f"{thread_name} finished")

def main():
    print("Main thread started")

    # Create two threads
    thread1 = threading.Thread(target=worker_function, args=("Thread 1",))
    thread2 = threading.Thread(target=worker_function, args=("Thread 2",))

    # Start the threads
    thread1.start()

    thread2.start()

    # Wait for both threads to complete
    thread1.join()
    thread2.join()

    print("Main thread finished")

if __name__ == "__main__":
    main()
