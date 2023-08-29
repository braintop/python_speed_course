import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Create a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 22],
        'City': ['New York', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)

# Set style for Seaborn
sns.set(style="whitegrid")

# Create a bar plot using Matplotlib
plt.figure(figsize=(8, 6))
plt.bar(df['Name'], df['Age'], color='blue')
plt.xlabel('Name')
plt.ylabel('Age')
plt.title('Age Distribution')
plt.show()

# Create a scatter plot using Seaborn
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Age', y='City', data=df, hue='Name', size='Age', sizes=(50, 200), legend='brief')
plt.xlabel('Age')
plt.ylabel('City')
plt.title('Scatter Plot')
plt.show()
