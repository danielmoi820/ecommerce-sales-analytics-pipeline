import pandas as pd
file_path = "cleaned_ecommerce_sales_data.csv"
try: 
   df =pd.read_csv(file_path)
   df['Order_Date'] = pd.to_datetime(df['Order_Date'], format='mixed')

   print("--Starting feature engineering --")
   df['Order_Month'] = df['Order_Date'].dt.month_name()
   df['Order_Day_OfWeek'] = df['Order_Date'].dt.day_name()
   df['Order_Tier'] =df['Total'].apply(lambda x: 'High value' if x >100 else 'Standard')

   print("New features added successfully!")
   print (df[['Order_Date', 'Order_Month', 'Order_Day_OfWeek','Total','Order_Tier']].head(3))
   output_path = "featured_ecommerce_sales_data.csv"
   df.to_csv(output_path, index=False)
   print(f"\nDataset with new featuressaved to '{output_path}'!")
except Exception as e:
   print (f"An error occured : {e}")

