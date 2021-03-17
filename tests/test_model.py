import joblib
import os
import numpy as np
import pytest


@pytest.fixture(scope='module')
def model():

    model_path = os.getenv('MODEL_PATH')
    model = joblib.load(model_path)

    return model


def test_model(model):

    data = [
        {
            'sepal_length': 4.9,
            'sepal_width': 3.0,
            'petal_length': 1.7,
            'petal_width': 0.2,
            'sepal_length_to_sepal_width': 1.63333333,
            'petal_length_to_petal_width': 8.5
        }
    ]
    values = [list(d.values()) for d in data]
    np_array = np.array(values)
    result = model.predict(np_array)

    assert len(result) == 1

    for v in result:
        assert v in [0, 1, 2]
