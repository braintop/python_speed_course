# In this example, we have a shared counter that multiple 
# threads attempt to increment by a large number of iterations.
# Since the counter update is not synchronized, race conditions occur,
# and the result may not be what we expect due to the
# interleaving of thread operations.

# Without proper resource management and synchronization,
# the final counter value may be lower than expected. 
# This demonstrates the need for proper synchronization mechanisms
#     like locks or semaphores to prevent data corruption and 
# ensure consistent results in a multi-threaded environment.

# To fix this, you can use synchronization mechanisms like
# threading.Lock to protect the critical section of code where
# the counter is being modified. Proper synchronization ensures 
# that only one thread can access the shared resource at a time,
# avoiding race conditions and ensuring consistent behavior.


import threading

# Shared counter
counter = 0

# Lock for synchronization
counter_lock = threading.Lock()

# Function to increment the counter
def increment_counter():
    global counter
    for _ in range(1000000):
        with counter_lock:
            counter += 1

def main():
    # Create multiple threads
    threads = [threading.Thread(target=increment_counter) for _ in range(5)]
    
    # Start the threads
    for thread in threads:
        thread.start()
    
    # Wait for all threads to finish
    for thread in threads:
        thread.join()
    
    # Print the final counter value
    print("Final counter value:", counter)

if __name__ == "__main__":
    main()
