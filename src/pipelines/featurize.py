import argparse
import pandas as pd
from typing import Text

from src.features.features import extract_features
from src.utils.config import load_config


def featurize(config_path: Text) -> None:
    """Create new features.
    Args:
        config_path {Text}: path to config
    """

    config = load_config(config_path)

    dataset = pd.read_csv(config.data_load.dataset_csv)
    featured_dataset = extract_features(dataset)

    features_path = config.featurize.features_path
    featured_dataset.to_csv(features_path, index=False)


if __name__ == '__main__':

    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--config', dest='config', required=True)
    args = args_parser.parse_args()

    featurize(config_path=args.config)
