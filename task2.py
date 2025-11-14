# ---------------------------
# 1. Import Libraries
# ---------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# ---------------------------
# 2. Load Dataset
# ---------------------------
df = pd.read_csv("C:\\Users\\G HARSHITHA\\Downloads\\archive (3).zip")  # <-- FIXED
print("Dataset Loaded Successfully!")
print(df.head())

# ---------------------------
# 3. Basic Info + Summary Statistics
# ---------------------------
print("\n=== Dataset Info ===")
df.info()

print("\n=== Summary Statistics ===")
print(df.describe())

# ---------------------------
# 4. Missing Values
# ---------------------------
print("\n=== Missing Values ===")
print(df.isnull().sum())

# ---------------------------
# 5. Histograms
# ---------------------------
print("\n=== Histograms ===")
df.hist(figsize=(12, 8), bins=20, color='skyblue')
plt.tight_layout()
plt.show()

# ---------------------------
# 6. Boxplots
# ---------------------------
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

plt.figure(figsize=(12, 6))
df[numeric_cols].boxplot()
plt.title("Boxplots of Numerical Features")
plt.xticks(rotation=45)
plt.show()

# ---------------------------
# 7. Correlation Matrix
# ---------------------------
print("\n=== Correlation Matrix ===")
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

# ---------------------------
# 8. Pairplot
# ---------------------------
print("\n=== Pairplot ===")
sns.pairplot(df.select_dtypes(include=['int64', 'float64']))
plt.show()

# ---------------------------
# 9. Countplot - Survival Count
# ---------------------------
plt.figure(figsize=(6,4))
sns.countplot(data=df, x='Survived')
plt.title("Survival Count")
plt.show()

# ---------------------------
# 10. Countplot - Survival by Gender
# ---------------------------
plt.figure(figsize=(6,4))
sns.countplot(data=df, x='Sex', hue='Survived')
plt.title("Survival by Gender")
plt.show()

# ---------------------------
# 11. Interactive Plot
# ---------------------------
print("\n=== Interactive Age Distribution ===")
fig = px.histogram(df, x="Age", nbins=30, title="Age Distribution (Interactive)")
fig.show()

print("\n=== EDA Completed Successfully! ===")
