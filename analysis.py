import seaborn as sns
import pandas as pd

# Load the tips dataset
tips = sns.load_dataset("tips")
tips.head()
avg_bill = tips.groupby(['day', 'time'])['total_bill'].mean().reset_index()
print(avg_bill)

max_tip = tips.groupby('smoker')['tip'].max().reset_index()
print(max_tip)

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(8, 5))
sns.barplot(data=avg_bill, x='day', y='total_bill', hue='time')
plt.title('Average Total Bill by Day and Time')
plt.ylabel('Average Total Bill')
plt.show()
plt.figure(figsize=(6, 4))
sns.barplot(data=max_tip, x='smoker', y='tip', palette='coolwarm')
plt.title('Maximum Tip by Smoker Status')
plt.ylabel('Maximum Tip')
plt.show()
