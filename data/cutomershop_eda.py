# ======================================
# EXPLORATORY DATA ANALYSIS (EDA)
# ======================================

import pandas as pd

# Load cleaned data
df = pd.read_csv('customer_shopping_cleaned.csv')

print("\n=== DATA PREVIEW ===")
print(df.head())

print("\n=== DATA INFO ===")
print(df.info())

print("\n=== DESCRIPTIVE STATISTICS ===")
print(df.describe())

# EDA: Discount vs Promo Code
print("\n=== DISCOUNT VS PROMO CHECK ===")
print(df[['discount_applied', 'promo_code_used']].head(10))
print("\nAre both columns identical?")
print((df['discount_applied'] == df['promo_code_used']).all())

# Simple analysis
print("\n=== AVERAGE PURCHASE AMOUNT ===")
print(df['purchase_amount'].mean())

print("\n=== PURCHASE BY GENDER ===")
print(df.groupby('gender')['purchase_amount'].mean())

print("\n=== PURCHASE BY AGE GROUP ===")
print(df.groupby('age_group')['purchase_amount'].mean())