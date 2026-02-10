import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Age": [22, 25, 21, 23, 24],
    "Marks": [85, 90, 78, 80, 88]
}

df = pd.DataFrame(data)

print("Statistics:\n", df.describe())

print("\nCorrelation:\n", df.corr())

plt.figure()
sns.heatmap(df.corr(), annot=True)
plt.title("Correlation Heatmap")
plt.show()
