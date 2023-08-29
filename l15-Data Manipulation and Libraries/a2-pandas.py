import pandas as pd

# Create a DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 22],
        'City': ['New York', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)

# Display the DataFrame
print("DataFrame:")
print(df)

# Accessing columns
names = df['Name']
ages = df['Age']

print("\nNames:")
print(names)
print("\nAges:")
print(ages)

# Filtering data
young_people = df[df['Age'] < 30]
print("\nPeople under 30:")
print(young_people)

# Grouping and aggregation
grouped_cities = df.groupby('City')['Age'].mean()
print("\nAverage age by city:")
print(grouped_cities)
