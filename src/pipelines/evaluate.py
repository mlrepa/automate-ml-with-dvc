import argparse
import joblib
import json
import os
from typing import Text
import yaml

from src.data.dataset import get_dataset
from src.evaluate.evaluate import evaluate


def evaluate_model(config_path: Text, base_config_path: Text) -> None:
    """Evaluate model.
    Args:
        config_path {Text}: path to config
        base_config_path {Text}: path to base config
    """

    config = yaml.safe_load(open(config_path))
    base_config = yaml.safe_load(open(base_config_path))

    target_column = base_config['featurize']['target_column']
    models_folder = base_config['base']['model']['models_folder']
    model_name = base_config['base']['model']['model_name']

    test_df = get_dataset(base_config['split_train_test']['test_csv'])
    model = joblib.load(os.path.join(models_folder, model_name))
    f1, cm = evaluate(df=test_df,
                      target_column=target_column,
                      clf=model)
    test_report = {
        'f1_score': f1,
        'confusion_matrix': cm.tolist()
    }
    print(test_report)
    filepath = os.path.join(base_config['base']['experiments']['experiments_folder'],
                            config['metrics_file'])
    json.dump(obj=test_report, fp=open(filepath, 'w'), indent=2)


if __name__ == '__main__':

    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--config', dest='config', required=True)
    args_parser.add_argument('--base_config', dest='base_config', required=True)
    args = args_parser.parse_args()

    evaluate_model(config_path=args.config, base_config_path=args.base_config)
