import pandas as pd
axes[0, 0].bar(df['Pclass'].value_counts().index, df['Pclass'].value_counts(), color='skyblue')

axes[0, 0].set_title("Passenger Class Distribution")
axes [0, 0].set_xlabel("Pclass")
axes[0, 0].set_ylabel("Count")
#Plot 2: Gender distribution

axes[0, 1].pie(df['Gender'].value_counts(), labels=df['Gender'].value_counts().index, autopct='%1.1f%%', colors=['lightblue', 'lightcoral'])
axes[0, 1].set_title("Gender Distribution")

#Plot 3: Age distribution

axes[1, 0].hist(df['Age'].dropna(), bins=8, color='lightgreen', edgecolor='black')

axes[1, 0].set_title("Age Distribution")

axes[1, 0].set_xlabel("Age")

axes[1, 0].set_ylabel("Frequency")

axes[1, 1].bar(df['Survived'].value_counts().index, df['Survived'].value_counts(), color=['lightblue', 'lightcoral'])

axes[1, 1].set_title("Survival Count")

axes[1, 1].set_xlabel("Survived (0= No, 1 = Yes)")

axes[1, 1].set_ylabel("Count")

#Plot 5: Fare vs Age

axes[2, 0].scatter(df ['Age'], df['Fare'], color='orange')

axes[2, 0].set_title("Fare vs Age")

axes[2, 0].set_xlabel("Age")

axes[2, 0].set_ylabel("Fare")

plt.tight_layout()
plt.show()
