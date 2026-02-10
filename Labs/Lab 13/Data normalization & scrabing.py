import pandas as pd
from sklearn.preprocessing import MinMaxScaler

data = {
    "Marks": [85, 90, 78, 80, 88]
}

df = pd.DataFrame(data)

scaler = MinMaxScaler()

df["Marks_Normalized"] = scaler.fit_transform(df[["Marks"]])

print(df)
