from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = load_wine(as_frame=True)

X = data['data']
y = data['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

clf = RandomForestClassifier()

clf.fit(X_train, y_train)

y_prediction_test = clf.predict(X_test)

print('Random Forrest Classifier for "Wine dataset"')
print('Accuracy on test set.')
print('Accuracy:', accuracy_score(y_test, y_prediction_test))
