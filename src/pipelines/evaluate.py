
import argparse
import joblib
import json
import os
import yaml

from src.data.dataset import get_dataset
from src.evaluate.evaluate import evaluate


if __name__ == '__main__':

    # add arguments
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--config', dest='config', required=True)
    args = args_parser.parse_args()

    config = yaml.load(open(args.config), Loader=yaml.FullLoader)

    dataset = get_dataset(config['dataset_csv'])

    features_columns_range = config['features_columns_range']
    target_column = config['target_column']

    model_name, models_folder = config['model_name'], config['models_folder']

    model = joblib.load(os.path.join(models_folder, model_name))

    f1, cm = evaluate(
        df=dataset,
        features_columns_range=['sepal_length', 'petal_length_to_petal_width'],
        target_column='species',
        clf=model
    )

    json.dump(
        obj={
            'f1_score': f1,
            'confusion_matrix': cm.tolist()
        },
        fp=open(
            os.path.join(config['reports_folder'], config['metrics_file']),
            'w'
        ),
        indent=4
    )