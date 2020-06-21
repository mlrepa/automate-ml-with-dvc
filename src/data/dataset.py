from typing import List

import pandas as pd
from sklearn.datasets import load_iris


def get_dataset() -> pd.DataFrame:
    """Read dataset into pandas.DataFrame

    Returns:
        pandas.DataFrame
    """

    data = load_iris(as_frame=True)

    dataset = data.frame
    dataset.columns = [colname.strip(' (cm)').replace(' ', '_') for colname in dataset.columns.tolist()]

    return dataset

def get_target_names() -> List:
    return load_iris(as_frame=True).target_names.tolist()