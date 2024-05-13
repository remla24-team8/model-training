
from keras.models import Sequential
from keras.layers import Embedding, Conv1D, MaxPooling1D, Flatten, Dense, Dropout


#model definition
def create_model(char_index,num_categories, embedding_dimension):
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


    model = Sequential()

    voc_size = len(char_index.keys())
    print("voc_size: {}".format(voc_size))
    model.add(Embedding(input_dim = voc_size+1, output_dim = embedding_dimension))

    model.add(Conv1D(128, 3, activation='tanh'))
    model.add(MaxPooling1D(3))
    model.add(Dropout(0.2))

    model.add(Conv1D(128, 7, activation='tanh', padding='same'))
    model.add(Dropout(0.2))

    model.add(Conv1D(128, 5, activation='tanh', padding='same'))
    model.add(Dropout(0.2))

    model.add(Conv1D(128, 3, activation='tanh', padding='same'))
    model.add(MaxPooling1D(3))
    model.add(Dropout(0.2))

    model.add(Conv1D(128, 5, activation='tanh', padding='same'))
    model.add(Dropout(0.2))

    model.add(Conv1D(128, 3, activation='tanh', padding='same'))
    model.add(MaxPooling1D(3))
    model.add(Dropout(0.2))

    model.add(Conv1D(128, 3, activation='tanh', padding='same'))
    model.add(MaxPooling1D(3))
    model.add(Dropout(0.2))

    model.add(Flatten())

    model.add(Dense(num_categories-1, activation='sigmoid'))
    return model 

