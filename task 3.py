import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Sales': [200, 220, 230, 210, 240, 250, 270, 260, 280, 300, 320, 310],
    'Expenses': [150, 160, 170, 155, 180, 190, 200, 195, 210, 220, 230, 225]
}

# Create DataFrame
df = pd.DataFrame(data)

# Bar Chart
plt.figure(figsize=(10, 5))
plt.bar(df['Month'], df['Sales'], color='blue', label='Sales')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Monthly Sales')
plt.legend()
plt.show()

# Line Chart
plt.figure(figsize=(10, 5))
plt.plot(df['Month'], df['Sales'], marker='o', linestyle='-', color='blue', label='Sales')
plt.plot(df['Month'], df['Expenses'], marker='o', linestyle='-', color='red', label='Expenses')
plt.xlabel('Month')
plt.ylabel('Amount')
plt.title('Monthly Sales and Expenses')
plt.legend()
plt.show()
