import multiprocessing

def sender(queue, pipe):
    message_queue = "Hello from Queue!"
    message_pipe = "Hello from Pipe!"
    
    # Sending data using Queue
    queue.put(message_queue)
    
    # Sending data using Pipe
    pipe.send(message_pipe)
    pipe.close()

def receiver(queue, pipe):
    # Receiving data from Queue
    message_queue = queue.get()
    print("Received from Queue:", message_queue)
    
    # Receiving data from Pipe
    message_pipe = pipe.recv()
    print("Received from Pipe:", message_pipe)

def main():
    # Create a Queue for communication
    queue = multiprocessing.Queue()
    
    # Create a Pipe for communication
    parent_conn, child_conn = multiprocessing.Pipe()
    
    # Create sender and receiver processes
    sender_process = multiprocessing.Process(target=sender, args=(queue, child_conn))
    receiver_process = multiprocessing.Process(target=receiver, args=(queue, parent_conn))
    
    # Start processes
    sender_process.start()
    receiver_process.start()
    
    # Wait for processes to finish
    sender_process.join()
    receiver_process.join()

if __name__ == "__main__":
    main()
