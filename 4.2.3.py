import pandas as pd

# Prompt the user for the file name
file_name = input()

# Load the data
df = pd.read_csv(file_name)

# write the code..
# 1. Group by City and sum the Quantity
city_sales = df.groupby('City')['Quantity'].sum()

# 2. Find the city with the highest total quantity
best_city = city_sales.idxmax()

# Display the result
print(f"City sold the most products: {best_city}")
