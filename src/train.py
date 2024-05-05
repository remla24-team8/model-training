from model import create_model
import numpy as np
import json


# Load or define necessary variables
#parameters load
with open('params.json', 'r') as json_file:
    params = json.load(json_file)


char_index = params['char_index']
num_categories = len(params['categories'])
embedding_dimension = params['embedding_dimension']

# Load the data from CSV files
x_train = np.loadtxt('csv_files/x_train.csv', delimiter=",")
x_val = np.loadtxt('csv_files/x_val.csv', delimiter=",")
x_test = np.loadtxt('csv_files/x_test.csv', delimiter=",")

y_train = np.loadtxt('csv_files/y_train.csv', delimiter=",")
y_val = np.loadtxt('csv_files/y_val.csv', delimiter=",")
y_test = np.loadtxt('csv_files/y_test.csv', delimiter=",")

#Clipping of the vocab size, something wrong with tokenizer
vocab_size = len(char_index.keys())
x_train = np.clip(x_train, 0, vocab_size - 1)
x_val = np.clip(x_val, 0, vocab_size - 1)
x_test = np.clip(x_test, 0, vocab_size - 1)


# Create the model
model = create_model(char_index, num_categories, embedding_dimension)
#training of the model
model.compile(loss=params['loss_function'], optimizer=params['optimizer'])


hist = model.fit(x_train, y_train,
                batch_size=params['batch_train'],
                epochs=params['epoch'],
                shuffle=True,
                validation_data=(x_val, y_val)
                )

# Save the entire model to a HDF5 file.
model.save('phishing_model.h5')  # legacy HDF5 format

