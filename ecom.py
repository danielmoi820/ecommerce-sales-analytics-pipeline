import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
file_path = "featured_ecommerce_sales_data.csv"
try:
 df = pd.read_csv(file_path)
 df.columns = df.columns.str.strip()
 print("Available column in dataset:",df.columns.tolist())
 sns.set_theme(style="whitegrid")
 plt.figure(figsize=(10, 5))
 monthly_sales =df.groupby('Order_Month')['Total'].sum().reset_index()
 sns.barplot(data=monthly_sales, x='Order_Month', y='Total',hue='Order_Month',  palette='Blues_d', legend= False)
 plt.title('Total Revenue by month', fontsize=14, fontweight='bold')
 plt.xlabel('Month', fontsize=12)
 plt.ylabel('Total Revenue ($)', fontsize=12)
 plt.xticks(rotation=45)
 plt.tight_layout()
 plt.savefig('monthly_revenue.png')
 plt.close()
 plt.figure(figsize=(10, 5))
 sns.countplot(data=df, x='Category', hue='Order_Tier',palette='Set2')
 plt.title('Order Volume by Categoryand Value Tier', fontsize=14, fontweight='bold')
 plt.xlabel('Category', fontsize=12)
 plt.tight_layout()
 plt.savefig('category_tiers.png')
 print("Saved chart :category_tiers.png")
 plt.close()
 print("\n--visualization phase complete--")

 print("\n--preliminary business insights--")
 top_category = df.groupby('Category')['Total'].sum().idxmax()
 top_revenue = df.groupby('Category')['Total'].sum().max()
 print(f"* Top Peforming Category : '{top_category}' brought in the highest total revenue (${top_revenue:,.2f}.")
 high_value_pct = (df['Order_Tier'].value_counts(normalize=True)['High Value']) * 100
 

 print(f"* Customer Tier Breakdown: {high_value_pct:.1f}% of all oders qualify as  'High Value' (> $100).")
except Exception as e:
 print(f"An error occured : {e}")# --- PRELIMINARY BUSINESS INSIGHTS (Bulletproof Version) ---
print("\n--- PRELIMINARY BUSINESS INSIGHTS ---")
top_category = df.groupby('Category')['Total'].sum().idxmax()
top_revenue = df.groupby('Category')['Total'].sum().max()
print(f"* Top Performing Category: '{top_category}' brought in total revenue (${top_revenue:,.2f}).")

# Safely calculate tier percentages without crashing
if 'Order_Tier' in df.columns:
    tier_counts = df['Order_Tier'].value_counts(normalize=True) * 100
    print(f"* Full Tier Breakdown:\n{tier_counts}")
    
    if 'High Value' in tier_counts:
        high_value_pct = tier_counts['High Value']
        print(f"* Customer Tier Breakdown: {high_value_pct:.1f}% of all orders qualify as 'High Value'.")
    else:
        print("* Notice: No 'High Value' orders (> $100) were found in this dataset.")
else:
    print("* Notice: 'Order_Tier' column was not found.")




















