

def create_new_features(df):

    dataset = df.copy()

    dataset['sepal_length_to_sepal_width'] = dataset['sepal_length'] / dataset['sepal_width']
    dataset['petal_length_to_petal_width'] = dataset['petal_length'] / dataset['petal_width']

    dataset['sepal_length_in_square'] = dataset['sepal_length'] ** 2
    dataset['sepal_width_in_square'] = dataset['sepal_width'] ** 2
    dataset['petal_length_in_square'] = dataset['petal_length'] ** 2
    dataset['petal_width_in_square'] = dataset['petal_width'] ** 2

    dataset['sepal_length_in_cube'] = dataset['sepal_length'] ** 3
    dataset['sepal_width_in_cube'] = dataset['sepal_width'] ** 3
    dataset['petal_length_in_cube'] = dataset['petal_length'] ** 3
    dataset['petal_width_in_cube'] = dataset['petal_width'] ** 3

    dataset = dataset[[
        'sepal_length', 'sepal_width', 'petal_length', 'petal_width',
        'sepal_length_in_square', 'sepal_width_in_square', 'petal_length_in_square', 'petal_width_in_square',
        'sepal_length_in_cube', 'sepal_width_in_cube', 'petal_length_in_cube', 'petal_width_in_cube',
        'sepal_length_to_sepal_width', 'petal_length_to_petal_width',
        'species'
    ]]

    return dataset