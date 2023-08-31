import multiprocessing

lock = multiprocessing.Lock()
with lock:
    # Code that accesses shared resource safely across processes
# Lock is automatically released after the block
