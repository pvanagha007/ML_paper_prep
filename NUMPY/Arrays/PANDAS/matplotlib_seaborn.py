import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------
# Load dataset
# -----------------------
df = pd.read_csv("iris.csv")

print(df.head())   # shows data so you know it loaded

# Set style
sns.set_style('whitegrid')

# -----------------------
# 1. Bar Plot (Species count)
# -----------------------
df['species'].value_counts().plot(kind='bar')
plt.title('Count of Each Iris Species')
plt.xlabel('Species')
plt.ylabel('Count')
plt.show()

# -----------------------
# 2. Histogram (Sepal Length)
# -----------------------
df['sepal_length'].hist(bins=20)
plt.title('Sepal Length Distribution')
plt.xlabel('Sepal Length')
plt.ylabel('Frequency')
plt.show()

# -----------------------
# 3. Box Plot (Petal Length by Species)
# -----------------------
df.boxplot(column='petal_length', by='species')
plt.title('Petal Length by Species')
plt.suptitle("")  # removes extra automatic title
plt.xlabel('Species')
plt.ylabel('Petal Length')
plt.show()