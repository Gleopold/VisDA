import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('data.csv')

# Print the first few rows of the data
print(data.head())

# Data analysis
total_revenue = data['Revenue'].sum()
average_revenue = data['Revenue'].mean()

# Data visualization
plt.figure(figsize=(10, 6))
plt.plot(data['Date'], data['Revenue'], marker='o')
plt.title('Revenue Over Time')
plt.xlabel('Date')
plt.ylabel('Revenue')
plt.grid(True)
plt.savefig('revenue_plot.png')
plt.show()
