import joblib
import os
import numpy as np


def test(model):

    data = [[1, 2, 3, 4, 5, 6]]
    np_array = np.array(data)
    result = model.predict(np_array)
    print(result)

    assert len(result) == 1
    assert result < 3


if __name__ == '__main__':

    model_path = os.getenv('MODEL_PATH')
    model = joblib.load(model_path)
    test(model)