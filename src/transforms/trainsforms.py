
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


def transform_targets_to_numerics(df, target_column):

    dataset = df.copy()
    le = LabelEncoder()

    dataset[target_column] = le.fit_transform(dataset[target_column])

    return dataset


def split_dataset_in_train_test(df, test_size, random_state=42):

    dataset = df.copy()
    train_dataset, test_dataset = train_test_split(dataset, test_size=test_size, random_state=random_state)

    return train_dataset, test_dataset
