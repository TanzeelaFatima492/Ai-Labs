from sklearn.datasets import load_iris

data = load_iris()

print("Features:\n", data.data[:5])
print("Target:\n", data.target[:5])
print("Feature Names:", data.feature_names)
