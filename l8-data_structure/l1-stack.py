from collections import deque

# Creating a stack using deque
stack = deque()

# Pushing items onto the stack
stack.append(5)
stack.append("a1")
stack.append(20)

# Peeking at the top item
print("0", stack[0])
print("1", stack[1])
print("2", stack[2])
print("Top item:", stack[-1])

# Popping items from the stack
print("Popped:", stack.pop())
print("Popped:", stack.pop())

# Checking if the stack is empty
print("Is stack empty?", not stack)

# Getting the size of the stack
print("Stack size:", len(stack))
