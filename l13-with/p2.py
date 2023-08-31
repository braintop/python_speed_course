import threading

lock = threading.Lock()
with lock:
    # Code that accesses shared resource safely
# Lock is automatically released after the block
