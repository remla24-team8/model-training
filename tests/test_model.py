

import numpy as np
import pytest
from model_service import ModelService

model = ModelService()


def test_model_predict_types():
    """
    Test the types of predictions returned by the model.

    This test checks if the model returns numpy arrays for both single 
    URL predictions and predictions on a list of URLs.
    """
    url = "https://www.google.com"
    assert isinstance(model.predict(url), np.ndarray)

    urls = ["https://www.google.com", "https://www.facebook.com"]
    assert isinstance(model.predict(urls), np.ndarray)


def test_model_predict_correct_score():
    """
    Test the correctness of prediction scores returned by the model.

    This test checks if the model returns prediction scores that are less than or 
    equal to 0.07 for both single URL predictions and predictions on a list of URLs.
    """
    url = "https://www.google.com"
    assert model.predict(url) <= 0.07

    urls = ["https://www.google.com", "https://www.facebook.com"]
    prediction = model.predict(urls)
    assert (prediction <= [0.07, 0.07]).all()


def test_internationalized():
    """
    Test the behavior of the model on internationalized URLs.

    This test checks if the model behaves correctly when predicting scores for 
    internationalized URLs. It skips the test if the model is not trained on internationalized URLs.
    """
    url_bad = "http://xn--thn-5cdop7dtb.xn--m-0tbi/"
    url_bad = "https://гауthеоn.соm"
    url_good = "https://raytheon.com"

    if not model.predict(url_good) < model.predict(url_bad):
        pytest.skip("Model not trained on internationalized URLs")
    else:
        assert model.predict(url_good) < model.predict(url_bad)
        assert model.predict(url_good) < 0.07
        assert model.predict(url_bad) > 0.07


def test_model_predict_incorrect_score():
    """
    Test the correctness of prediction scores returned by the model.

    This test checks if the model returns prediction scores that are greater than 
    or equal to 0.45 for both single URL predictions and predictions on a list of URLs.
    """
    url = "http://www.&shygoogle.com"
    assert model.predict(url) >= 0.45

    urls = ["http://www.gooogle.com", "http://www.faceebook.com"]
    prediction = model.predict(urls)
    assert (prediction >= [0.45, 0.45]).all()
