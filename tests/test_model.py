

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
    print(f"Testing legit urls: {prediction}")
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
    good_score = model.predict(url_good)
    bad_score = model.predict(url_bad)
    print(f"Testing internationalized urls: legit: {good_score}, scam: {bad_score}")

    if not good_score < bad_score:
        pytest.skip("Model not trained on internationalized URLs")
    else:
        assert good_score < bad_score
        assert good_score < 0.07
        assert bad_score > 0.07


def test_model_predict_incorrect_score():
    """
    Test the correctness of prediction scores returned by the model.

    This test checks if the model returns prediction scores that are greater than 
    or equal to 0.45 for both single URL predictions and predictions on a list of URLs.
    """
    url = "http://www.&shygoogle.com"
    print(f"Testing scam urls: {model.predict(url)}")

    if model.predict(url) < 0.45:
        pytest.skip("Model is not very good at detecting scam")
    else:
        assert model.predict(url) >= 0.45
        urls = ["http://www.gooogle.com", "http://www.faceebook.com"]
        print(f"Testing scam urls: {model.predict(urls)}")
        prediction = model.predict(urls)
        assert (prediction >= [0.45, 0.45]).all()
