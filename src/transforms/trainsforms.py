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

    dataset = df.copy()
    le = LabelEncoder()
    dataset[target_column] = le.fit_transform(dataset[target_column])

    return dataset
