import threading
import time


def f1():
    for num in range(5):
        print(num)
        time.sleep(1)

    print("finished")
arr = []
for n in range(4):
    t1 = threading.Thread(target=f1)  # sync 
    arr.append(t1)
for t in arr:
     t.start()
     #t.join()

for t in arr:
     t.join()
     
if t.is_alive():
    print("Thread is currently running")
else:
    print("Thread is not running")

print("all thread finished")

