"""
This script is used to train the model using the processed data.
"""

import json
import os
from joblib import dump, load
from model import create_model
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive



# Load or define necessary variables
# parameters load


char_index = load("output/char_index.joblib")

# Load the data from CSV files
x_train = load("output/x_train.joblib")
x_val = load("output/x_val.joblib")
x_test = load("output/x_test.joblib")

y_train = load("output/y_train.joblib")
y_val = load("output/y_val.joblib")
y_test = load("output/y_test.joblib")

# Clipping of the vocab size, something wrong with tokenizer
vocab_size = len(char_index.keys())
# x_train = np.clip(x_train, 0, vocab_size - 1)
# x_val = np.clip(x_val, 0, vocab_size - 1)
# x_test = np.clip(x_test, 0, vocab_size - 1)


# Create the model and return model parameters
model, params = create_model(char_index)
# training of the model
model.compile(
    loss=params["loss_function"],
    optimizer=params["optimizer"],
    metrics=params["metrics"],
)


hist = model.fit(
    x_train,
    y_train,
    batch_size=params["batch_train"],
    epochs=params["epoch"],
    shuffle=True,
    validation_data=(x_val, y_val),
)

scores = model.evaluate(x_test, y_test, batch_size=params["batch_test"])

metrics = dict(zip(["loss", "accuracy"], scores))

with open("output/metrics.json", "w+", encoding='UTF-8') as json_file:
    json.dump(metrics, json_file, indent=4)

# Save the model
model.save("models/model.h5")
# Upload the model file to Google Drive using authenticator flow

client_json_path = os.path.join(os.path.dirname(__file__), 'client_secrets.json')
GoogleAuth.DEFAULT_SETTINGS['client_config_file'] = client_json_path

# Authenticate with Google Drive
gauth = GoogleAuth()
gauth.LocalWebserverAuth()

# Create GoogleDrive instance
drive = GoogleDrive(gauth)

# Upload the model file
file = drive.CreateFile({'id': '174hfdMaKE_J0OLdvfGIxxJM_7KJyiqaJ'})
file.SetContentFile("models/model.h5")
file.Upload()


