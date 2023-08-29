import csv
import json

# Writing to a CSV file
data = [['Name', 'Age'], ['Alice', 25], ['Bob', 30]]
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

# Reading from a CSV file
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Writing to a JSON file
data = {'name': 'Alice', 'age': 25}
with open('data.json', 'w') as file:
    json.dump(data, file)

# Reading from a JSON file
with open('data.json', 'r') as file:
    data = json.load(file)
    print(data)
