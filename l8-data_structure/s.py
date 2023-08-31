from collections import deque

# Create a deque
deque_example = deque([1, 2, 3, 4, 5], maxlen=5)
print("1.Deque:", deque_example)

# Append and appendleft
deque_example.append(6)
print("2.append:", deque_example)

deque_example.appendleft(0)
print("3.appendleft:", deque_example)

# Extend and extendleft
deque_example.extend([7, 8])
print("4.extend:", deque_example)
deque_example.extendleft([-1, -2])
print("5.extendleft:", deque_example)

# Pop and popleft
popped_item = deque_example.pop()
print("6.pop:", deque_example)

popped_left_item = deque_example.popleft()
print("7.popleft:", deque_example)

# Rotate
deque_example.rotate(1)
print("8.rotate:", deque_example)

