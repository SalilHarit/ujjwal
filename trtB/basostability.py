import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt

file_path = r'C:\Users\Salil\Desktop\ujjwal\trtB\TrtB_adlb.xlsx'
df = pd.read_excel(file_path, sheet_name='Sheet1')  # Replace 'Sheet1' with your actual sheet name

# Display the first few rows of the dataset
print(df.head())

# Get a summary of the data
print(df.info())

# Check for missing values
print(df.isnull().sum())

param = 'Basophils (GI/L)'
data_param = df[df['PARAM'] == param]

# Plot parameter stability over time
plt.figure(figsize=(10, 6))
sns.lineplot(data=data_param, x='AVISIT', y='AVAL', hue='SUBJID', marker="o", alpha=0.6)
plt.title(f'Stability of {param} Over Time')
plt.xlabel('Visit')
plt.ylabel(f'{param} Value')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend([], [], frameon=False)  # Remove legend for clarity if too many subjects

# Save the plot as a PNG file
plt.savefig('plot.png')

# Show the plot
plt.show()
