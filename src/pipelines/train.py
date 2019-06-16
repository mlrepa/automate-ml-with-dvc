import argparse
import joblib
import os
import yaml

from src.data.dataset import get_dataset
from src.train.train import train


if __name__ == '__main__':

    # add arguments
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--config', dest='config', required=True)
    args = args_parser.parse_args()

    config = yaml.load(open(args.config), Loader=yaml.FullLoader)

    estimator_name = config['estimator_name']
    grid_search_cv_config = config['grid_search_cv_config']

    features_columns_range = config['features_columns_range']
    target_column = config['target_column']

    train_df = get_dataset(config['train_csv'])

    model = model = train(
        df=train_df,
        features_columns_range=features_columns_range,
        target_column=target_column,
        estimator_name=estimator_name,
        grid_search_cv_config=grid_search_cv_config
    )

    model_name, models_folder = config['model_name'], config['models_folder']

    joblib.dump(
        model,
        os.path.join(models_folder, model_name)
    )