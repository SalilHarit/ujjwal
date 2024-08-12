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


param = 'Hemoglobin (mmol/L)'
data_param = df[df['PARAM'] == param]
# Calculate the change from baseline
data_param['Change_From_Baseline'] = data_param['AVAL'] - data_param['BASE']

# Plot the change from baseline over time
plt.figure(figsize=(10, 6))
sns.lineplot(data=data_param, x='AVISIT', y='Change_From_Baseline', hue='AGEGR1', marker="o")
plt.title(f'Change from Baseline in {param} Over Time by Age Group')
plt.xlabel('Visit')
plt.ylabel(f'Change in {param}')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend(title='Age Group')
plt.show()
