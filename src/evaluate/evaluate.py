from sklearn.metrics import confusion_matrix, f1_score


def evaluate(df, features_columns_range, target_column, clf):
    
    Xtest, Ytest = df.loc[:, features_columns_range[0]:features_columns_range[1]].values, df.loc[:,target_column].values
    Xtest = Xtest.astype("float32")

    prediction = clf.predict(Xtest)
    f1 = f1_score(y_true=Ytest, y_pred=prediction, average='macro')
    cm = confusion_matrix(prediction, Ytest)

    return f1, cm