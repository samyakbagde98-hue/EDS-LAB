import pandas as pd

print(data[data['Survived'] == 0] ['Sex'].value_counts())

#3. Number of survivors by embarkation location 'S'

print(data[data['Survived'] == 1] ['Embarked_S'].value_counts())

#4. Number of non-survivors by embarkation location 'S'

print(data[data['Survived'] == 0] ['Embarked_S'].value_counts())

#5. Percentage of children (Age < 18) who survived

children = data[data['Age'] < 18] 
print(children['Survived'].mean())

# 6. Percentage of adults (Age >= 18) who survived

adults = data[data['Age'] >= 18] 
print(adults['Survived'].mean())

#7. Median age of survivors print(data[data['Survived'] == 1] ['Age'].median())
print(data[data['Survived'] == 1] ['Age'].median())
#8. Median age of non-survivors print(data[data['Survived'] == 0] ['Age'].median())
print(data[data['Survived'] == 0] ['Age'].median())
# 9. Median fare of survivors

print(data[data['Survived'] == 1] ['Fare'].median())

#10. Median fare of non-survivors

print(data[data['Survived'] == 0] ['Fare'].median())
