import threading

# Shared variable
counter = 0

# Create a lock
lock = threading.Lock()

# Function to increment the counter safely
def increment_counter():
    global counter
    for _ in range(100):
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
