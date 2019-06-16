import argparse
import yaml

from src.data.dataset import get_dataset
from src.transforms.trainsforms import transform_targets_to_numerics, split_dataset_in_train_test


def split_dataset():

    # add arguments
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--config', dest='config', required=True)
    args = args_parser.parse_args()

    config = yaml.load(open(args.config), Loader=yaml.FullLoader)

    dataset = get_dataset(config['dataset_csv'])
    test_size = config['test_size']
    random_state = config['random_state']
    train_csv = config['train_csv']
    test_csv = config['test_csv']
    target_column = config['target_column']

    dataset = transform_targets_to_numerics(dataset, target_column=target_column)

    train_dataset, test_dataset = split_dataset_in_train_test(dataset, test_size=test_size, random_state=random_state)

    train_dataset.to_csv(train_csv, index=False)
    test_dataset.to_csv(test_csv, index=False)



if __name__ == '__main__':

    split_dataset()

