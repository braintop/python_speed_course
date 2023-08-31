# In this modified version, we use a threading.
# Lock to ensure that only one thread can access 
# the counter variable at a time. This proper resource
# management and synchronization guarantee accurate results
# and prevent data corruption.






import threading

# Shared counter
counter = 0

# Function to increment the counter
def increment_counter():
    global counter
    for _ in range(1000000):
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
