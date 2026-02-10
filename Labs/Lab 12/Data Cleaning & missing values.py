import pandas as pd
import numpy as np

data = {
    "Age": [22, 25, np.nan, 23, 24],
    "Marks": [85, 90, 78, np.nan, 88]
}

df = pd.DataFrame(data)

print("Before Cleaning:\n", df)

print("\nMissing Values:\n", df.isnull().sum())

df["Age"].fillna(df["Age"].mean(), inplace=True)
df["Marks"].fillna(df["Marks"].mean(), inplace=True)

print("\nAfter Cleaning:\n", df)
