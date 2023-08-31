import concurrent.futures
import time

# Function to simulate a time-consuming task
def simulate_task(task_name, seconds):
    print(f"Starting task: {task_name}")
    time.sleep(seconds)
    print(f"Completed task: {task_name}")
    return task_name.upper()

def main():
    tasks = [("Task 1", 3), ("Task 2", 2), ("Task 3", 4), ("Task 4", 1)]

    # Using ThreadPoolExecutor
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as thread_executor:
        thread_results = [thread_executor.submit(simulate_task, task_name, seconds) for task_name, seconds in tasks]

        for future in concurrent.futures.as_completed(thread_results):
            result = future.result()
            print(f"Thread Result: {result}")

    # Using ProcessPoolExecutor
    with concurrent.futures.ProcessPoolExecutor(max_workers=2) as process_executor:
        process_results = [process_executor.submit(simulate_task, task_name, seconds) for task_name, seconds in tasks]

        for future in concurrent.futures.as_completed(process_results):
            result = future.result()
            print(f"Process Result: {result}")

if __name__ == "__main__":
    main()
