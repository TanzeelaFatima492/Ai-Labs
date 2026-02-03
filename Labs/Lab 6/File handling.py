with open("data.txt", "w") as f: f.write("Line1\nLine2")
with open("data.txt") as f: print(f.read())

import csv
with open("data.csv", "w", newline='') as f:
    writer = csv.writer(f); writer.writerow(["Name", "Age"]); writer.writerow(["Ali", 22])
with open("data.csv") as f: print(list(csv.reader(f)))