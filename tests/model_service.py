import gdown
import os
from keras.models import load_model
from lib_ml.process_data import DataProcessor


class ModelService:

    def __init__(self):
        self.model = self.get_model()
        self.processor = DataProcessor(
            tokenizer_url="https://drive.google.com/drive/u/0/folders/1Z0bbPcIegbLHjJcZ90CqzVPmCBLlYEkj"
        )

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
