Certainly! Here are some of the key functions and methods of the `queue` module in Python:

1. `queue.Queue(maxsize=0)`: Creates a new FIFO (First-In-First-Out) queue. If `maxsize` is provided and greater than 0, the queue size is limited.

2. `queue.LifoQueue(maxsize=0)`: Creates a new LIFO (Last-In-First-Out) queue.

3. `queue.PriorityQueue(maxsize=0)`: Creates a new priority queue. Elements are removed from the queue based on their priority.

4. `put(item, block=True, timeout=None)`: Adds an item to the queue. If `block` is `True`, it blocks until space is available. `timeout` sets a maximum time to block.

5. `put_nowait(item)`: Adds an item to the queue without blocking.

6. `get(block=True, timeout=None)`: Removes and returns an item from the queue. If `block` is `True`, it blocks until an item is available. `timeout` sets a maximum time to block.

7. `get_nowait()`: Removes and returns an item from the queue without blocking.

8. `empty()`: Returns `True` if the queue is empty, otherwise `False`.

9. `full()`: Returns `True` if the queue is full, otherwise `False`.

10. `qsize()`: Returns the approximate size of the queue.

11. `put(item, block=True, timeout=None)`: Adds an item to the queue. If `block` is `True`, it blocks until space is available. `timeout` sets a maximum time to block.

12. `join()`: Blocks until all items in the queue have been processed.

Here's an example demonstrating the basic usage of the `queue.Queue` class:

```python
import queue

# Create a queue
q = queue.Queue(maxsize=3)

# Put items into the queue
q.put(1)
q.put(2)
q.put(3)

# Get items from the queue
item1 = q.get()
item2 = q.get()
item3 = q.get()

print("Items:", item1, item2, item3)
print("Is queue empty?", q.empty())
```

This example creates a FIFO queue using the `queue.Queue` class. It puts three items into the queue and then retrieves and prints them. The `empty()` method is used to check if the queue is empty.
