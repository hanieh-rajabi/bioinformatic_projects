import numpy as np
from sklearn.model_selection import train_test_split, StratifiedKFold
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from kmer_tool.data_processing import load_promoter_data, encode_labels
from kmer_tool.kmer import create_feature_matrix



sequences, labels = load_promoter_data("data/promoters_data")

X = create_feature_matrix(sequences, 3)
y = encode_labels(labels)

X = np.array(X)
y = np.array(y)


cv = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

scores = []

for train_index, test_index in cv.split(X, y):

    X_train = X[train_index]
    X_test = X[test_index]

    y_train = y[train_index]
    y_test = y[test_index]

    model = MLPClassifier(
        hidden_layer_sizes=(16,),
        activation="relu",
        max_iter=3000,
        random_state=42
    )

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)

    scores.append(accuracy)


print("Cross-validation scores:", scores)
print("Mean accuracy:", np.mean(scores))
