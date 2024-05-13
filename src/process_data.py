import pandas as pd
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder
import json
from joblib import dump,load

def main():
    # Load data from CSV files
    raw_x_train = load("output/raw_x_train.joblib")
    raw_y_train = load("output/raw_y_train.joblib")

    raw_x_test = load("output/raw_x_test.joblib")
    raw_y_test = load("output/raw_y_test.joblib")

    raw_x_val = load("output/raw_x_val.joblib")
    raw_y_val = load("output/raw_y_val.joblib")

    #Tokenize the dataset
    tokenizer = Tokenizer(char_level=True,lower=True, oov_token = '-n-') #
    tokenizer.fit_on_texts(raw_x_train.tolist() + raw_x_test.tolist() + raw_x_val.tolist())


    char_index = tokenizer.word_index
    dump(char_index, 'output/char_index.joblib')
    sequence_length=200

    x_train = pad_sequences(tokenizer.texts_to_sequences(raw_x_train), maxlen=sequence_length)
    x_val = pad_sequences(tokenizer.texts_to_sequences(raw_x_val), maxlen=sequence_length)
    x_test = pad_sequences(tokenizer.texts_to_sequences(raw_x_test), maxlen=sequence_length)

    # Encoding labels
    encoder = LabelEncoder()
    y_train = encoder.fit_transform(raw_y_train)
    y_val = encoder.transform(raw_y_val)
    y_test = encoder.transform(raw_y_test)


    # Save processed data
    dump(x_train, 'output/x_train.joblib')
    dump(x_val, 'output/x_val.joblib')
    dump(x_test, 'output/x_test.joblib')

    dump(y_train, 'output/y_train.joblib')
    dump(y_val, 'output/y_val.joblib')
    dump(y_test, 'output/y_test.joblib')


    # print('Max index in x_train:', np.max(x_train))
    # print('Min index in x_train:', np.min(x_train))

    # print('Max index in x_test:', np.max(x_test))
    # print('Min index in x_test:', np.min(x_test))

    # print('Max index in x_val:', np.max(x_val))
    # print('Min index in x_val:', np.min(x_val))


if __name__ == "__main__":
    main()