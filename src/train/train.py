
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC


class UnsupportedClassifier(Exception):

    def __init__(self, estimator_name):

        self.msg = f'Unsupported estimator {estimator_name}'
        super().__init__(self.msg)


def get_supported_estimator():

    return {
        'logreg': LogisticRegression,
        'svm': SVC,
        'knn': KNeighborsClassifier
    }


def train(df, features_columns_range, target_column, estimator_name, grid_search_cv_config):

    estimators = get_supported_estimator()

    if estimator_name not in estimators.keys():

        raise UnsupportedClassifier(estimator_name)

    estimator = estimators[estimator_name]()
    clf = GridSearchCV(estimator=estimator, **grid_search_cv_config)

    Xtrain, Ytrain = df.loc[:, features_columns_range[0]:features_columns_range[1]].values, df.loc[:, target_column].values
    Xtrain = Xtrain.astype("float32")

    clf.fit(Xtrain, Ytrain)

    return clf