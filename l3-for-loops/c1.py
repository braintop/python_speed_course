for num in range(1, 6):
    print(num)

sum = 0
for num in range(1, 11):
    sum += num
print("Sum:", sum)

word = "Python"
for char in word:
    print(char)

for i in range(1, 6):
    for j in range(1, 11):
        print(i, "*", j, "=", i * j)


# The enumerate function can be used to iterate over both 
# the index and the value of a sequence.
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print("Index:", index, "Fruit:", fruit)
