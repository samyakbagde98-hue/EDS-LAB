import pandas as pd

import pandas as pd
import numpy as np

# Load the Titanic dataset
data = pd.read_csv('Titanic-Dataset.csv')  # Change filename if necessary

# 0. Create 'FamilySize'
data['FamilySize'] = data['SibSp'] + data['Parch']

# 1. Create a new column 'IsAlone'
data['IsAlone'] = np.where(data['FamilySize'] == 0, 1, 0)
data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})

# 3. One-hot encode 'Embarked' column, drop first
data = pd.get_dummies(data, columns=['Embarked'], drop_first=True)

# 4. Get the mean age of passengers
mean_age = data['Age'].mean()
print(mean_age)

# 5. Get the median fare of passengers
median_fare = data['Fare'].median()
print(median_fare)
passengers_by_class = data['Pclass'].value_counts()
print(passengers_by_class)

# 7. Get number of passengers by gender
passengers_by_gender = data['Sex'].value_counts()
print(passengers_by_gender)

# 8. Get number of passengers by survival status
passengers_by_survival = data['Survived'].value_counts()
print(passengers_by_survival)

# 9. Calculate the overall survival rate
survival_rate = data['Survived'].mean()
print(survival_rate)

# 10. Calculate the survival rate by gender
survival_rate_by_gender = data.groupby('Sex')['Survived'].mean()
print(survival_rate_by_gender)
