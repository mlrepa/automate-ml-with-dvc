
import argparse
import yaml


def split_common_config():

    """
    Split common config into configs for steps
    """

    # add arguments
    args_parser = argparse.ArgumentParser()

    args_parser.add_argument('--config', dest='config', required=True)

    args = args_parser.parse_args()

    # read config and get config sections

    config = yaml.load(open(args.config), Loader=yaml.FullLoader)

    dataset_config = config['dataset']
    model_config = config['model']
    train_config = config['train']
    evaluate_config = config['evaluate']
    report_config = config['report']
    split_config = config['split_config']

    # create split train/test config
    split_train_test_config = dict(
        random_state=dataset_config['random_state'],
        dataset_csv=dataset_config['featured_dataset_csv'],
        train_csv=dataset_config['train_csv'],
        test_csv=dataset_config['test_csv'],
        target_column=dataset_config['target_column'],
        test_size=dataset_config['test_size']
    )

    with open('{}/{}'.format(split_config['folder'], 'split_train_test_config.yml'), 'w')\
            as split_train_test_yml:
        yaml.dump(
            data=split_train_test_config,
            stream=split_train_test_yml,
            default_flow_style=False
        )

    featurize_config = dict(
        dataset_csv=dataset_config['dataset_csv'],
        featured_dataset_csv=dataset_config['featured_dataset_csv']
    )

    with open('{}/{}'.format(split_config['folder'], 'featurize_config.yml'), 'w')  as featurize_yml:
        yaml.dump(
            data=featurize_config,
            stream=featurize_yml,
            default_flow_style=False
        )

    # train model config
    train_clf_config = dict(
        estimator_name=train_config['estimator_name'],
        grid_search_cv_config=train_config['grid_search_cv_config'],
        features_columns_range=dataset_config['features_columns_range'],
        target_column=dataset_config['target_column'],
        train_csv=dataset_config['train_csv'],
        model_name=model_config['model_name'],
        models_folder=model_config['models_folder']
    )

    with open('{}/{}'.format(split_config['folder'], 'train_clf_config.yml'), 'w') as train_clf_yml:
        yaml.dump(
            data=train_clf_config,
            stream=train_clf_yml,
            default_flow_style=False
        )

    # evaluate model config
    evaluate_model_config = dict(
        dataset_csv=dataset_config['test_csv'],
        features_columns_range=dataset_config['features_columns_range'],
        target_column=dataset_config['target_column'],
        model_name=model_config['model_name'],
        models_folder=model_config['models_folder'],
        reports_folder=report_config['reports_folder'],
        metrics_file=evaluate_config['metrics_file']
    )

    with open('{}/{}'.format(split_config['folder'], 'evaluate_model_config.yml'), 'w') as evaluate_model_yml:
        yaml.dump(
            data=evaluate_model_config,
            stream=evaluate_model_yml,
            default_flow_style=False
        )


if __name__ == '__main__':

    split_common_config()
