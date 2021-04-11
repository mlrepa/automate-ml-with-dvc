import argparse
from typing import Text

from src.data.dataset import get_dataset
from src.utils.config import load_config


def data_load(config_path: Text) -> None:
    """Load raw data.
    Args:
        config_path {Text}: path to config
    """

    config = load_config(config_path)
    dataset = get_dataset()
    dataset.to_csv(config.data_load.dataset_csv, index=False)
    print(f'Data saved to: {config.data_load.dataset_csv}')


if __name__ == '__main__':

    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--config', dest='config', required=True)
    args = args_parser.parse_args()

    data_load(config_path=args.config)
