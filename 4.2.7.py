import pandas as pd
data['IsAlone'] = np.where(data['FamilySize'] > 0, 0, 1)
data = pd.get_dummies(data, columns=['Embarked'], drop_first=True)

print(data.groupby('Pclass') ['Survived'].mean())

#2. Calculate the survival rate by embarked location (Embarked_S)

print(data.groupby('Embarked_S') ['Survived'].mean())

#3. Calculate the survival rate by family size

print(data.groupby('FamilySize') ['Survived'].mean())

#4. Calculate the survival rate by being alone

print(data.groupby('IsAlone') ['Survived'].mean())

#5. Get the average fare by class

print(data.groupby('Pclass') ['Fare'].mean())

#6. Get the average age by class

print(data.groupby('Pclass') ['Age'].mean())

#7. Get the average age by survival status

print(data.groupby('Survived') ['Age'].mean())

#8. Get the average fare by survival status

print(data.groupby('Survived') ['Fare'].mean())

#9. Get the number of survivors by class (sort by values descending)

print(data[data['Survived'] == 1] ['Pclass'].value_counts())

#10. Get the number of non-survivors by class (sort by values descending)

print(data[data['Survived'] == 0] ['Pclass'].value_counts())
