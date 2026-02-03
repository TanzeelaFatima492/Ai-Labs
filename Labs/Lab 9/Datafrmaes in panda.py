import pandas as pd
df = pd.DataFrame({"Name": ["Ali", "Sara", "John"], "Score": [75, 85, 92]})
print(df[df["Score"] > 80])
