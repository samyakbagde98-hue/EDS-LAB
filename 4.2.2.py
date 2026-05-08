import pandas as pd
# Adding a new row
newname=input("New name: ")
newage=int(input("New age: "))
df.loc[len(df)]=[newname,newage]
print("After adding a row:\n",df)
# Modifying a row
index=int(input("Index of row to modify: "))
new_age=int(input("New age: "))
df.at[index,"Age"]=new_age

# Display the DataFrame after modifying a row
print("After modifying a row:")
print(df)
# Deleting a row
row=int(input("Index of row to delete: "))
df.drop(row,inplace=True)
df.reset_index(drop=True,inplace=True)
# Display the DataFrame after deleting a row
print("After deleting a row:")
print(df)


# Adding a new column
gender=input("Enter genders separated by space: ").split()
#if len(gender)==len(df):
df["Gender"]=gender

# Display the DataFrame after adding a new column
print("After adding a new column:")
print(df)
# Modifying a column
df["Name"]=df["Name"].astype(str).str.upper()
# Display the DataFrame after modifying a column
print("After modifying a column:")
print(df)
# Deleting a column
df=df.drop(columns=["Age"])
# Display the DataFrame after deleting a column
print("After deleting a column:")
print(df)
