import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the penguins dataset
penguins = sns.load_dataset("penguins")

# Display first few rows
print(penguins.head())
numeric_data = penguins.select_dtypes(include=['float64', 'int64'])

# Compute correlation matrix
corr_matrix = numeric_data.corr()

# Display the correlation matrix
print(corr_matrix)
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap - Penguins Dataset")
plt.show()