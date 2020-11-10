import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier

ferns = pd.read_csv("D:/Data/HoltResearchForest_FernObservations.csv")

ferns = ferns[ferns.PROFILE != "N"]

X = ferns.drop(columns="SP", axis=1)
y = ferns["SP"]

print(X.dtypes)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, train_size=0.7, random_state=1
)

rfc = RandomForestClassifier(n_estimators=1000, max_depth=5, random_state=1).fit(X, y)

train_score = rfc.score(X_train, y_train)
test_score = rfc.score(X_test, y_test)

print("Train score:", train_score)
print("Test score:", test_score)
