from sklearn.metrics import confusion_matrix, f1_score


def evaluate(df, target_column, clf):
    
   # Get X and Y
    y_test = df.loc[:, target_column].values.astype("float32")
    X_test = df.drop(target_column, axis=1).values
    X_test = X_test.astype("float32")

    prediction = clf.predict(X_test)
    f1 = f1_score(y_true=y_test, y_pred=prediction, average='macro')
    cm = confusion_matrix(prediction, y_test)

    return f1, cm