In this example, I'll demonstrate the concept of thread safety, race conditions, and the use of the `threading.Lock` class to synchronize access to shared resources and prevent data corruption in a multi-threaded environment.

```python
import threading

# Shared variable
counter = 0

# Create a lock
lock = threading.Lock()

# Function to increment the counter safely
def increment_counter():
    global counter
    for _ in range(100000):
        with lock:  # Acquire the lock before modifying the shared resource
            counter += 1

def main():
    # Create multiple threads
    threads = []
    for _ in range(4):
        thread = threading.Thread(target=increment_counter)
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    print("Final counter value:", counter)
    print("Main thread finished")

if __name__ == "__main__":
    main()
```

Explanation of the code:

-   Import the `threading` module.
-   Define a shared variable `counter` that multiple threads will increment.
-   Create a `threading.Lock` object named `lock`. The lock will be used to ensure exclusive access to the shared resource (`counter`).
-   Define the `increment_counter` function that increments the counter by 100,000 in a loop. The `with lock:` statement is used to acquire the lock before modifying the shared resource. This prevents multiple threads from accessing the resource simultaneously.
-   In the `main` function:
    -   Create a list of threads and start them, each targeting the `increment_counter` function.
    -   Wait for all threads to complete using the `join` method.
    -   Print the final value of the counter after all threads have finished.
    -   Print a message indicating that the main thread has finished.
-   In the `if __name__ == "__main__":` block, call the `main` function to initiate the program.

By using the `threading.Lock` class and the `with lock:` statement, we ensure that only one thread can modify the `counter` variable at a time. This prevents race conditions and data corruption that can occur when multiple threads access a shared resource concurrently.
