import threading
import time
import random
import queue  # Import the queue module

# Event for thread synchronization
event = threading.Event()

# Condition for thread communication
condition = threading.Condition()

# Queue for inter-thread communication
queue = queue.Queue()

# Producer thread
def producer():
    for i in range(5):
        item = f"Item {i}"
        print(f"Producing {item}")
        queue.put(item)
        time.sleep(random.uniform(0.1, 0.5))
    event.set()  # Signal the end of production

# Consumer thread
def consumer():
    event.wait()  # Wait for the producer to finish
    while not queue.empty():
        item = queue.get()
        print(f"Consuming {item}")
        time.sleep(random.uniform(0.1, 0.5))

def main():
    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()

    print("Main thread finished")

if __name__ == "__main__":
    main()
