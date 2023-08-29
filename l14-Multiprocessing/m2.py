import multiprocessing
import time

def worker_function(name):
    print(f"Worker {name} started")
    time.sleep(2)
    print(f"Worker {name} finished")

if __name__ == "__main__":
    # Create two processes
    p1 = multiprocessing.Process(target=worker_function, args=("Process 1",))
    p2 = multiprocessing.Process(target=worker_function, args=("Process 2",))

    # Start the processes
    p1.start()
    p2.start()

    # Wait for both processes to finish
    p1.join()
    p2.join()

    print("Both processes have finished")
