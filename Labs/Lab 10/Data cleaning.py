import pandas as pd
import numpy as np
df = pd.DataFrame({"A": [1, 2, np.nan, 2], "B": [4, 4, 6, 6]})
df.fillna(df.mean(), inplace=True)
df.drop_duplicates(inplace=True)
print(df)
print("Mean of column A:", df["A"].mean())