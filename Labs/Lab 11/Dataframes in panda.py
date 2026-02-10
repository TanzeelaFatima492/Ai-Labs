import pandas as pd
import numpy as np

data = {
    "Name": ["Ali", "Sara", "Ahmed", "Fatima", "Usman"],
    "Age": [22, 25, np.nan, 23, 24],
    "Marks": [85, 90, 78, np.nan, 88],
    "City": ["Lahore", "Karachi", "Lahore", "Islamabad", "Karachi"]
}

df = pd.DataFrame(data)

print(df)
print("\nFirst 3 rows:\n", df.head(3))
print("\nColumns:\n", df.columns)
