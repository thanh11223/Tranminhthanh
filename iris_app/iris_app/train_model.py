from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.neighbors import KNeighborsClassifier
import pickle

def train_and_save(model_path="model.pkl", n_neighbors=3):
    iris = load_iris()
    X, y = iris.data, iris.target

    # Pipeline: Imputer (điền thiếu) + KNN
    pipe = Pipeline([
        ("imputer", SimpleImputer(strategy="mean")),
        ("knn", KNeighborsClassifier(n_neighbors=n_neighbors))
    ])
    pipe.fit(X, y)

    with open(model_path, "wb") as f:
        pickle.dump(pipe, f)
    print(f"Saved model to {model_path}")

if __name__ == "__main__":
    train_and_save()
