from sklearn.svm import SVC
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)

model = SVC()
model.fit(X, y)

print(model.predict([X[5]]))
