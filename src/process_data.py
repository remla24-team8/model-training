import pandas as pd
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder
import json

# Load data from CSV files
train_data = pd.read_csv('csv_files/train_data.csv')
val_data = pd.read_csv('csv_files/val_data.csv')
test_data = pd.read_csv('csv_files/test_data.csv')

#Tokenize the dataset
tokenizer = Tokenizer(char_level=True,lower=True, oov_token = '-n-') #
tokenizer.fit_on_texts(train_data['text'].tolist() + val_data['text'].tolist() + test_data['text'].tolist())


char_index = tokenizer.word_index
sequence_length=200

x_train = pad_sequences(tokenizer.texts_to_sequences(train_data['text']), maxlen=sequence_length)
x_val = pad_sequences(tokenizer.texts_to_sequences(val_data['text']), maxlen=sequence_length)
x_test = pad_sequences(tokenizer.texts_to_sequences(test_data['text']), maxlen=sequence_length)

# Encoding labels
encoder = LabelEncoder()
y_train = encoder.fit_transform(train_data['label'])
y_val = encoder.transform(val_data['label'])
y_test = encoder.transform(test_data['label'])

#Parameters
params = {'loss_function': 'binary_crossentropy',
                       'optimizer': 'adam',
                       'sequence_length': 200,
                       'batch_train': 500,
                       'batch_test': 250,
                       'categories': ['phishing', 'legitimate'],
                       'char_index': char_index,
                       'epoch': 30,
                       'embedding_dimension': 50,
                       'dataset_dir': "../dataset/small_dataset/",
                       "metrics": ["accuracy"]}


# Save processed data
pd.DataFrame(x_train).to_csv('csv_files/x_train.csv', index=False)
pd.DataFrame(x_val).to_csv('csv_files/x_val.csv', index=False)
pd.DataFrame(x_test).to_csv('csv_files/x_test.csv', index=False)

pd.DataFrame(y_train, dtype=int).to_csv('csv_files/y_train.csv', index=False)
pd.DataFrame(y_val, dtype=int).to_csv('csv_files/y_val.csv', index=False)
pd.DataFrame(y_test, dtype=int).to_csv('csv_files/y_test.csv', index=False)


# Save parameters to a JSON file
with open('params.json', 'w+') as json_file:
    json.dump(params, json_file, indent=4)

# print('Max index in x_train:', np.max(x_train))
# print('Min index in x_train:', np.min(x_train))

# print('Max index in x_test:', np.max(x_test))
# print('Min index in x_test:', np.min(x_test))

# print('Max index in x_val:', np.max(x_val))
# print('Min index in x_val:', np.min(x_val))

