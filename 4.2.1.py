import pandas as pd

# Prompt the user for the file name
file_name = input()

# Load the data
df = pd.read_csv(file_name)


# 1. Convert Date to datetime and create a Month column (formatted as YYYY-MM)
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.strftime('%Y-%m')

# 2. Calculate Sales for each entry
df['Sales'] = df['Quantity'] * df['Price']

# 3. Group by Month and sum the sales
monthly_sales = df.groupby('Month')['Sales'].sum()

# 4. Find the month with the highest total sales
best_month = monthly_sales.idxmax()
highest_sales = monthly_sales.max()
# Find the month with the highest total sales
#best_month =
#highest_sales = 
print(f"Best month: {best_month}")
print(f"Total sales: ${highest_sales:.2f}")
