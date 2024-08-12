
import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt

# Load the Excel file
file_path = r'C:\Users\Salil\Desktop\ujjwal\trtB\TrtB_adlb.xlsx'
df = pd.read_excel(file_path, sheet_name='Sheet1')  # Replace 'Sheet1' with your actual sheet name

# Display the first few rows of the dataset
print(df.head())

# Get a summary of the data
print(df.info())

# Check for missing values
print(df.isnull().sum())

# Filter the dataset for a specific parameter (e.g., Hemoglobin)
param = 'Basophils (GI/L)'
data_param = df[df['PARAM'] == param]  # Filter the DataFrame based on the condition

# Plot the change in parameter over time
plt.figure(figsize=(10, 6))
sns.lineplot(data=data_param, x='AVISIT', y='AVAL', hue='AGEGR1', marker="o")
plt.title(f'{param} Over Time by Age Group')
plt.xlabel('Visit')
plt.ylabel(f'{param} Value')
plt.xticks(rotation=45)
plt.legend(title='Age Group')
plt.grid(True)
plt.show()
