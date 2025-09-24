# ==============================
# Insurance Dataset - EDA Script
# For Google Colab Execution
# ==============================

# Install (if needed in Colab)
# !pip install seaborn matplotlib pandas

# 1. Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# 2. Load dataset
# Upload your file in Colab: dataset.csv
df = pd.read_csv('dataset.csv')
print(df.head())

# 3. Basic info & statistics
print(df.info())
print(df.describe())

# 4. Preprocessing
df = pd.get_dummies(df, columns=['sex', 'region'], drop_first=True)
df['smoker'] = df['smoker'].map({'yes': 1, 'no': 0})
print(df.head())

# =======================================
# Exploratory Data Analysis (EDA)
# =======================================

# 5. Impact of Smoking on Charges
smoker_vs_non_smoker = df.groupby('smoker')['charges'].mean()
print("\nAverage charges by smoking status:\n", smoker_vs_non_smoker)

sns.boxplot(x='smoker', y='charges', data=df)
plt.title('Charges Distribution by Smoking Status')
plt.show()

# 6. BMI vs Charges
sns.scatterplot(x='bmi', y='charges', hue='smoker', data=df, alpha=0.7)
plt.title('BMI vs Charges')
plt.show()

print("Correlation between BMI and Charges:", df['bmi'].corr(df['charges']))

# 7. Regional Differences
region_charges = df.groupby(['region_northwest','region_southeast','region_southwest']).mean()['charges']
print("\nAverage charges by region (dummy-encoded):\n", region_charges)

sns.barplot(x='region_southeast', y='charges', data=df)
plt.title('Regional Impact on Charges')
plt.show()

# 8. Effect of Children
children_charges = df.groupby('children')['charges'].mean()
print("\nAverage charges by number of children:\n", children_charges)

sns.barplot(x='children', y='charges', data=df, estimator=np.mean)
plt.title('Average Charges by Number of Children')
plt.show()

# 9. High-Risk Customers (Top 10%)
top_10 = df.sort_values(by='charges', ascending=False).head(int(len(df)*0.1))
print("\nTop 10% high-charge customers (stats):\n", top_10.describe())

sns.pairplot(top_10[['age','bmi','charges','smoker']], hue='smoker')
plt.show()

# 10. Correlation Heatmap
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()
