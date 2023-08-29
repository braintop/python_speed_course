import threading
import time

def print_numbers(start, end):
    for i in range(start, end + 1):
        print(f"Number: {i}")
        time.sleep(1)

def print_letters(letters):
    for letter in letters:
        print(f"Letter: {letter}")
        time.sleep(1)

# Create threads with arguments
t1 = threading.Thread(target=print_numbers, args=(1, 5))
t2 = threading.Thread(target=print_letters, args=(['a', 'b', 'c', 'd', 'e'],))

# Start the threads
t1.start()
t2.start()

# Wait for both threads to finish
t1.join()
t2.join()

print("Both threads have finished.")
