import gdown
import os
from keras.models import load_model
from lib_ml.process_data import DataProcessor
import numpy as np


class ModelService:
    
    def __init__(self):
        self.model = self.get_model()
        self.processor = DataProcessor(tokenizer_url='https://drive.google.com/drive/u/0/folders/1Z0bbPcIegbLHjJcZ90CqzVPmCBLlYEkj')
    
    def predict(self, url):
        """
        Make a prediction using the stored model and a given url as input
        """
        if isinstance(url, list):
            data = url
        else:
            data = [url]
        preprocess_url = self.processor.tokenize_pad_data(data)
        prediction = self.model.predict(preprocess_url, verbose=0).flatten()
        
        return prediction

    @staticmethod    
    def get_model():
        if os.path.exists("models/model.h5"):
            model = load_model("models/model.h5", compile=True)
            return model
        
        if not os.path.exists("models/"):
            os.makedirs("models/")
        
        gdrive_url = "https://drive.google.com/drive/u/0/folders/1ITlzN-9Qe7ZnNRGWkq-YHrjt9xYG3e_-"
        model_out = "./"
        gdown.download_folder(gdrive_url, output=model_out)
        model = load_model("models/model.h5", compile=True)
        return model

model = ModelService()

def test_model_predict_types():
    # Test the model with a single URL
    url = "https://www.google.com"
    assert isinstance(model.predict(url), np.ndarray)

    # Test the model with a list of URLs
    urls = ["https://www.google.com", "https://www.facebook.com"]
    assert isinstance(model.predict(urls), np.ndarray)


def test_model_predict_correct_score():
    # Test the model with a single URL
    url = "https://www.google.com"
    assert model.predict(url) <= 0.07

    # Test the model with a list of URLs
    urls = ["https://www.google.com", "https://www.facebook.com"]
    prediction = model.predict(urls)
    assert (prediction <= [0.07, 0.07]).all()



# This test is not working because the model is not trained on internationalized urls
def test_internationalized():
    url_bad = "http://xn--thn-5cdop7dtb.xn--m-0tbi/"
    url_good = "http://raytheon.com"

    assert model.predict(url_good) < model.predict(url_bad)
    assert model.predict(url_good) < 0.07
    assert model.predict(url_bad) > 0.07


def test_model_predict_incorrect_score():
    # Test the model with a single URL
    url = "http://www.&shygoogle.com"
    assert model.predict(url) >= 0.45

    # Test the model with a list of URLs
    urls = ["http://www.gooogle.com", "http://www.faceebook.com"]
    prediction = model.predict(urls)
    assert (prediction >= [0.45, 0.45]).all()
