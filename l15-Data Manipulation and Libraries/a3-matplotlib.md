Certainly! Matplotlib and Seaborn are popular libraries in Python for creating data visualizations. Matplotlib provides a flexible and comprehensive set of functions for creating various types of plots, while Seaborn builds on top of Matplotlib to provide a higher-level interface for creating aesthetically pleasing statistical visualizations. Here's an example that demonstrates some basic data visualization using both libraries:

```python
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
```

In this example, we:

1. **Create a DataFrame:**

    - We create a DataFrame `df` similar to the previous example.

2. **Set Seaborn Style:**

    - We set the style for Seaborn using `sns.set()`. In this case, we're using the "whitegrid" style.

3. **Create a Bar Plot with Matplotlib:**

    - We use Matplotlib to create a bar plot showing the age distribution for each person.

4. **Create a Scatter Plot with Seaborn:**
    - We use Seaborn to create a scatter plot that visualizes the relationship between age, city, and name. Different colors and sizes are used to represent different names and ages.

Both Matplotlib and Seaborn offer a wide range of customization options for creating various types of plots. They are widely used in data analysis and visualization projects to effectively communicate insights from data.
