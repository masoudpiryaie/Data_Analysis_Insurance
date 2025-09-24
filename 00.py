
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('dataset.csv')
print(df.head())

print(df.info())
print(df.describe())

df = pd.get_dummies(df, columns=['sex', 'region'], drop_first=True)
df['smoker'] = df['smoker'].map({'yes': 1, 'no': 0})
print(df.head())


smoker_vs_non_smoker = df.groupby('smoker')['charges'].mean()
print("\nAverage charges by smoking status:\n", smoker_vs_non_smoker)

sns.boxplot(x='smoker', y='charges', data=df)
plt.title('Charges Distribution by Smoking Status')
plt.show()


sns.scatterplot(x='bmi', y='charges', hue='smoker', data=df, alpha=0.7)
plt.title('BMI vs Charges')
plt.show()

print("Correlation between BMI and Charges:", df['bmi'].corr(df['charges']))

region_charges = df.groupby(['region_northwest','region_southeast','region_southwest']).mean()['charges']
print("\nAverage charges by region (dummy-encoded):\n", region_charges)

sns.barplot(x='region_southeast', y='charges', data=df)
plt.title('Regional Impact on Charges')
plt.show()

children_charges = df.groupby('children')['charges'].mean()
print("\nAverage charges by number of children:\n", children_charges)

sns.barplot(x='children', y='charges', data=df, estimator=np.mean)
plt.title('Average Charges by Number of Children')
plt.show()

top_10 = df.sort_values(by='charges', ascending=False).head(int(len(df)*0.1))
print("\nTop 10% high-charge customers (stats):\n", top_10.describe())

sns.pairplot(top_10[['age','bmi','charges','smoker']], hue='smoker')
plt.show()

plt.figure(figsize=(10,6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()
