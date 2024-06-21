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
        """
        Load the model from the local file system or download it if necessary.

        Returns:
            The loaded model.
        """
        if os.path.exists("models/model.h5"):
            model = load_model("models/model.h5", compile=True)
            return model
        
        os.system("python -m dvc get \
                  https://github.com/remla24-team8/model-training models/")

        model = load_model("models/model.h5", compile=True)
        return model