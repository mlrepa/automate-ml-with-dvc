import argparse
import pandas as pd
from sklearn.model_selection import train_test_split
from typing import Text
import yaml


def data_split(config_path: Text) -> None:
    """Split dataset into train/test.
    Args:
        config_path {Text}: path to config
    """

    config = yaml.safe_load(open(config_path))

    dataset = pd.read_csv(config['featurize']['features_path'])
    train_dataset, test_dataset = train_test_split(
        dataset,
        test_size = config['data_split']['test_size'],
        random_state = config['base']['random_state']
    )

    train_csv_path = config['data_split']['train_path']
    test_csv_path = config['data_split']['test_path']
    train_dataset.to_csv(train_csv_path, index=False)
    test_dataset.to_csv(test_csv_path, index=False)


if __name__ == '__main__':

    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--config', dest='config', required=True)
    args = args_parser.parse_args()

    data_split(config_path=args.config)

