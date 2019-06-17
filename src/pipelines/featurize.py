import argparse
import yaml

from src.data.dataset import get_dataset
from src.features.features import extract_features


if __name__ == '__main__':

    # add arguments
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--config', dest='config', required=True)
    args = args_parser.parse_args()

    config = yaml.load(open(args.config), Loader=yaml.FullLoader)

    dataset = get_dataset(config['dataset_csv'])
    featured_dataset_csv = config['featured_dataset_csv']

    featured_dataset = extract_features(dataset)
    featured_dataset.to_csv(featured_dataset_csv, index=False)

