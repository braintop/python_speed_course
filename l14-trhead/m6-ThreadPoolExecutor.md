An example that demonstrates how to use the `ThreadPoolExecutor` and `ProcessPoolExecutor` classes from the `concurrent.futures` module to manage thread and process pools in Python.

```python
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
```

Explanation of the code:

-   Import the `concurrent.futures` module.
-   Define the `simulate_task` function that simulates a time-consuming task using `time.sleep`.
-   In the `main` function:
    -   Create a list of tasks, where each task is represented as a tuple containing the task name and the number of seconds the task takes.
    -   Use `ThreadPoolExecutor` to execute tasks using a thread pool with a maximum of 2 workers.
        -   Submit each task to the thread executor using the `submit` method, which returns a `Future` object.
        -   Use `concurrent.futures.as_completed` to iterate over completed futures and retrieve their results.
    -   Use `ProcessPoolExecutor` to execute tasks using a process pool with a maximum of 2 workers.
        -   Submit each task to the process executor using the `submit` method.
        -   Use `concurrent.futures.as_completed` to iterate over completed futures and retrieve their results.

When you run this code, you'll see that tasks are executed concurrently using thread and process pools, respectively. The `ThreadPoolExecutor` and `ProcessPoolExecutor` classes simplify the management of thread and process pools and allow you to easily perform concurrent computations in a controlled manner.
