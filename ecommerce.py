import pandas as pd
file_path = "messy_ecommerce_sales_data.csv"
try :
 df = pd.read_csv(file_path)
 print("CSV loaded successfully! Here are the first few rows:")
 print(df.head())
except FileNotFoundError:
 print(f"Error:The file{messy_eommerce_sales_data.csv} was not found." )
except Exception as e:
 print(f"An expected error occured:  {e}")

try:
 df = pd.read_csv(file_path)
 print("--First 5 Rows --")
 print(df.head())
 print("\n --Data set Info(columns & types)--")
 print(df.info())
 print("\n--Missing values per column--")
 print(df.isnull().sum())
except  FileNotFoundError:
 print(f"Error: The file '{file_path}'was not found")
except Exception as e:
 print(f"An unexpecte error occured :{e}" )

try:

 df['Price'] = pd.to_numeric(df['Price'].astype(str).str.replace(r'[^0-9.]','',regex=True),errors='coerce')
 df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
 df['Order_date'] = pd.to_datetime(df['Order_Date'], errors='coerce')

 if 'Category' in df.columns:
    df['Category'] = df['Category'].fillna('Unknown')
 df = df.dropna(subset=['Price', 'Quantity'])
 initial_count = len(df)
 df = df.drop_duplicates()
 print(f"Remove {initial_count - len(df)}duplicate rows.")
 print("\n--DATA cleaning successful--")
 print(f"Cleaned dataset shape :{df.shape}")
 print("\n New Data Types:")
 print(df.dtypes)
 print("\nFirst 3 rows of cleaned data:")
 print(df.head(3))
except FileNotFoundError:
 print(f"Error: The file '{file_path}' was not found.")
except Exception as e:

 print (f"An unexpected error occur:{e}")
df['Total'] = df['Price'] * df['Quantity']

output_file_path = "cleaned_ecommerce_sales_data.csv"
df.to_csv(output_file_path, index=False)
print(f"\cleaned data successfully saved to'{output_file_path}'!")



















import pandas as pd
file_path = "messy_ecommerce_sales_data.csv"
try :
 df = pd.read_csv(file_path)
 print("CSV loaded successfully! Here are the first few rows:")
 print(df.head())
except FileNotFoundError:
 print(f"Error:The file{messy_eommerce_sales_data.csv} was not found." )
except Exception as e:
 print(f"An expected error occured:  {e}")

try:
 df = pd.read_csv(file_path)
 print("--First 5 Rows --")
 print(df.head())
 print("\n --Data set Info(columns & types)--")
 print(df.info())
 print("\n--Missing values per column--")
 print(df.isnull().sum())
except  FileNotFoundError:
 print(f"Error: The file '{file_path}'was not found")
except Exception as e:
 print(f"An unexpecte error occured :{e}" )

try:

 df['Price'] = pd.to_numeric(df['Price'].astype(str).str.replace(r'[^0-9.]','',regex=True),errors='coerce')
 df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
 df['Order_date'] = pd.to_datetime(df['Order_Date'], errors='coerce')

 if 'Category' in df.columns:
    df['Category'] = df['Category'].fillna('Unknown')
 df = df.dropna(subset=['Price', 'Quantity'])
 initial_count = len(df)
 df = df.drop_duplicates()
 print(f"Remove {initial_count - len(df)}duplicate rows.")
 print("\n--DATA cleaning successful--")
 print(f"Cleaned dataset shape :{df.shape}")
 print("\n New Data Types:")
 print(df.dtypes)
 print("\nFirst 3 rows of cleaned data:")
 print(df.head(3))
except FileNotFoundError:
 print(f"Error: The file '{file_path}' was not found.")
except Exception as e:
 print (f"An unexpected error occur:{e}")





















import pandas as pd
file_path = "messy_ecommerce_sales_data.csv"
try :
 df = pd.read_csv(file_path)
 print("CSV loaded successfully! Here are the first few rows:")
 print(df.head())
except FileNotFoundError:
 print(f"Error:The file{messy_eommerce_sales_data.csv} was not found." )
except Exception as e:
 print(f"An expected error occured:  {e}")

try:
 df = pd.read_csv(file_path)
 print("--First 5 Rows --")
 print(df.head())
 print("\n --Data set Info(columns & types)--")
 print(df.info())
 print("\n--Missing values per column--")
 print(df.isnull().sum())
except  FileNotFoundError:
 print(f"Error: The file '{file_path}'was not found")
except Exception as e:
 print(f"An unexpecte error occured :{e}" )

try:

 df['Price'] = pd.to_numeric(df['Price'].astype(str).str.replace(r'[^0-9.]','',regex=True),errors='coerce')
 df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
 df['Order_date'] = pd.to_datetime(df['Order_Date'], errors='coerce')

 if 'Category' in df.columns:
    df['Category'] = df['Category'].fillna('Unknown')
 df = df.dropna(subset=['Price', 'Quantity'])
 initial_count = len(df)
 df = df.drop_duplicates()
 print(f"Remove {initial_count - len(df)}duplicate rows.")
 print("\n--DATA cleaning successful--")
 print(f"Cleaned dataset shape :{df.shape}")
 print("\n New Data Types:")
 print(df.dtypes)
 print("\nFirst 3 rows of cleaned data:")
 print(df.head(3))
except FileNotFoundError:
 print(f"Error: The file '{file_path}' was not found.")
except Exception as e:
 print (f"An unexpected error occur:{e}")







































