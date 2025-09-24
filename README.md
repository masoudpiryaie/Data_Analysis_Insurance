# 🏥 Insurance Dataset - Exploratory Data Analysis (EDA)

## 📌 Project Overview
This project performs an **Exploratory Data Analysis (EDA)** on a health insurance dataset.  
The main goal is to uncover the factors that most strongly influence **medical charges** and provide actionable insights for **risk management** and **pricing strategies** in the insurance industry.

## 🎯 Objectives
- Identify the impact of **smoking status** on medical costs.  
- Analyze the relationship between **BMI** and insurance charges.  
- Explore **regional differences** in premium costs.  
- Assess how the **number of children** affects family insurance charges.  
- Profile the **highest-risk customers**.  

## 📂 Dataset
The dataset is stored in **Google Drive** and loaded into Colab using `gdown`.  
It contains the following key features:  
dataset: https://www.kaggle.com/datasets/varishabatool/data-set?resource=download&select=insurance.csv

- `age` – Age of the customer  
- `sex` – Gender of the customer  
- `bmi` – Body Mass Index  
- `children` – Number of dependents  
- `smoker` – Smoking status (`yes`/`no`)  
- `region` – Geographical region  
- `charges` – Insurance cost charged to the customer  

## 🛠️ Technologies Used
- **Python** 🐍  
- **Pandas** – Data manipulation  
- **Matplotlib / Seaborn** – Visualization  
- **gdown** – Load dataset from Google Drive  

## 📊 Analysis & Visualizations
The following analyses were conducted:
1. **Impact of Smoking** → Boxplots show smokers pay significantly higher premiums.  
2. **BMI vs Charges** → Scatterplots highlight higher costs for obese individuals (especially smokers).  
3. **Regional Differences** → Barplots indicate moderate variations by region.  
4. **Children Effect** → Families with more children face slightly higher costs.  
5. **High-Risk Customers** → The top 10% of customers are mostly smokers with high BMI.  
6. **Correlation Heatmap** → Highlights strong correlations between charges, smoking, BMI, and age.  

## ✅ Key Insights
- **Smoking, BMI, and age** are the strongest predictors of high insurance charges.  
- **Children** and **region** also affect costs but to a lesser degree.  
- High-risk profiles are typically **smokers with high BMI and older age**.  

## 💡 Recommendations
1. Adjust pricing models for **smokers** and **high-BMI customers**.  
2. Promote **health programs** (e.g., smoking cessation, weight management).  
3. Introduce **family-oriented insurance packages**.  
4. Apply **regional adjustments** for better competitiveness.  
5. Collect additional lifestyle and medical history data to enhance predictions.  

## 🚀 How to Run
1. Clone this repository:  
   ```bash
   git clone https://github.com/<your-username>/insurance-eda.git
   cd insurance-eda
