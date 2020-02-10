import pandas as pd
from typing import Text


def get_dataset(dataset_path: Text) -> pd.DataFrame:
    """Read dataset into pandas.DataFrame
    Args:
        dataset_path {Text}: dataset path
    Returns:
        pandas.DataFrame
    """

    return pd.read_csv(dataset_path)