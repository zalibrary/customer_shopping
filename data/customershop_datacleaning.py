# ======================================
# DATA CLEANING
# ======================================

import pandas as pd

# Load data
df = pd.read_csv('customer_shopping_behavior.csv')

print("\n=== RAW DATA PREVIEW ===")
print(df.head())

# Rename columns
df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ', '_')
df = df.rename(columns={'purchase_amount_(usd)': 'purchase_amount'})

print("\n=== COLUMNS AFTER RENAME ===")
print(df.columns)

# Check missing values
print("\n=== MISSING VALUES ===")
print(df.isnull().sum())

# Check duplicated rows
print("\n=== DUPLICATED ROWS ===")
print(df.duplicated().sum())

# Feature engineering
labels = ['Young Adult', 'Adult', 'Middle-aged', 'Senior']
df['age_group'] = pd.qcut(df['age'], q=4, labels=labels)

frequency_mapping = {
    'Fortnightly': 14,
    'Weekly': 7,
    'Monthly': 30,
    'Quarterly': 90,
    'Bi-Weekly': 14,
    'Annually': 365,
    'Every 3 Months': 90
}
df['purchase_frequency_days'] = df['frequency_of_purchases'].map(frequency_mapping)

print("\n=== AGE GROUP CHECK ===")
print(df[['age', 'age_group']].head(10))

print("\n=== PURCHASE FREQUENCY DAYS CHECK ===")
print(df[['frequency_of_purchases', 'purchase_frequency_days']].head(10))

# Save cleaned data
df.to_csv('customer_shopping_cleaned.csv', index=False)
print("\n=== CLEANED DATA SAVED ===")
