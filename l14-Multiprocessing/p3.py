import multiprocessing

def worker_function(number):
    print(f"Worker {number} started")
    result = number * 2
    print(f"Worker {number} finished with result: {result}")
    return result

if __name__ == "__main__":
    # Get the number of available CPU cores
    num_cores = multiprocessing.cpu_count()
    print(f"Number of CPU cores: {num_cores}")

    # Create a pool of worker processes
    pool = multiprocessing.Pool(processes=num_cores)

    # Map tasks to the worker processes
    tasks = [1, 2, 3, 4, 5]
    results = pool.map(worker_function, tasks)

    # Close the pool and wait for the worker processes to finish
    pool.close()
    pool.join()

    print("All worker processes have finished.")

    # Display the results
    print("Results:", results)
