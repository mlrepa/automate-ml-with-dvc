import pandas as pd
from sklearn.preprocessing import LabelEncoder
from typing import Text


def transform_target_values_to_labels(df: pd.DataFrame, target_column: Text) -> pd.DataFrame:
    """Convert target column values to labels.
    Args:
        df {pandas.DataFrame}: dataset
        target_column {Text}: target column name
    Returns:
        pandas.DataFrame: update dataframe
    """
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from typing import Text, Tuple


def transform_targets_to_numerics(df: pd.DataFrame, target_column: Text) -> pd.DataFrame:

    dataset = df.copy()
    le = LabelEncoder()
    dataset[target_column] = le.fit_transform(dataset[target_column])

    return dataset


def split_dataset_in_train_test(df: pd.DataFrame, test_size: float, random_state: int = 42) \
        -> Tuple[pd.DataFrame, pd.DataFrame]:

    dataset = df.copy()
    train_dataset, test_dataset = train_test_split(dataset, test_size=test_size, random_state=random_state)

    return train_dataset, test_dataset
