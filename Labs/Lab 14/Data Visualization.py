import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Name": ["Ali", "Sara", "Ahmed", "Fatima", "Usman"],
    "Marks": [85, 90, 78, 80, 88]
}

df = pd.DataFrame(data)

plt.figure()
plt.hist(df["Marks"])
plt.title("Marks Distribution")
plt.show()

plt.figure()
sns.barplot(x="Name", y="Marks", data=df)
plt.title("Marks by Student")
plt.show()
